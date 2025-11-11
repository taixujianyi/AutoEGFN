import os
import time

def set_smtlib2(rounds):
    smtlib2_constr = []
    smtlib2_constr.append("(set-logic QF_BV)\n\n")

    for r in range(rounds):
        smtlib2_constr.append(f"(declare-fun x_0_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun x_1_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun x_2_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun x_3_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun x_4_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun x_5_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun x_0_{r}_1 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun x_2_{r}_1 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun x_4_{r}_1 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun z_0_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun z_1_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun z_2_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_0_{r} () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_1_{r} () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_2_{r} () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_3_{r} () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_4_{r} () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_5_{r} () (_ BitVec 2))\n\n")

    for r in range(rounds):
        if r > 0:
            smtlib2_constr.append(f"(assert (= x_0_{r}_0 y_0_{r-1}))\n")
            smtlib2_constr.append(f"(assert (= x_1_{r}_0 y_1_{r-1}))\n")
            smtlib2_constr.append(f"(assert (= x_2_{r}_0 y_2_{r-1}))\n")
            smtlib2_constr.append(f"(assert (= x_3_{r}_0 y_3_{r-1}))\n")
            smtlib2_constr.append(f"(assert (= x_4_{r}_0 y_4_{r-1}))\n")
            smtlib2_constr.append(f"(assert (= x_5_{r}_0 y_5_{r-1}))\n")
        smtlib2_constr.append("\n")

        smtlib2_constr.append(f"(assert (= x_0_{r}_1 (ite (= x_0_{r}_0 #b00) #b00 #b11)))\n")
        smtlib2_constr.append(f"(assert (= x_2_{r}_1 (ite (= x_2_{r}_0 #b00) #b00 #b11)))\n")
        smtlib2_constr.append(f"(assert (= x_4_{r}_1 (ite (= x_4_{r}_0 #b00) #b00 #b11)))\n")
        smtlib2_constr.append("\n")

        smtlib2_constr.append(
            f"(assert (= z_0_{r}_0\n"
            f"    (ite (= x_0_{r}_1 #b00) x_1_{r}_0\n"
            f"         (ite (and (= x_0_{r}_1 #b01) (= x_1_{r}_0 #b00)) #b01\n"
            f"         (ite (and (= x_0_{r}_1 #b01) (= x_1_{r}_0 #b01)) #b01\n"
            f"         (ite (and (= x_0_{r}_1 #b01) (= x_1_{r}_0 #b10)) #b11\n"
            f"         (ite (and (= x_0_{r}_1 #b01) (= x_1_{r}_0 #b11)) #b11\n"
            f"         (ite (and (= x_0_{r}_1 #b10) (= x_1_{r}_0 #b00)) #b10\n"
            f"         (ite (and (= x_0_{r}_1 #b10) (= x_1_{r}_0 #b01)) #b11\n"
            f"         (ite (and (= x_0_{r}_1 #b10) (= x_1_{r}_0 #b10)) #b10\n"
            f"         (ite (and (= x_0_{r}_1 #b10) (= x_1_{r}_0 #b11)) #b11\n"
            f"         (ite (= x_0_{r}_1 #b11) #b11 #b00))))))))))))\n"
        )
        smtlib2_constr.append("\n")

        smtlib2_constr.append(
            f"(assert (= z_1_{r}_0\n"
            f"    (ite (= x_2_{r}_1 #b00) x_3_{r}_0\n"
            f"         (ite (and (= x_2_{r}_1 #b01) (= x_3_{r}_0 #b00)) #b01\n"
            f"         (ite (and (= x_2_{r}_1 #b01) (= x_3_{r}_0 #b01)) #b01\n"
            f"         (ite (and (= x_2_{r}_1 #b01) (= x_3_{r}_0 #b10)) #b11\n"
            f"         (ite (and (= x_2_{r}_1 #b01) (= x_3_{r}_0 #b11)) #b11\n"
            f"         (ite (and (= x_2_{r}_1 #b10) (= x_3_{r}_0 #b00)) #b10\n"
            f"         (ite (and (= x_2_{r}_1 #b10) (= x_3_{r}_0 #b01)) #b11\n"
            f"         (ite (and (= x_2_{r}_1 #b10) (= x_3_{r}_0 #b10)) #b10\n"
            f"         (ite (and (= x_2_{r}_1 #b10) (= x_3_{r}_0 #b11)) #b11\n"
            f"         (ite (= x_2_{r}_1 #b11) #b11 #b00))))))))))))\n"
        )
        smtlib2_constr.append("\n")

        smtlib2_constr.append(
            f"(assert (= z_2_{r}_0\n"
            f"    (ite (= x_4_{r}_1 #b00) x_5_{r}_0\n"
            f"         (ite (and (= x_4_{r}_1 #b01) (= x_5_{r}_0 #b00)) #b01\n"
            f"         (ite (and (= x_4_{r}_1 #b01) (= x_5_{r}_0 #b01)) #b01\n"
            f"         (ite (and (= x_4_{r}_1 #b01) (= x_5_{r}_0 #b10)) #b11\n"
            f"         (ite (and (= x_4_{r}_1 #b01) (= x_5_{r}_0 #b11)) #b11\n"
            f"         (ite (and (= x_4_{r}_1 #b10) (= x_5_{r}_0 #b00)) #b10\n"
            f"         (ite (and (= x_4_{r}_1 #b10) (= x_5_{r}_0 #b01)) #b11\n"
            f"         (ite (and (= x_4_{r}_1 #b10) (= x_5_{r}_0 #b10)) #b10\n"
            f"         (ite (and (= x_4_{r}_1 #b10) (= x_5_{r}_0 #b11)) #b11\n"
            f"         (ite (= x_4_{r}_1 #b11) #b11 #b00))))))))))))\n"
        )
        smtlib2_constr.append("\n")

        smtlib2_constr.append(f"(assert (= y_0_{r} z_0_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_1_{r} x_2_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_2_{r} z_1_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_3_{r} x_4_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_4_{r} z_2_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_5_{r} x_0_{r}_0))\n\n")

    smtlib2_constr.append(f"(assert (= (bvand x_0_{rounds-1}_0 (bvand x_2_{rounds-1}_0 x_4_{rounds-1}_0)) #b00))\n\n")

    smtlib2_constr.append(
        "(assert (not (= (concat x_0_0_0 (concat x_1_0_0 (concat x_2_0_0 (concat x_3_0_0 (concat x_4_0_0 x_5_0_0))))) #b000000000000)))\n"
    )
    
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
    target = "type2-d6-r1"
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