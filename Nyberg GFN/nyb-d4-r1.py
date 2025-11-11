import os
import time

def set_smtlib2(rounds):
    smtlib2_constr = []
    smtlib2_constr.append("(set-logic QF_BV)\n\n")

    # declare variables
    for r in range(rounds):
        for i in range(4):
            smtlib2_constr.append(f"(declare-fun x_{i}_{r}_0 () (_ BitVec 2))\n")
        
        for i in [2, 3]:
            smtlib2_constr.append(f"(declare-fun x_{i}_{r}_1 () (_ BitVec 2))\n")
        
        for i in range(2):
            smtlib2_constr.append(f"(declare-fun z_{i}_{r}_0 () (_ BitVec 2))\n")
        
        for i in range(4):
            smtlib2_constr.append(f"(declare-fun y_{i}_{r} () (_ BitVec 2))\n")
        
        smtlib2_constr.append("\n")

    for r in range(rounds):
        # Assign
        if r > 0:
            for i in range(4):
                smtlib2_constr.append(f"(assert (= x_{i}_{r}_0 y_{i}_{r-1}))\n")
        smtlib2_constr.append("\n")

        # F function
        smtlib2_constr.append(f"(assert (= x_2_{r}_1 (ite (= x_2_{r}_0 #b00) #b00 #b11)))\n")
        smtlib2_constr.append(f"(assert (= x_3_{r}_1 (ite (= x_3_{r}_0 #b00) #b00 #b11)))\n")
        smtlib2_constr.append("\n")

        # XOR operations
        smtlib2_constr.append(
            f"(assert (= z_0_{r}_0\n"
            f"    (ite (= x_2_{r}_1 #b00) x_1_{r}_0\n"
            f"    (ite (and (= x_2_{r}_1 #b01) (= x_1_{r}_0 #b00)) #b01\n"
            f"    (ite (and (= x_2_{r}_1 #b01) (= x_1_{r}_0 #b01)) #b01\n"
            f"    (ite (and (= x_2_{r}_1 #b01) (= x_1_{r}_0 #b10)) #b11\n"
            f"    (ite (and (= x_2_{r}_1 #b01) (= x_1_{r}_0 #b11)) #b11\n"
            f"    (ite (and (= x_2_{r}_1 #b10) (= x_1_{r}_0 #b00)) #b10\n"
            f"    (ite (and (= x_2_{r}_1 #b10) (= x_1_{r}_0 #b01)) #b11\n"
            f"    (ite (and (= x_2_{r}_1 #b10) (= x_1_{r}_0 #b10)) #b10\n"
            f"    (ite (and (= x_2_{r}_1 #b10) (= x_1_{r}_0 #b11)) #b11\n"
            f"    (ite (= x_2_{r}_1 #b11) #b11 #b00))))))))))))\n"
        )

        smtlib2_constr.append(
            f"(assert (= z_1_{r}_0\n"
            f"    (ite (= x_3_{r}_1 #b00) x_0_{r}_0\n"
            f"    (ite (and (= x_3_{r}_1 #b01) (= x_0_{r}_0 #b00)) #b01\n"
            f"    (ite (and (= x_3_{r}_1 #b01) (= x_0_{r}_0 #b01)) #b01\n"
            f"    (ite (and (= x_3_{r}_1 #b01) (= x_0_{r}_0 #b10)) #b11\n"
            f"    (ite (and (= x_3_{r}_1 #b01) (= x_0_{r}_0 #b11)) #b11\n"
            f"    (ite (and (= x_3_{r}_1 #b10) (= x_0_{r}_0 #b00)) #b10\n"
            f"    (ite (and (= x_3_{r}_1 #b10) (= x_0_{r}_0 #b01)) #b11\n"
            f"    (ite (and (= x_3_{r}_1 #b10) (= x_0_{r}_0 #b10)) #b10\n"
            f"    (ite (and (= x_3_{r}_1 #b10) (= x_0_{r}_0 #b11)) #b11\n"
            f"    (ite (= x_3_{r}_1 #b11) #b11 #b00))))))))))))\n"
        )
        smtlib2_constr.append("\n")

        # Permutation
        smtlib2_constr.append(f"(assert (= y_0_{r} x_3_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_1_{r} z_1_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_2_{r} z_0_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_3_{r} x_2_{r}_0))\n\n")

    smtlib2_constr.append(f"(assert (= (bvand x_3_{rounds-1}_0 x_2_{rounds-1}_0) #b00))\n\n")
    smtlib2_constr.append(
        "(assert (not (= (concat x_0_0_0 (concat x_1_0_0 (concat x_2_0_0 x_3_0_0))) #b00000000)))\n"
    )
    
    # Constraints
    for i in range(4):
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
    target = "nyb-d4-r1"
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