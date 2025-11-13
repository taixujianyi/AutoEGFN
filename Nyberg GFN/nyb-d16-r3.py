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
        smtlib2_constr.append(f"(declare-fun x_12_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun x_13_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun x_14_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun x_15_{r}_0 () (_ BitVec 2))\n")
        
        smtlib2_constr.append(f"(declare-fun z_0_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun z_1_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun z_2_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun z_3_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun z_4_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun z_5_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun z_6_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun z_7_{r}_0 () (_ BitVec 2))\n")
        
        smtlib2_constr.append(f"(declare-fun y_0_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_1_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_2_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_3_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_4_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_5_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_6_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_7_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_8_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_9_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_10_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_11_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_12_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_13_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_14_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_15_{r}_0 () (_ BitVec 2))\n")
        
        smtlib2_constr.append(f"(declare-fun y_0_{r}_1 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_1_{r}_1 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_2_{r}_1 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_3_{r}_1 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_4_{r}_1 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_5_{r}_1 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_6_{r}_1 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_7_{r}_1 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_8_{r}_1 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_9_{r}_1 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_10_{r}_1 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_11_{r}_1 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_12_{r}_1 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_13_{r}_1 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_14_{r}_1 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_15_{r}_1 () (_ BitVec 2))\n")
        
        smtlib2_constr.append(f"(declare-fun y_8_{r}_2 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_9_{r}_2 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_10_{r}_2 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_11_{r}_2 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_12_{r}_2 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_13_{r}_2 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_14_{r}_2 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_15_{r}_2 () (_ BitVec 2))\n\n")

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
        # Assign
        if r > 0:
            smtlib2_constr.append(f"(assert (= y_0_{r}_0 x_0_{r-1}_0))\n")
            smtlib2_constr.append(f"(assert (= y_1_{r}_0 x_1_{r-1}_0))\n")
            smtlib2_constr.append(f"(assert (= y_2_{r}_0 x_2_{r-1}_0))\n")
            smtlib2_constr.append(f"(assert (= y_3_{r}_0 x_3_{r-1}_0))\n")
            smtlib2_constr.append(f"(assert (= y_4_{r}_0 x_4_{r-1}_0))\n")
            smtlib2_constr.append(f"(assert (= y_5_{r}_0 x_5_{r-1}_0))\n")
            smtlib2_constr.append(f"(assert (= y_6_{r}_0 x_6_{r-1}_0))\n")
            smtlib2_constr.append(f"(assert (= y_7_{r}_0 x_7_{r-1}_0))\n")
            smtlib2_constr.append(f"(assert (= y_8_{r}_0 x_8_{r-1}_0))\n")
            smtlib2_constr.append(f"(assert (= y_9_{r}_0 x_9_{r-1}_0))\n")
            smtlib2_constr.append(f"(assert (= y_10_{r}_0 x_10_{r-1}_0))\n")
            smtlib2_constr.append(f"(assert (= y_11_{r}_0 x_11_{r-1}_0))\n")
            smtlib2_constr.append(f"(assert (= y_12_{r}_0 x_12_{r-1}_0))\n")
            smtlib2_constr.append(f"(assert (= y_13_{r}_0 x_13_{r-1}_0))\n")
            smtlib2_constr.append(f"(assert (= y_14_{r}_0 x_14_{r-1}_0))\n")
            smtlib2_constr.append(f"(assert (= y_15_{r}_0 x_15_{r-1}_0))\n")
        smtlib2_constr.append("\n")

        # Permutation
        smtlib2_constr.append(f"(assert (= y_0_{r}_1 y_1_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_1_{r}_1 y_2_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_2_{r}_1 y_3_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_3_{r}_1 y_4_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_4_{r}_1 y_5_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_5_{r}_1 y_6_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_6_{r}_1 y_7_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_7_{r}_1 y_8_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_8_{r}_1 y_9_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_9_{r}_1 y_10_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_10_{r}_1 y_11_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_11_{r}_1 y_12_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_12_{r}_1 y_13_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_13_{r}_1 y_14_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_14_{r}_1 y_15_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_15_{r}_1 y_0_{r}_0))\n")
        smtlib2_constr.append("\n")

        # F function
        smtlib2_constr.append(f"(assert (= y_8_{r}_2 (ite (= y_8_{r}_1 #b00) #b00 #b11)))\n")
        smtlib2_constr.append(f"(assert (= y_9_{r}_2 (ite (= y_9_{r}_1 #b00) #b00 #b11)))\n")
        smtlib2_constr.append(f"(assert (= y_10_{r}_2 (ite (= y_10_{r}_1 #b00) #b00 #b11)))\n")
        smtlib2_constr.append(f"(assert (= y_11_{r}_2 (ite (= y_11_{r}_1 #b00) #b00 #b11)))\n")
        smtlib2_constr.append(f"(assert (= y_12_{r}_2 (ite (= y_12_{r}_1 #b00) #b00 #b11)))\n")
        smtlib2_constr.append(f"(assert (= y_13_{r}_2 (ite (= y_13_{r}_1 #b00) #b00 #b11)))\n")
        smtlib2_constr.append(f"(assert (= y_14_{r}_2 (ite (= y_14_{r}_1 #b00) #b00 #b11)))\n")
        smtlib2_constr.append(f"(assert (= y_15_{r}_2 (ite (= y_15_{r}_1 #b00) #b00 #b11)))\n")
        smtlib2_constr.append("\n")


        # XOR
        smtlib2_constr.append(f"(assert (= (Table (concat (concat y_15_{r}_2 y_0_{r}_1) z_0_{r}_0)) #b1))\n")
        smtlib2_constr.append(f"(assert (= (Table (concat (concat y_14_{r}_2 y_1_{r}_1) z_1_{r}_0)) #b1))\n")
        smtlib2_constr.append(f"(assert (= (Table (concat (concat y_13_{r}_2 y_2_{r}_1) z_2_{r}_0)) #b1))\n")
        smtlib2_constr.append(f"(assert (= (Table (concat (concat y_12_{r}_2 y_3_{r}_1) z_3_{r}_0)) #b1))\n")
        
        smtlib2_constr.append(f"(assert (= (Table (concat (concat y_11_{r}_2 y_4_{r}_1) z_4_{r}_0)) #b1))\n")
        smtlib2_constr.append(f"(assert (= (Table (concat (concat y_10_{r}_2 y_5_{r}_1) z_5_{r}_0)) #b1))\n")
        smtlib2_constr.append(f"(assert (= (Table (concat (concat y_9_{r}_2 y_6_{r}_1) z_6_{r}_0)) #b1))\n")
        smtlib2_constr.append(f"(assert (= (Table (concat (concat y_8_{r}_2 y_7_{r}_1) z_7_{r}_0)) #b1))\n")


        # Permutation
        smtlib2_constr.append(f"(assert (= x_0_{r}_0 z_0_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= x_1_{r}_0 z_1_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= x_2_{r}_0 z_2_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= x_3_{r}_0 z_3_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= x_4_{r}_0 z_4_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= x_5_{r}_0 z_5_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= x_6_{r}_0 z_6_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= x_7_{r}_0 z_7_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= x_8_{r}_0 y_8_{r}_1))\n")
        smtlib2_constr.append(f"(assert (= x_9_{r}_0 y_9_{r}_1))\n")
        smtlib2_constr.append(f"(assert (= x_10_{r}_0 y_10_{r}_1))\n")
        smtlib2_constr.append(f"(assert (= x_11_{r}_0 y_11_{r}_1))\n")
        smtlib2_constr.append(f"(assert (= x_12_{r}_0 y_12_{r}_1))\n")
        smtlib2_constr.append(f"(assert (= x_13_{r}_0 y_13_{r}_1))\n")
        smtlib2_constr.append(f"(assert (= x_14_{r}_0 y_14_{r}_1))\n")
        smtlib2_constr.append(f"(assert (= x_15_{r}_0 y_15_{r}_1))\n\n")

    smtlib2_constr.append(f"(assert (= (bvand y_8_{rounds-1}_1 (bvand y_9_{rounds-1}_1 (bvand y_10_{rounds-1}_1 (bvand y_11_{rounds-1}_1 (bvand y_12_{rounds-1}_1 (bvand y_13_{rounds-1}_1 (bvand y_14_{rounds-1}_1 y_15_{rounds-1}_1))))))) #b00))\n\n")
    smtlib2_constr.append(
        "(assert (not (= (concat y_0_0_0 (concat y_1_0_0 (concat y_2_0_0 (concat y_3_0_0 (concat y_4_0_0 (concat y_5_0_0 (concat y_6_0_0 (concat y_7_0_0 (concat y_8_0_0 (concat y_9_0_0 (concat y_10_0_0 (concat y_11_0_0 (concat y_12_0_0 (concat y_13_0_0 (concat y_14_0_0 y_15_0_0))))))))))))))) #b00000000000000000000000000000000)))\n"
    )
    
    for i in range(16):
        smtlib2_constr.append(f"(assert (not (= y_{i}_0_0 #b11)))\n")
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
    target = "nyb-d16-r3"
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