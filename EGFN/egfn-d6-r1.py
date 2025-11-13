import os
import time

def set_smtlib2(rounds):
    smtlib2_constr = []
    smtlib2_constr.append("(set-logic QF_BV)\n\n")

    # Declare variables
    for r in range(rounds):
        for i in range(6):
            smtlib2_constr.append(f"(declare-fun x_{i}_{r}_0 () (_ BitVec 2))\n")
        
        for i in range(3):
            smtlib2_constr.append(f"(declare-fun x_{i}_{r}_1 () (_ BitVec 2))\n")
        
        for i in range(3):
            smtlib2_constr.append(f"(declare-fun z_{i}_{r}_0 () (_ BitVec 2))\n")
        
        smtlib2_constr.append(f"(declare-fun z_2_{r}_1 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun z_2_{r}_2 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun z_1_{r}_1 () (_ BitVec 2))\n")
        
        for i in range(6):
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
            for i in range(6):
                smtlib2_constr.append(f"(assert (= x_{i}_{r}_0 y_{i}_{r-1}))\n")
        smtlib2_constr.append("\n")

        # F functions
        smtlib2_constr.append(f"(assert (= x_0_{r}_1 (ite (= x_0_{r}_0 #b00) #b00 #b11)))\n")
        smtlib2_constr.append(f"(assert (= x_1_{r}_1 (ite (= x_1_{r}_0 #b00) #b00 #b11)))\n")
        smtlib2_constr.append(f"(assert (= x_2_{r}_1 (ite (= x_2_{r}_0 #b00) #b00 #b11)))\n")
        smtlib2_constr.append("\n")

        # XOR
        smtlib2_constr.append(f"(assert (= (Table (concat (concat x_2_{r}_1 x_3_{r}_0) z_0_{r}_0)) #b1))\n")
        smtlib2_constr.append(f"(assert (= (Table (concat (concat x_1_{r}_1 x_4_{r}_0) z_1_{r}_0)) #b1))\n")
        smtlib2_constr.append(f"(assert (= (Table (concat (concat x_0_{r}_1 x_5_{r}_0) z_2_{r}_0)) #b1))\n")
        smtlib2_constr.append(f"(assert (= (Table (concat (concat x_1_{r}_0 z_2_{r}_0) z_2_{r}_1)) #b1))\n")
        smtlib2_constr.append(f"(assert (= (Table (concat (concat x_2_{r}_0 z_2_{r}_1) z_2_{r}_2)) #b1))\n")
        smtlib2_constr.append(f"(assert (= (Table (concat (concat x_2_{r}_0 z_1_{r}_0) z_1_{r}_1)) #b1))\n")

        # Permutation
        smtlib2_constr.append(f"(assert (= y_0_{r} z_0_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_1_{r} z_1_{r}_1))\n")
        smtlib2_constr.append(f"(assert (= y_2_{r} z_2_{r}_2))\n")
        smtlib2_constr.append(f"(assert (= y_3_{r} x_0_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_4_{r} x_1_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_5_{r} x_2_{r}_0))\n\n")

    # Active constraints
    smtlib2_constr.append("(declare-fun active_1 () (_ BitVec 1))\n")
    smtlib2_constr.append("(declare-fun active_2 () (_ BitVec 1))\n")
    smtlib2_constr.append("(declare-fun active_3 () (_ BitVec 1))\n")
    
    smtlib2_constr.append(f"(assert (= active_1 (ite (= x_0_{rounds-1}_0 #b00) #b0 #b1)))\n")
    smtlib2_constr.append(f"(assert (= active_2 (ite (= x_1_{rounds-1}_0 #b00) #b0 #b1)))\n")
    smtlib2_constr.append(f"(assert (= active_3 (ite (= x_2_{rounds-1}_0 #b00) #b0 #b1)))\n")
    
    and_expr = "(bvand active_1 (bvand active_2 active_3))"
    smtlib2_constr.append(f"(assert (= {and_expr} #b0))\n\n")

    concat_expr = "(concat x_0_0_0 (concat x_1_0_0 (concat x_2_0_0 (concat x_3_0_0 (concat x_4_0_0 x_5_0_0)))))"
    smtlib2_constr.append(f"(assert (not (= {concat_expr} #b000000000000)))\n")
    for i in range(6):
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
    target = "egfn-d6-r1"
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