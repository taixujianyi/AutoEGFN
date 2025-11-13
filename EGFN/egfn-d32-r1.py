import os
import time

def set_smtlib2(rounds):
    smtlib2_constr = []
    smtlib2_constr.append("(set-logic QF_BV)\n\n")

    # Declare variables
    for r in range(rounds):
        for i in range(32):
            smtlib2_constr.append(f"(declare-fun x_{i}_{r}_0 () (_ BitVec 2))\n")
        
        for i in range(16):
            smtlib2_constr.append(f"(declare-fun x_{i}_{r}_1 () (_ BitVec 2))\n")
        
        for i in range(16, 32):
            smtlib2_constr.append(f"(declare-fun z_{i}_{r}_0 () (_ BitVec 2))\n")
        
        for i in range(17, 31):
            smtlib2_constr.append(f"(declare-fun z_{i}_{r}_1 () (_ BitVec 2))\n")
        
        for i in range(1, 16):
            smtlib2_constr.append(f"(declare-fun z_31_{r}_{i} () (_ BitVec 2))\n")
        
        for i in range(32):
            smtlib2_constr.append(f"(declare-fun y_{i}_{r} () (_ BitVec 2))\n")
        
        smtlib2_constr.append("\n")

    smtlib2_constr.append(f"(define-fun Table ((key (_ BitVec 6))) (_ BitVec 1)\n")
    smtlib2_constr.append(f"    (ite (or\n")
    smtlib2_constr.append(f"        (= key #b000000)\n")
    smtlib2_constr.append(f"        (= key #b000101)\n")
    smtlib2_constr.append(f"        (= key #b001010)\n")
    smtlib2_constr.append(f"        (= key #b001111)\n")

    smtlib2_constr.append(f"        (= key #b010001)\n")
    smtlib2_constr.append(f"        (= key #b010100)\n")
    smtlib2_constr.append(f"        (= key #b010101)\n")
    smtlib2_constr.append(f"        (= key #b011011)\n")
    smtlib2_constr.append(f"        (= key #b011111)\n")

    smtlib2_constr.append(f"        (= key #b100010)\n")
    smtlib2_constr.append(f"        (= key #b100111)\n")
    smtlib2_constr.append(f"        (= key #b101000)\n")
    smtlib2_constr.append(f"        (= key #b101010)\n")
    smtlib2_constr.append(f"        (= key #b101111)\n")

    smtlib2_constr.append(f"        (= key #b110011)\n")
    smtlib2_constr.append(f"        (= key #b110111)\n")
    smtlib2_constr.append(f"        (= key #b111011)\n")
    smtlib2_constr.append(f"        (= key #b111111)\n")
    smtlib2_constr.append(f"    ) #b1 #b0))\n")

    for r in range(rounds):
        if r > 0:
            for i in range(32):
                smtlib2_constr.append(f"(assert (= x_{i}_{r}_0 y_{i}_{r-1}))\n")
        smtlib2_constr.append("\n")

        # F function
        for i in range(16):
            smtlib2_constr.append(f"(assert (= x_{i}_{r}_1 (ite (= x_{i}_{r}_0 #b00) #b00 #b11)))\n")
        smtlib2_constr.append("\n")

        # XOR
        for i in range(16, 32):
            control_idx = 31 - i
            smtlib2_constr.append(f"(assert (= (Table (concat (concat x_{control_idx}_{r}_1 x_{i}_{r}_0) z_{i}_{r}_0)) #b1))\n")
            smtlib2_constr.append("\n")

        smtlib2_constr.append(f"(assert (= (Table (concat (concat x_1_{r}_0 z_31_{r}_0) z_31_{r}_1)) #b1))\n")
        smtlib2_constr.append("\n")
        
        for i in range(2, 16):
            smtlib2_constr.append(f"(assert (= (Table (concat (concat x_{i}_{r}_0 z_31_{r}_{i-1}) z_31_{r}_{i})) #b1))\n")
            smtlib2_constr.append("\n")

        for i in range(1, 15):
            control_idx = 31 - i
            smtlib2_constr.append(f"(assert (= (Table (concat (concat x_15_{r}_0 z_{control_idx}_{r}_0) z_{control_idx}_{r}_1)) #b1))\n")
            smtlib2_constr.append("\n")

        # Permutation
        smtlib2_constr.append(f"(assert (= y_0_{r} z_16_{r}_0))\n")
        for i in range(17, 31):
            smtlib2_constr.append(f"(assert (= y_{i-16}_{r} z_{i}_{r}_1))\n")
        smtlib2_constr.append(f"(assert (= y_15_{r} z_31_{r}_15))\n")
        
        for i in range(16):
            smtlib2_constr.append(f"(assert (= y_{i+16}_{r} x_{i}_{r}_0))\n")
        
        smtlib2_constr.append("\n")

    # Active constraints
    active_vars = []
    for i in range(16):
        active_vars.append(f"active_{i+1}")
        smtlib2_constr.append(f"(declare-fun active_{i+1} () (_ BitVec 1))\n")
    
    for i in range(16):
        smtlib2_constr.append(f"(assert (= active_{i+1} (ite (= x_{i}_{rounds-1}_0 #b00) #b0 #b1)))\n")
    
    and_expr = active_vars[0]
    for var in active_vars[1:]:
        and_expr = f"(bvand {and_expr} {var})"
    smtlib2_constr.append(f"(assert (= {and_expr} #b0))\n\n")

    concat_terms = [f"x_{i}_0_0" for i in range(32)]
    concat_expr = concat_terms[0]
    for term in concat_terms[1:]:
        concat_expr = f"(concat {concat_expr} {term})"
    smtlib2_constr.append(f"(assert (not (= {concat_expr} #b{'0'*64})))\n")
    
    for i in range(32):
        smtlib2_constr.append(f"(assert (not (= x_{i}_0_0 #b11)))\n")
    smtlib2_constr.append("\n")

    smtlib2_constr.append("(check-sat)\n(get-model)\n")

    return smtlib2_constr

def run_stp(target, rounds):
    smtlib2_code = set_smtlib2(rounds)
    filename = f"{target}-round{rounds}.smt2"
    with open(filename, "w") as f:
        f.writelines(smtlib2_code)

    command = f"stp {filename}"
    output = os.popen(command)
    return output

def remove_file(target, rounds):
    for i in range(1, rounds + 1):
        filename = f"{target}-round{i}.smt2"
        if os.path.exists(filename):
            os.remove(filename)

if __name__ == '__main__':
    start = time.time()
    target = "egfn-d32-r1"
    rounds = 1
    print("round =", rounds)
    result = run_stp(target, rounds)
    result_str = result.read()
    print("result =", result_str)

    while "unsat" not in result_str:
        rounds += 1
        print("round =", rounds)
        result = run_stp(target, rounds)
        result_str = result.read()
        print("result =", result_str)
    else:
        print("max-r1 =", rounds - 1)

    end = time.time()
    print("time: {:.2f} s".format(end - start))
    remove_file(target, rounds)