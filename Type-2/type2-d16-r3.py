import os
import time

def set_smtlib2(rounds):
    smtlib2_constr = []
    smtlib2_constr.append("(set-logic QF_BV)\n\n")

    for r in range(rounds):
        # Declare variables
        for i in range(16):
            smtlib2_constr.append(f"(declare-fun x_{i}_{r}_0 () (_ BitVec 2))\n")
        
        for i in range(1, 16, 2):
            smtlib2_constr.append(f"(declare-fun y_{i}_{r}_1 () (_ BitVec 2))\n")
        
        for i in range(8):
            smtlib2_constr.append(f"(declare-fun z_{i}_{r}_0 () (_ BitVec 2))\n")
        
        for i in range(16):
            smtlib2_constr.append(f"(declare-fun y_{i}_{r}_0 () (_ BitVec 2))\n")
        
        smtlib2_constr.append("\n")

    smtlib2_constr.append(f"(define-fun Table ((key (_ BitVec 6))) (_ BitVec 1)\n")
    smtlib2_constr.append(f"    (ite (or\n")
    smtlib2_constr.append(f"        (= key #b000000)\n")
    smtlib2_constr.append(f"        (= key #b000101)\n")
    smtlib2_constr.append(f"        (= key #b001111)\n")

    smtlib2_constr.append(f"        (= key #b010001)\n")
    smtlib2_constr.append(f"        (= key #b010100)\n")
    smtlib2_constr.append(f"        (= key #b010101)\n")
    smtlib2_constr.append(f"        (= key #b011111)\n")

    smtlib2_constr.append(f"        (= key #b110011)\n")
    smtlib2_constr.append(f"        (= key #b110111)\n")
    smtlib2_constr.append(f"        (= key #b111111)\n")
    smtlib2_constr.append(f"    ) #b1 #b0))\n")
    
    
    for r in range(rounds):
        # Assign
        if r > 0:
            for i in range(16):
                smtlib2_constr.append(f"(assert (= y_{i}_{r}_0 x_{i}_{r-1}_0))\n")
        smtlib2_constr.append("\n")

        # Pass through F
        for i in range(1, 16, 2):
            smtlib2_constr.append(f"(assert (= y_{i}_{r}_1 (ite (= y_{i}_{r}_0 #b00) #b00 #b11)))\n")
        smtlib2_constr.append("\n")

        # XOR
        smtlib2_constr.append(f"(assert (= (Table (concat (concat y_15_{r}_1 y_0_{r}_0) z_0_{r}_0)) #b1))\n")
        smtlib2_constr.append(f"(assert (= (Table (concat (concat y_1_{r}_1 y_2_{r}_0) z_1_{r}_0)) #b1))\n")
        smtlib2_constr.append(f"(assert (= (Table (concat (concat y_3_{r}_1 y_4_{r}_0) z_2_{r}_0)) #b1))\n")
        smtlib2_constr.append(f"(assert (= (Table (concat (concat y_5_{r}_1 y_6_{r}_0) z_3_{r}_0)) #b1))\n")
        smtlib2_constr.append(f"(assert (= (Table (concat (concat y_7_{r}_1 y_8_{r}_0) z_4_{r}_0)) #b1))\n")
        smtlib2_constr.append(f"(assert (= (Table (concat (concat y_9_{r}_1 y_10_{r}_0) z_5_{r}_0)) #b1))\n")
        smtlib2_constr.append(f"(assert (= (Table (concat (concat y_11_{r}_1 y_12_{r}_0) z_6_{r}_0)) #b1))\n")
        smtlib2_constr.append(f"(assert (= (Table (concat (concat y_13_{r}_1 y_14_{r}_0) z_7_{r}_0)) #b1))\n")


        # Permutation
        smtlib2_constr.append(f"(assert (= x_0_{r}_0 y_15_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= x_1_{r}_0 z_0_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= x_2_{r}_0 y_1_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= x_3_{r}_0 z_1_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= x_4_{r}_0 y_3_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= x_5_{r}_0 z_2_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= x_6_{r}_0 y_5_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= x_7_{r}_0 z_3_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= x_8_{r}_0 y_7_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= x_9_{r}_0 z_4_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= x_10_{r}_0 y_9_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= x_11_{r}_0 z_5_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= x_12_{r}_0 y_11_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= x_13_{r}_0 z_6_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= x_14_{r}_0 y_13_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= x_15_{r}_0 z_7_{r}_0))\n\n")

    # Active constraints
    for i in range(8):
        smtlib2_constr.append(f"(declare-fun active_{i+1} () (_ BitVec 1))\n")
    
    smtlib2_constr.append(f"(assert (= active_1 (ite (= y_1_{rounds-1}_0 #b00) #b0 #b1)))\n")
    smtlib2_constr.append(f"(assert (= active_2 (ite (= y_3_{rounds-1}_0 #b00) #b0 #b1)))\n")
    smtlib2_constr.append(f"(assert (= active_3 (ite (= y_5_{rounds-1}_0 #b00) #b0 #b1)))\n")
    smtlib2_constr.append(f"(assert (= active_4 (ite (= y_7_{rounds-1}_0 #b00) #b0 #b1)))\n")
    smtlib2_constr.append(f"(assert (= active_5 (ite (= y_9_{rounds-1}_0 #b00) #b0 #b1)))\n")
    smtlib2_constr.append(f"(assert (= active_6 (ite (= y_11_{rounds-1}_0 #b00) #b0 #b1)))\n")
    smtlib2_constr.append(f"(assert (= active_7 (ite (= y_13_{rounds-1}_0 #b00) #b0 #b1)))\n")
    smtlib2_constr.append(f"(assert (= active_8 (ite (= y_15_{rounds-1}_0 #b00) #b0 #b1)))\n")
    
    and_expr = "active_1"
    for i in range(2, 9):
        and_expr = f"(bvand {and_expr} active_{i})"
    smtlib2_constr.append(f"(assert (= {and_expr} #b0))\n\n")

    # Input constraints
    y_bits = []
    for i in range(16):
        y_bits.append(f"y_{i}_0_0")

    concat_expr = y_bits[0]
    for bit in y_bits[1:]:
        concat_expr = f"(concat {concat_expr} {bit})"

    smtlib2_constr.append(f"(assert (not (= {concat_expr} #b00000000000000000000000000000000)))\n")

    for i in range(16):
        smtlib2_constr.append(f"(assert (not (= y_{i}_0_0 #b11)))\n")
        smtlib2_constr.append(f"(assert (not (= y_{i}_0_0 #b10)))\n")
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
    target = "type2-d16-r3"
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
        print("max-r3 =", rounds - 1)

    end = time.time()
    print("time: {:.2f} s".format(end - start))
    remove_file(target, rounds)