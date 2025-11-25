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
        smtlib2_constr.append(f"(declare-fun x_6_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun x_7_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_7_{r}_1 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_1_{r}_1 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_3_{r}_1 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_5_{r}_1 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun z_0_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun z_1_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun z_2_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun z_3_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_0_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_1_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_2_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_3_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_4_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_5_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_6_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_7_{r}_0 () (_ BitVec 2))\n\n")

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
        if r > 0:
            smtlib2_constr.append(f"(assert (= y_0_{r}_0 x_0_{r-1}_0))\n")
            smtlib2_constr.append(f"(assert (= y_1_{r}_0 x_1_{r-1}_0))\n")
            smtlib2_constr.append(f"(assert (= y_2_{r}_0 x_2_{r-1}_0))\n")
            smtlib2_constr.append(f"(assert (= y_3_{r}_0 x_3_{r-1}_0))\n")
            smtlib2_constr.append(f"(assert (= y_4_{r}_0 x_4_{r-1}_0))\n")
            smtlib2_constr.append(f"(assert (= y_5_{r}_0 x_5_{r-1}_0))\n")
            smtlib2_constr.append(f"(assert (= y_6_{r}_0 x_6_{r-1}_0))\n")
            smtlib2_constr.append(f"(assert (= y_7_{r}_0 x_7_{r-1}_0))\n")
        smtlib2_constr.append("\n")

        smtlib2_constr.append(f"(assert (= y_7_{r}_1 (ite (= y_7_{r}_0 #b00) #b00 #b11)))\n")
        smtlib2_constr.append(f"(assert (= y_1_{r}_1 (ite (= y_1_{r}_0 #b00) #b00 #b11)))\n")
        smtlib2_constr.append(f"(assert (= y_3_{r}_1 (ite (= y_3_{r}_0 #b00) #b00 #b11)))\n")
        smtlib2_constr.append(f"(assert (= y_5_{r}_1 (ite (= y_5_{r}_0 #b00) #b00 #b11)))\n")
        smtlib2_constr.append("\n")

        # XOR
        smtlib2_constr.append(f"(assert (= (Table (concat (concat y_7_{r}_1 y_0_{r}_0) z_0_{r}_0)) #b1))\n")
        smtlib2_constr.append(f"(assert (= (Table (concat (concat y_1_{r}_1 y_2_{r}_0) z_1_{r}_0)) #b1))\n")
        smtlib2_constr.append(f"(assert (= (Table (concat (concat y_3_{r}_1 y_4_{r}_0) z_2_{r}_0)) #b1))\n")
        smtlib2_constr.append(f"(assert (= (Table (concat (concat y_5_{r}_1 y_6_{r}_0) z_3_{r}_0)) #b1))\n")


        smtlib2_constr.append(f"(assert (= x_0_{r}_0 y_7_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= x_1_{r}_0 z_0_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= x_2_{r}_0 y_1_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= x_3_{r}_0 z_1_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= x_4_{r}_0 y_3_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= x_5_{r}_0 z_2_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= x_6_{r}_0 y_5_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= x_7_{r}_0 z_3_{r}_0))\n\n")

    smtlib2_constr.append("(declare-fun active_1 () (_ BitVec 1))\n")
    smtlib2_constr.append("(declare-fun active_2 () (_ BitVec 1))\n")
    smtlib2_constr.append("(declare-fun active_3 () (_ BitVec 1))\n")
    smtlib2_constr.append("(declare-fun active_4 () (_ BitVec 1))\n")
    smtlib2_constr.append(f"(assert (= active_1 (ite (= y_1_{rounds-1}_0 #b00) #b0 #b1)))\n")
    smtlib2_constr.append(f"(assert (= active_2 (ite (= y_3_{rounds-1}_0 #b00) #b0 #b1)))\n")
    smtlib2_constr.append(f"(assert (= active_3 (ite (= y_5_{rounds-1}_0 #b00) #b0 #b1)))\n")
    smtlib2_constr.append(f"(assert (= active_4 (ite (= y_7_{rounds-1}_0 #b00) #b0 #b1)))\n")
    smtlib2_constr.append("(assert (= (bvand active_1 (bvand active_2 (bvand active_3 active_4))) #b0))\n\n")

    smtlib2_constr.append(
        "(assert (not (= (concat y_0_0_0 (concat y_1_0_0 (concat y_2_0_0 (concat y_3_0_0 (concat y_4_0_0 (concat y_5_0_0 (concat y_6_0_0 y_7_0_0))))))) #b0000000000000000)))\n"
    )
    
    for i in range(8):
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
    target = "type2-d8-r3"
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