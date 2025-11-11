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
        smtlib2_constr.append(f"(declare-fun x_6_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun x_7_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun x_8_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun x_9_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun x_10_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun x_11_{r}_0 () (_ BitVec 2))\n")
        
        smtlib2_constr.append(f"(declare-fun x_8_{r}_1 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun x_9_{r}_1 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun x_10_{r}_1 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun x_11_{r}_1 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun x_6_{r}_1 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun x_7_{r}_1 () (_ BitVec 2))\n")
        
        smtlib2_constr.append(f"(declare-fun z_0_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun z_1_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun z_2_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun z_3_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun z_4_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun z_5_{r}_0 () (_ BitVec 2))\n")
        
        smtlib2_constr.append(f"(declare-fun y_0_{r} () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_1_{r} () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_2_{r} () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_3_{r} () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_4_{r} () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_5_{r} () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_6_{r} () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_7_{r} () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_8_{r} () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_9_{r} () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_10_{r} () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_11_{r} () (_ BitVec 2))\n\n")

    for r in range(rounds):
        # Assign
        if r > 0:
            smtlib2_constr.append(f"(assert (= x_0_{r}_0 y_0_{r-1}))\n")
            smtlib2_constr.append(f"(assert (= x_1_{r}_0 y_1_{r-1}))\n")
            smtlib2_constr.append(f"(assert (= x_2_{r}_0 y_2_{r-1}))\n")
            smtlib2_constr.append(f"(assert (= x_3_{r}_0 y_3_{r-1}))\n")
            smtlib2_constr.append(f"(assert (= x_4_{r}_0 y_4_{r-1}))\n")
            smtlib2_constr.append(f"(assert (= x_5_{r}_0 y_5_{r-1}))\n")
            smtlib2_constr.append(f"(assert (= x_6_{r}_0 y_6_{r-1}))\n")
            smtlib2_constr.append(f"(assert (= x_7_{r}_0 y_7_{r-1}))\n")
            smtlib2_constr.append(f"(assert (= x_8_{r}_0 y_8_{r-1}))\n")
            smtlib2_constr.append(f"(assert (= x_9_{r}_0 y_9_{r-1}))\n")
            smtlib2_constr.append(f"(assert (= x_10_{r}_0 y_10_{r-1}))\n")
            smtlib2_constr.append(f"(assert (= x_11_{r}_0 y_11_{r-1}))\n")
        smtlib2_constr.append("\n")

        # F function
        smtlib2_constr.append(f"(assert (= x_8_{r}_1 (ite (= x_8_{r}_0 #b00) #b00 #b11)))\n")
        smtlib2_constr.append(f"(assert (= x_9_{r}_1 (ite (= x_9_{r}_0 #b00) #b00 #b11)))\n")
        smtlib2_constr.append(f"(assert (= x_10_{r}_1 (ite (= x_10_{r}_0 #b00) #b00 #b11)))\n")
        smtlib2_constr.append(f"(assert (= x_11_{r}_1 (ite (= x_11_{r}_0 #b00) #b00 #b11)))\n")
        smtlib2_constr.append(f"(assert (= x_6_{r}_1 (ite (= x_6_{r}_0 #b00) #b00 #b11)))\n")
        smtlib2_constr.append(f"(assert (= x_7_{r}_1 (ite (= x_7_{r}_0 #b00) #b00 #b11)))\n")
        smtlib2_constr.append("\n")

        # XOR operations
        # z_0
        smtlib2_constr.append(
            f"(assert (= z_0_{r}_0\n"
            f"    (ite (= x_6_{r}_1 #b00) x_5_{r}_0\n"
            f"         (ite (and (= x_6_{r}_1 #b01) (= x_5_{r}_0 #b00)) #b01\n"
            f"         (ite (and (= x_6_{r}_1 #b01) (= x_5_{r}_0 #b01)) #b01\n"
            f"         (ite (and (= x_6_{r}_1 #b01) (= x_5_{r}_0 #b10)) #b11\n"
            f"         (ite (and (= x_6_{r}_1 #b01) (= x_5_{r}_0 #b11)) #b11\n"
            f"         (ite (and (= x_6_{r}_1 #b10) (= x_5_{r}_0 #b00)) #b10\n"
            f"         (ite (and (= x_6_{r}_1 #b10) (= x_5_{r}_0 #b01)) #b11\n"
            f"         (ite (and (= x_6_{r}_1 #b10) (= x_5_{r}_0 #b10)) #b10\n"
            f"         (ite (and (= x_6_{r}_1 #b10) (= x_5_{r}_0 #b11)) #b11\n"
            f"         (ite (= x_6_{r}_1 #b11) #b11 #b00))))))))))))\n"
        )
        
        # z_1
        smtlib2_constr.append(
            f"(assert (= z_1_{r}_0\n"
            f"    (ite (= x_7_{r}_1 #b00) x_4_{r}_0\n"
            f"         (ite (and (= x_7_{r}_1 #b01) (= x_4_{r}_0 #b00)) #b01\n"
            f"         (ite (and (= x_7_{r}_1 #b01) (= x_4_{r}_0 #b01)) #b01\n"
            f"         (ite (and (= x_7_{r}_1 #b01) (= x_4_{r}_0 #b10)) #b11\n"
            f"         (ite (and (= x_7_{r}_1 #b01) (= x_4_{r}_0 #b11)) #b11\n"
            f"         (ite (and (= x_7_{r}_1 #b10) (= x_4_{r}_0 #b00)) #b10\n"
            f"         (ite (and (= x_7_{r}_1 #b10) (= x_4_{r}_0 #b01)) #b11\n"
            f"         (ite (and (= x_7_{r}_1 #b10) (= x_4_{r}_0 #b10)) #b10\n"
            f"         (ite (and (= x_7_{r}_1 #b10) (= x_4_{r}_0 #b11)) #b11\n"
            f"         (ite (= x_7_{r}_1 #b11) #b11 #b00))))))))))))\n"
        )
        
        # z_2
        smtlib2_constr.append(
            f"(assert (= z_2_{r}_0\n"
            f"    (ite (= x_8_{r}_1 #b00) x_3_{r}_0\n"
            f"         (ite (and (= x_8_{r}_1 #b01) (= x_3_{r}_0 #b00)) #b01\n"
            f"         (ite (and (= x_8_{r}_1 #b01) (= x_3_{r}_0 #b01)) #b01\n"
            f"         (ite (and (= x_8_{r}_1 #b01) (= x_3_{r}_0 #b10)) #b11\n"
            f"         (ite (and (= x_8_{r}_1 #b01) (= x_3_{r}_0 #b11)) #b11\n"
            f"         (ite (and (= x_8_{r}_1 #b10) (= x_3_{r}_0 #b00)) #b10\n"
            f"         (ite (and (= x_8_{r}_1 #b10) (= x_3_{r}_0 #b01)) #b11\n"
            f"         (ite (and (= x_8_{r}_1 #b10) (= x_3_{r}_0 #b10)) #b10\n"
            f"         (ite (and (= x_8_{r}_1 #b10) (= x_3_{r}_0 #b11)) #b11\n"
            f"         (ite (= x_8_{r}_1 #b11) #b11 #b00))))))))))))\n"
        )
        
        # z_3
        smtlib2_constr.append(
            f"(assert (= z_3_{r}_0\n"
            f"    (ite (= x_9_{r}_1 #b00) x_2_{r}_0\n"
            f"         (ite (and (= x_9_{r}_1 #b01) (= x_2_{r}_0 #b00)) #b01\n"
            f"         (ite (and (= x_9_{r}_1 #b01) (= x_2_{r}_0 #b01)) #b01\n"
            f"         (ite (and (= x_9_{r}_1 #b01) (= x_2_{r}_0 #b10)) #b11\n"
            f"         (ite (and (= x_9_{r}_1 #b01) (= x_2_{r}_0 #b11)) #b11\n"
            f"         (ite (and (= x_9_{r}_1 #b10) (= x_2_{r}_0 #b00)) #b10\n"
            f"         (ite (and (= x_9_{r}_1 #b10) (= x_2_{r}_0 #b01)) #b11\n"
            f"         (ite (and (= x_9_{r}_1 #b10) (= x_2_{r}_0 #b10)) #b10\n"
            f"         (ite (and (= x_9_{r}_1 #b10) (= x_2_{r}_0 #b11)) #b11\n"
            f"         (ite (= x_9_{r}_1 #b11) #b11 #b00))))))))))))\n"
        )
        
        # z_4
        smtlib2_constr.append(
            f"(assert (= z_4_{r}_0\n"
            f"    (ite (= x_10_{r}_1 #b00) x_1_{r}_0\n"
            f"         (ite (and (= x_10_{r}_1 #b01) (= x_1_{r}_0 #b00)) #b01\n"
            f"         (ite (and (= x_10_{r}_1 #b01) (= x_1_{r}_0 #b01)) #b01\n"
            f"         (ite (and (= x_10_{r}_1 #b01) (= x_1_{r}_0 #b10)) #b11\n"
            f"         (ite (and (= x_10_{r}_1 #b01) (= x_1_{r}_0 #b11)) #b11\n"
            f"         (ite (and (= x_10_{r}_1 #b10) (= x_1_{r}_0 #b00)) #b10\n"
            f"         (ite (and (= x_10_{r}_1 #b10) (= x_1_{r}_0 #b01)) #b11\n"
            f"         (ite (and (= x_10_{r}_1 #b10) (= x_1_{r}_0 #b10)) #b10\n"
            f"         (ite (and (= x_10_{r}_1 #b10) (= x_1_{r}_0 #b11)) #b11\n"
            f"         (ite (= x_10_{r}_1 #b11) #b11 #b00))))))))))))\n"
        )
        
        # z_5
        smtlib2_constr.append(
            f"(assert (= z_5_{r}_0\n"
            f"    (ite (= x_11_{r}_1 #b00) x_0_{r}_0\n"
            f"         (ite (and (= x_11_{r}_1 #b01) (= x_0_{r}_0 #b00)) #b01\n"
            f"         (ite (and (= x_11_{r}_1 #b01) (= x_0_{r}_0 #b01)) #b01\n"
            f"         (ite (and (= x_11_{r}_1 #b01) (= x_0_{r}_0 #b10)) #b11\n"
            f"         (ite (and (= x_11_{r}_1 #b01) (= x_0_{r}_0 #b11)) #b11\n"
            f"         (ite (and (= x_11_{r}_1 #b10) (= x_0_{r}_0 #b00)) #b10\n"
            f"         (ite (and (= x_11_{r}_1 #b10) (= x_0_{r}_0 #b01)) #b11\n"
            f"         (ite (and (= x_11_{r}_1 #b10) (= x_0_{r}_0 #b10)) #b10\n"
            f"         (ite (and (= x_11_{r}_1 #b10) (= x_0_{r}_0 #b11)) #b11\n"
            f"         (ite (= x_11_{r}_1 #b11) #b11 #b00))))))))))))\n"
        )
        smtlib2_constr.append("\n")

        # Permutation
        smtlib2_constr.append(f"(assert (= y_0_{r} x_11_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_1_{r} z_5_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_2_{r} z_4_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_3_{r} z_3_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_4_{r} z_2_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_5_{r} z_1_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_6_{r} z_0_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_7_{r} x_6_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_8_{r} x_7_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_9_{r} x_8_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_10_{r} x_9_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_11_{r} x_10_{r}_0))\n\n")

    smtlib2_constr.append(f"(assert (= (bvand x_8_{rounds-1}_0 (bvand x_9_{rounds-1}_0 (bvand x_10_{rounds-1}_0 (bvand x_11_{rounds-1}_0 (bvand x_6_{rounds-1}_0 x_7_{rounds-1}_0))))) #b00))\n\n")
    smtlib2_constr.append(
        "(assert (not (= (concat x_0_0_0 (concat x_1_0_0 (concat x_2_0_0 (concat x_3_0_0 (concat x_4_0_0 (concat x_5_0_0 (concat x_6_0_0 (concat x_7_0_0 (concat x_8_0_0 (concat x_9_0_0 (concat x_10_0_0 x_11_0_0))))))))))) #b000000000000000000000000)))\n"
    )
    
    for i in range(12):
        smtlib2_constr.append(f"(assert (not (= x_{i}_0_0 #b11)))\n")
    smtlib2_constr.append("\n")

    smtlib2_constr.append("(check-sat)\n")
    smtlib2_constr.append("(get-model)\n")
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
    target = "nyb-d12-r1"
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