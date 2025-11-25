import os
import time

def set_smtlib2(rounds):
    smtlib2_constr = []
    smtlib2_constr.append("(set-logic QF_BV)\n\n")

    # declare variables
    for r in range(rounds):
        for i in range(16):
            smtlib2_constr.append(f"(declare-fun x_{i}_{r}_0 () (_ BitVec 2))\n")
        
        for i in [0, 2, 4, 6, 8, 10, 12, 14]:
            smtlib2_constr.append(f"(declare-fun x_{i}_{r}_1 () (_ BitVec 2))\n")
        
        for i in range(8):
            smtlib2_constr.append(f"(declare-fun z_{i}_{r}_0 () (_ BitVec 2))\n")
        
        for i in range(16):
            smtlib2_constr.append(f"(declare-fun y_{i}_{r} () (_ BitVec 2))\n")
        
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
                smtlib2_constr.append(f"(assert (= x_{i}_{r}_0 y_{i}_{r-1}))\n")
        smtlib2_constr.append("\n")

        # F function
        for i in [0, 2, 4, 6, 8, 10, 12, 14]:
            smtlib2_constr.append(f"(assert (= x_{i}_{r}_1 (ite (= x_{i}_{r}_0 #b00) #b00 #b11)))\n")
        smtlib2_constr.append("\n")


        # XOR
        smtlib2_constr.append(f"(assert (= (Table (concat (concat x_0_{r}_1 x_1_{r}_0) z_0_{r}_0)) #b1))\n")
        smtlib2_constr.append(f"(assert (= (Table (concat (concat x_2_{r}_1 x_3_{r}_0) z_1_{r}_0)) #b1))\n")
        smtlib2_constr.append(f"(assert (= (Table (concat (concat x_4_{r}_1 x_5_{r}_0) z_2_{r}_0)) #b1))\n")
        smtlib2_constr.append(f"(assert (= (Table (concat (concat x_6_{r}_1 x_7_{r}_0) z_3_{r}_0)) #b1))\n")
        smtlib2_constr.append(f"(assert (= (Table (concat (concat x_8_{r}_1 x_9_{r}_0) z_4_{r}_0)) #b1))\n")
        smtlib2_constr.append(f"(assert (= (Table (concat (concat x_10_{r}_1 x_11_{r}_0) z_5_{r}_0)) #b1))\n")
        smtlib2_constr.append(f"(assert (= (Table (concat (concat x_12_{r}_1 x_13_{r}_0) z_6_{r}_0)) #b1))\n")
        smtlib2_constr.append(f"(assert (= (Table (concat (concat x_14_{r}_1 x_15_{r}_0) z_7_{r}_0)) #b1))\n")


        # Permutation {1,2,9,4,15,6,5,8,13,10,7,14,11,12,3,0}
        smtlib2_constr.append(f"(assert (= y_0_{r} z_7_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_1_{r} x_0_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_2_{r} z_0_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_3_{r} x_14_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_4_{r} z_1_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_5_{r} x_6_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_6_{r} z_2_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_7_{r} x_10_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_8_{r} z_3_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_9_{r} x_2_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_10_{r} z_4_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_11_{r} x_12_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_12_{r} z_6_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_13_{r} x_8_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_14_{r} z_5_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_15_{r} x_4_{r}_0))\n\n")

    smtlib2_constr.append("(declare-fun active_1 () (_ BitVec 1))\n")
    smtlib2_constr.append("(declare-fun active_2 () (_ BitVec 1))\n")
    smtlib2_constr.append("(declare-fun active_3 () (_ BitVec 1))\n")
    smtlib2_constr.append("(declare-fun active_4 () (_ BitVec 1))\n")
    smtlib2_constr.append("(declare-fun active_5 () (_ BitVec 1))\n")
    smtlib2_constr.append("(declare-fun active_6 () (_ BitVec 1))\n")
    smtlib2_constr.append("(declare-fun active_7 () (_ BitVec 1))\n")
    smtlib2_constr.append("(declare-fun active_8 () (_ BitVec 1))\n\n")

    smtlib2_constr.append(f"(assert (= active_1 (ite (= x_0_{rounds-1}_0 #b00) #b0 #b1)))\n")
    smtlib2_constr.append(f"(assert (= active_2 (ite (= x_2_{rounds-1}_0 #b00) #b0 #b1)))\n")
    smtlib2_constr.append(f"(assert (= active_3 (ite (= x_4_{rounds-1}_0 #b00) #b0 #b1)))\n")
    smtlib2_constr.append(f"(assert (= active_4 (ite (= x_6_{rounds-1}_0 #b00) #b0 #b1)))\n")
    smtlib2_constr.append(f"(assert (= active_5 (ite (= x_8_{rounds-1}_0 #b00) #b0 #b1)))\n")
    smtlib2_constr.append(f"(assert (= active_6 (ite (= x_10_{rounds-1}_0 #b00) #b0 #b1)))\n")
    smtlib2_constr.append(f"(assert (= active_7 (ite (= x_12_{rounds-1}_0 #b00) #b0 #b1)))\n")
    smtlib2_constr.append(f"(assert (= active_8 (ite (= x_14_{rounds-1}_0 #b00) #b0 #b1)))\n")
    
    smtlib2_constr.append("(assert (= (bvand active_1 (bvand active_2 (bvand active_3 (bvand active_4 (bvand active_5 (bvand active_6 (bvand active_7 active_8))))))) #b0))\n\n")

    smtlib2_constr.append(
        "(assert (not (= (concat x_0_0_0 (concat x_1_0_0 (concat x_2_0_0 (concat x_3_0_0 (concat x_4_0_0 (concat x_5_0_0 (concat x_6_0_0 (concat x_7_0_0 (concat x_8_0_0 (concat x_9_0_0 (concat x_10_0_0 (concat x_11_0_0 (concat x_12_0_0 (concat x_13_0_0 (concat x_14_0_0 x_15_0_0))))))))))))))) #b00000000000000000000000000000000)))\n"
    )
    
    # Constraints
    for i in range(16):
        smtlib2_constr.append(f"(assert (not (= x_{i}_0_0 #b11)))\n")
        smtlib2_constr.append(f"(assert (not (= x_{i}_0_0 #b10)))\n")
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
    target = "sm-d16-r1"
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