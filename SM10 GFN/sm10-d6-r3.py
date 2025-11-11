import os
import time

def set_smtlib2(rounds):
    smtlib2_constr = []
    smtlib2_constr.append("(set-logic QF_BV)\n\n")

    # declare variables
    for r in range(rounds):
        smtlib2_constr.append(f"(declare-fun x_0_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun x_1_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun x_2_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun x_3_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun x_4_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun x_5_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_0_{r}_2 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_2_{r}_2 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_4_{r}_2 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun z_0_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun z_1_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun z_2_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_0_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_1_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_2_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_3_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_4_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_5_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_0_{r}_1 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_1_{r}_1 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_2_{r}_1 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_3_{r}_1 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_4_{r}_1 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_5_{r}_1 () (_ BitVec 2))\n\n")

    for r in range(rounds):
        # Assign
        if r > 0:
            smtlib2_constr.append(f"(assert (= y_0_{r}_0 x_0_{r-1}_0))\n")
            smtlib2_constr.append(f"(assert (= y_1_{r}_0 x_1_{r-1}_0))\n")
            smtlib2_constr.append(f"(assert (= y_2_{r}_0 x_2_{r-1}_0))\n")
            smtlib2_constr.append(f"(assert (= y_3_{r}_0 x_3_{r-1}_0))\n")
            smtlib2_constr.append(f"(assert (= y_4_{r}_0 x_4_{r-1}_0))\n")
            smtlib2_constr.append(f"(assert (= y_5_{r}_0 x_5_{r-1}_0))\n")
        smtlib2_constr.append("\n")

        # Permutation {1,2,5,0,3,4}
        smtlib2_constr.append(f"(assert (= y_0_{r}_1 y_3_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_1_{r}_1 y_0_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_2_{r}_1 y_1_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_3_{r}_1 y_4_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_4_{r}_1 y_5_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_5_{r}_1 y_2_{r}_0))\n")
        smtlib2_constr.append("\n")

        # F functions
        smtlib2_constr.append(f"(assert (= y_0_{r}_2 (ite (= y_0_{r}_1 #b00) #b00 #b11)))\n")
        smtlib2_constr.append(f"(assert (= y_2_{r}_2 (ite (= y_2_{r}_1 #b00) #b00 #b11)))\n")
        smtlib2_constr.append(f"(assert (= y_4_{r}_2 (ite (= y_4_{r}_1 #b00) #b00 #b11)))\n")
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
        smtlib2_constr.append("\n")

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
        smtlib2_constr.append("\n")

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
        smtlib2_constr.append("\n")

        # Permutation
        smtlib2_constr.append(f"(assert (= x_0_{r}_0 y_0_{r}_1))\n")
        smtlib2_constr.append(f"(assert (= x_1_{r}_0 z_0_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= x_2_{r}_0 y_2_{r}_1))\n")
        smtlib2_constr.append(f"(assert (= x_3_{r}_0 z_1_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= x_4_{r}_0 y_4_{r}_1))\n")
        smtlib2_constr.append(f"(assert (= x_5_{r}_0 z_2_{r}_0))\n\n")

    smtlib2_constr.append(f"(assert (= (bvand y_0_{rounds-1}_1 (bvand y_2_{rounds-1}_1 y_4_{rounds-1}_1)) #b00))\n")
    smtlib2_constr.append("\n")

    # Constraints
    smtlib2_constr.append("(assert (not (= (concat y_0_0_0 (concat y_1_0_0 (concat y_2_0_0 (concat y_3_0_0 (concat y_4_0_0 y_5_0_0))))) #b000000000000)))\n")
    
    for i in range(6):
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
    target = "sm-d6-r3"
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