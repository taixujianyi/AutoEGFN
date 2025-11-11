import os
import time

def set_smtlib2(rounds):
    smtlib2_constr = []
    smtlib2_constr.append("(set-logic QF_BV)\n\n")

    # declare variables
    for r in range(rounds):
        for i in range(16):
            smtlib2_constr.append(f"(declare-fun x_{i}_{r}_0 () (_ BitVec 2))\n")
        
        for i in [1, 3, 5, 7, 9, 11, 13, 15]:
            smtlib2_constr.append(f"(declare-fun y_{i}_{r}_1 () (_ BitVec 2))\n")
        
        for i in [0, 2, 4, 6, 8, 10, 12, 14]:
            smtlib2_constr.append(f"(declare-fun y_{i}_{r}_1 () (_ BitVec 2))\n")
        
        for i in [0, 2, 4, 6, 8, 10, 12, 14]:
            smtlib2_constr.append(f"(declare-fun y_{i}_{r}_2 () (_ BitVec 2))\n")
        
        for i in range(8):
            smtlib2_constr.append(f"(declare-fun z_{i}_{r}_0 () (_ BitVec 2))\n")
        
        for i in range(16):
            smtlib2_constr.append(f"(declare-fun y_{i}_{r}_0 () (_ BitVec 2))\n")
        
        smtlib2_constr.append("\n")

    for r in range(rounds):
        # Assign
        if r > 0:
            for i in range(16):
                smtlib2_constr.append(f"(assert (= y_{i}_{r}_0 x_{i}_{r-1}_0))\n")
        smtlib2_constr.append("\n")

        # Permutation {15,0,1,14,3,6,5,10,7,2,9,12,13,8,11,4}
        smtlib2_constr.append(f"(assert (= y_0_{r}_1 y_1_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_1_{r}_1 y_2_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_2_{r}_1 y_9_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_3_{r}_1 y_4_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_4_{r}_1 y_15_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_5_{r}_1 y_6_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_6_{r}_1 y_5_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_7_{r}_1 y_8_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_8_{r}_1 y_13_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_9_{r}_1 y_10_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_10_{r}_1 y_7_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_11_{r}_1 y_14_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_12_{r}_1 y_11_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_13_{r}_1 y_12_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_14_{r}_1 y_3_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_15_{r}_1 y_0_{r}_0))\n")
        smtlib2_constr.append("\n")

        # F function
        for i in [0, 2, 4, 6, 8, 10, 12, 14]:
            smtlib2_constr.append(f"(assert (= y_{i}_{r}_2 (ite (= y_{i}_{r}_1 #b00) #b00 #b11)))\n")
        smtlib2_constr.append("\n")

        # XOR operations
        smtlib2_constr.append(
            f"(assert (= z_0_{r}_0\n"
            f"    (ite (= y_0_{r}_2 #b00) y_1_{r}_1\n"
            f"    (ite (and (= y_0_{r}_2 #b01) (= y_1_{r}_1 #b00)) #b01\n"
            f"    (ite (and (= y_0_{r}_2 #b01) (= y_1_{r}_1 #b01)) #b01\n"
            f"    (ite (and (= y_0_{r}_2 #b01) (= y_1_{r}_1 #b10)) #b11\n"
            f"    (ite (and (= y_0_{r}_2 #b01) (= y_1_{r}_1 #b11)) #b11\n"
            f"    (ite (and (= y_0_{r}_2 #b10) (= y_1_{r}_1 #b00)) #b10\n"
            f"    (ite (and (= y_0_{r}_2 #b10) (= y_1_{r}_1 #b01)) #b11\n"
            f"    (ite (and (= y_0_{r}_2 #b10) (= y_1_{r}_1 #b10)) #b10\n"
            f"    (ite (and (= y_0_{r}_2 #b10) (= y_1_{r}_1 #b11)) #b11\n"
            f"    (ite (= y_0_{r}_2 #b11) #b11 #b00))))))))))))\n"
        )

        smtlib2_constr.append(
            f"(assert (= z_1_{r}_0\n"
            f"    (ite (= y_2_{r}_2 #b00) y_3_{r}_1\n"
            f"    (ite (and (= y_2_{r}_2 #b01) (= y_3_{r}_1 #b00)) #b01\n"
            f"    (ite (and (= y_2_{r}_2 #b01) (= y_3_{r}_1 #b01)) #b01\n"
            f"    (ite (and (= y_2_{r}_2 #b01) (= y_3_{r}_1 #b10)) #b11\n"
            f"    (ite (and (= y_2_{r}_2 #b01) (= y_3_{r}_1 #b11)) #b11\n"
            f"    (ite (and (= y_2_{r}_2 #b10) (= y_3_{r}_1 #b00)) #b10\n"
            f"    (ite (and (= y_2_{r}_2 #b10) (= y_3_{r}_1 #b01)) #b11\n"
            f"    (ite (and (= y_2_{r}_2 #b10) (= y_3_{r}_1 #b10)) #b10\n"
            f"    (ite (and (= y_2_{r}_2 #b10) (= y_3_{r}_1 #b11)) #b11\n"
            f"    (ite (= y_2_{r}_2 #b11) #b11 #b00))))))))))))\n"
        )

        smtlib2_constr.append(
            f"(assert (= z_2_{r}_0\n"
            f"    (ite (= y_4_{r}_2 #b00) y_5_{r}_1\n"
            f"    (ite (and (= y_4_{r}_2 #b01) (= y_5_{r}_1 #b00)) #b01\n"
            f"    (ite (and (= y_4_{r}_2 #b01) (= y_5_{r}_1 #b01)) #b01\n"
            f"    (ite (and (= y_4_{r}_2 #b01) (= y_5_{r}_1 #b10)) #b11\n"
            f"    (ite (and (= y_4_{r}_2 #b01) (= y_5_{r}_1 #b11)) #b11\n"
            f"    (ite (and (= y_4_{r}_2 #b10) (= y_5_{r}_1 #b00)) #b10\n"
            f"    (ite (and (= y_4_{r}_2 #b10) (= y_5_{r}_1 #b01)) #b11\n"
            f"    (ite (and (= y_4_{r}_2 #b10) (= y_5_{r}_1 #b10)) #b10\n"
            f"    (ite (and (= y_4_{r}_2 #b10) (= y_5_{r}_1 #b11)) #b11\n"
            f"    (ite (= y_4_{r}_2 #b11) #b11 #b00))))))))))))\n"
        )

        smtlib2_constr.append(
            f"(assert (= z_3_{r}_0\n"
            f"    (ite (= y_6_{r}_2 #b00) y_7_{r}_1\n"
            f"    (ite (and (= y_6_{r}_2 #b01) (= y_7_{r}_1 #b00)) #b01\n"
            f"    (ite (and (= y_6_{r}_2 #b01) (= y_7_{r}_1 #b01)) #b01\n"
            f"    (ite (and (= y_6_{r}_2 #b01) (= y_7_{r}_1 #b10)) #b11\n"
            f"    (ite (and (= y_6_{r}_2 #b01) (= y_7_{r}_1 #b11)) #b11\n"
            f"    (ite (and (= y_6_{r}_2 #b10) (= y_7_{r}_1 #b00)) #b10\n"
            f"    (ite (and (= y_6_{r}_2 #b10) (= y_7_{r}_1 #b01)) #b11\n"
            f"    (ite (and (= y_6_{r}_2 #b10) (= y_7_{r}_1 #b10)) #b10\n"
            f"    (ite (and (= y_6_{r}_2 #b10) (= y_7_{r}_1 #b11)) #b11\n"
            f"    (ite (= y_6_{r}_2 #b11) #b11 #b00))))))))))))\n"
        )

        smtlib2_constr.append(
            f"(assert (= z_4_{r}_0\n"
            f"    (ite (= y_8_{r}_2 #b00) y_9_{r}_1\n"
            f"    (ite (and (= y_8_{r}_2 #b01) (= y_9_{r}_1 #b00)) #b01\n"
            f"    (ite (and (= y_8_{r}_2 #b01) (= y_9_{r}_1 #b01)) #b01\n"
            f"    (ite (and (= y_8_{r}_2 #b01) (= y_9_{r}_1 #b10)) #b11\n"
            f"    (ite (and (= y_8_{r}_2 #b01) (= y_9_{r}_1 #b11)) #b11\n"
            f"    (ite (and (= y_8_{r}_2 #b10) (= y_9_{r}_1 #b00)) #b10\n"
            f"    (ite (and (= y_8_{r}_2 #b10) (= y_9_{r}_1 #b01)) #b11\n"
            f"    (ite (and (= y_8_{r}_2 #b10) (= y_9_{r}_1 #b10)) #b10\n"
            f"    (ite (and (= y_8_{r}_2 #b10) (= y_9_{r}_1 #b11)) #b11\n"
            f"    (ite (= y_8_{r}_2 #b11) #b11 #b00))))))))))))\n"
        )

        smtlib2_constr.append(
            f"(assert (= z_5_{r}_0\n"
            f"    (ite (= y_10_{r}_2 #b00) y_11_{r}_1\n"
            f"    (ite (and (= y_10_{r}_2 #b01) (= y_11_{r}_1 #b00)) #b01\n"
            f"    (ite (and (= y_10_{r}_2 #b01) (= y_11_{r}_1 #b01)) #b01\n"
            f"    (ite (and (= y_10_{r}_2 #b01) (= y_11_{r}_1 #b10)) #b11\n"
            f"    (ite (and (= y_10_{r}_2 #b01) (= y_11_{r}_1 #b11)) #b11\n"
            f"    (ite (and (= y_10_{r}_2 #b10) (= y_11_{r}_1 #b00)) #b10\n"
            f"    (ite (and (= y_10_{r}_2 #b10) (= y_11_{r}_1 #b01)) #b11\n"
            f"    (ite (and (= y_10_{r}_2 #b10) (= y_11_{r}_1 #b10)) #b10\n"
            f"    (ite (and (= y_10_{r}_2 #b10) (= y_11_{r}_1 #b11)) #b11\n"
            f"    (ite (= y_10_{r}_2 #b11) #b11 #b00))))))))))))\n"
        )

        smtlib2_constr.append(
            f"(assert (= z_6_{r}_0\n"
            f"    (ite (= y_12_{r}_2 #b00) y_13_{r}_1\n"
            f"    (ite (and (= y_12_{r}_2 #b01) (= y_13_{r}_1 #b00)) #b01\n"
            f"    (ite (and (= y_12_{r}_2 #b01) (= y_13_{r}_1 #b01)) #b01\n"
            f"    (ite (and (= y_12_{r}_2 #b01) (= y_13_{r}_1 #b10)) #b11\n"
            f"    (ite (and (= y_12_{r}_2 #b01) (= y_13_{r}_1 #b11)) #b11\n"
            f"    (ite (and (= y_12_{r}_2 #b10) (= y_13_{r}_1 #b00)) #b10\n"
            f"    (ite (and (= y_12_{r}_2 #b10) (= y_13_{r}_1 #b01)) #b11\n"
            f"    (ite (and (= y_12_{r}_2 #b10) (= y_13_{r}_1 #b10)) #b10\n"
            f"    (ite (and (= y_12_{r}_2 #b10) (= y_13_{r}_1 #b11)) #b11\n"
            f"    (ite (= y_12_{r}_2 #b11) #b11 #b00))))))))))))\n"
        )

        smtlib2_constr.append(
            f"(assert (= z_7_{r}_0\n"
            f"    (ite (= y_14_{r}_2 #b00) y_15_{r}_1\n"
            f"    (ite (and (= y_14_{r}_2 #b01) (= y_15_{r}_1 #b00)) #b01\n"
            f"    (ite (and (= y_14_{r}_2 #b01) (= y_15_{r}_1 #b01)) #b01\n"
            f"    (ite (and (= y_14_{r}_2 #b01) (= y_15_{r}_1 #b10)) #b11\n"
            f"    (ite (and (= y_14_{r}_2 #b01) (= y_15_{r}_1 #b11)) #b11\n"
            f"    (ite (and (= y_14_{r}_2 #b10) (= y_15_{r}_1 #b00)) #b10\n"
            f"    (ite (and (= y_14_{r}_2 #b10) (= y_15_{r}_1 #b01)) #b11\n"
            f"    (ite (and (= y_14_{r}_2 #b10) (= y_15_{r}_1 #b10)) #b10\n"
            f"    (ite (and (= y_14_{r}_2 #b10) (= y_15_{r}_1 #b11)) #b11\n"
            f"    (ite (= y_14_{r}_2 #b11) #b11 #b00))))))))))))\n"
        )
        smtlib2_constr.append("\n")

        # Permutation
        smtlib2_constr.append(f"(assert (= x_0_{r}_0 y_0_{r}_1))\n")
        smtlib2_constr.append(f"(assert (= x_1_{r}_0 z_0_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= x_2_{r}_0 y_2_{r}_1))\n")
        smtlib2_constr.append(f"(assert (= x_3_{r}_0 z_1_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= x_4_{r}_0 y_4_{r}_1))\n")
        smtlib2_constr.append(f"(assert (= x_5_{r}_0 z_2_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= x_6_{r}_0 y_6_{r}_1))\n")
        smtlib2_constr.append(f"(assert (= x_7_{r}_0 z_3_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= x_8_{r}_0 y_8_{r}_1))\n")
        smtlib2_constr.append(f"(assert (= x_9_{r}_0 z_4_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= x_10_{r}_0 y_10_{r}_1))\n")
        smtlib2_constr.append(f"(assert (= x_11_{r}_0 z_5_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= x_12_{r}_0 y_12_{r}_1))\n")
        smtlib2_constr.append(f"(assert (= x_13_{r}_0 z_6_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= x_14_{r}_0 y_14_{r}_1))\n")
        smtlib2_constr.append(f"(assert (= x_15_{r}_0 z_7_{r}_0))\n\n")

    smtlib2_constr.append("(declare-fun active_1 () (_ BitVec 1))\n")
    smtlib2_constr.append("(declare-fun active_2 () (_ BitVec 1))\n")
    smtlib2_constr.append("(declare-fun active_3 () (_ BitVec 1))\n")
    smtlib2_constr.append("(declare-fun active_4 () (_ BitVec 1))\n")
    smtlib2_constr.append("(declare-fun active_5 () (_ BitVec 1))\n")
    smtlib2_constr.append("(declare-fun active_6 () (_ BitVec 1))\n")
    smtlib2_constr.append("(declare-fun active_7 () (_ BitVec 1))\n")
    smtlib2_constr.append("(declare-fun active_8 () (_ BitVec 1))\n\n")

    smtlib2_constr.append(f"(assert (= active_1 (ite (= y_0_{rounds-1}_1 #b00) #b0 #b1)))\n")
    smtlib2_constr.append(f"(assert (= active_2 (ite (= y_2_{rounds-1}_1 #b00) #b0 #b1)))\n")
    smtlib2_constr.append(f"(assert (= active_3 (ite (= y_4_{rounds-1}_1 #b00) #b0 #b1)))\n")
    smtlib2_constr.append(f"(assert (= active_4 (ite (= y_6_{rounds-1}_1 #b00) #b0 #b1)))\n")
    smtlib2_constr.append(f"(assert (= active_5 (ite (= y_8_{rounds-1}_1 #b00) #b0 #b1)))\n")
    smtlib2_constr.append(f"(assert (= active_6 (ite (= y_10_{rounds-1}_1 #b00) #b0 #b1)))\n")
    smtlib2_constr.append(f"(assert (= active_7 (ite (= y_12_{rounds-1}_1 #b00) #b0 #b1)))\n")
    smtlib2_constr.append(f"(assert (= active_8 (ite (= y_14_{rounds-1}_1 #b00) #b0 #b1)))\n")
    
    smtlib2_constr.append("(assert (= (bvand active_1 (bvand active_2 (bvand active_3 (bvand active_4 (bvand active_5 (bvand active_6 (bvand active_7 active_8))))))) #b0))\n\n")
    smtlib2_constr.append(
        "(assert (not (= (concat y_0_0_0 (concat y_1_0_0 (concat y_2_0_0 (concat y_3_0_0 (concat y_4_0_0 (concat y_5_0_0 (concat y_6_0_0 (concat y_7_0_0 (concat y_8_0_0 (concat y_9_0_0 (concat y_10_0_0 (concat y_11_0_0 (concat y_12_0_0 (concat y_13_0_0 (concat y_14_0_0 y_15_0_0))))))))))))))) #b00000000000000000000000000000000)))\n"
    )
    
    # Constraints
    for i in range(16):
        smtlib2_constr.append(f"(assert (not (= y_{i}_0_0 #b11)))\n")
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
    target = "sm-d16-r3"
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