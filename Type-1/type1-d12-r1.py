import os
import time

def set_smtlib2_stp(rounds):
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
        smtlib2_constr.append(f"(declare-fun x_0_{r}_1 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun z_0_{r}_0 () (_ BitVec 2))\n")
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
        smtlib2_constr.append(f"(assert (= x_0_{r}_1 (ite (= x_0_{r}_0 #b00) #b00 #b11)))\n")
        smtlib2_constr.append("\n")


        # XOR
        smtlib2_constr.append(f"(assert (= (Table (concat (concat x_0_{r}_1 x_1_{r}_0) z_0_{r}_0)) #b1))\n")


        # Perm
        smtlib2_constr.append(f"(assert (= y_0_{r} z_0_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_1_{r} x_2_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_2_{r} x_3_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_3_{r} x_4_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_4_{r} x_5_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_5_{r} x_6_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_6_{r} x_7_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_7_{r} x_8_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_8_{r} x_9_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_9_{r} x_10_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_10_{r} x_11_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_11_{r} x_0_{r}_0))\n\n")

    smtlib2_constr.append(f"(assert (= x_0_{rounds-1}_0 #b00))\n")
    smtlib2_constr.append("\n")

    smtlib2_constr.append(
        "(assert (not (= (concat (concat (concat (concat (concat (concat x_0_0_0 x_1_0_0) (concat x_2_0_0 x_3_0_0)) (concat x_4_0_0 x_5_0_0)) (concat x_6_0_0 x_7_0_0)) (concat x_8_0_0 x_9_0_0)) (concat x_10_0_0 x_11_0_0)) #b000000000000000000000000)))\n"
    )
    for i in range(12):
        smtlib2_constr.append(f"(assert (not (= x_{i}_0_0 #b11)))\n")
        smtlib2_constr.append(f"(assert (not (= x_{i}_0_0 #b10)))\n")
    smtlib2_constr.append("\n")

    smtlib2_constr.append("(check-sat)\n(get-model)\n")
    return smtlib2_constr

def run_stp(target, rounds):
    smtlib2_code = set_smtlib2_stp(rounds)
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
    target = "type1-d12-r1"
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