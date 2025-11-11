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
        smtlib2_constr.append(f"(declare-fun x_8_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun x_9_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun x_10_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun x_11_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun x_12_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun x_13_{r}_0 () (_ BitVec 2))\n")
        
        smtlib2_constr.append(f"(declare-fun y_1_{r}_1 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_3_{r}_1 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_5_{r}_1 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_7_{r}_1 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_9_{r}_1 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_11_{r}_1 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun y_13_{r}_1 () (_ BitVec 2))\n")
        
        smtlib2_constr.append(f"(declare-fun z_0_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun z_1_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun z_2_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun z_3_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun z_4_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun z_5_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun z_6_{r}_0 () (_ BitVec 2))\n")
        
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
        smtlib2_constr.append(f"(declare-fun y_13_{r}_0 () (_ BitVec 2))\n\n")

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
        smtlib2_constr.append("\n")

        # Pass through F
        smtlib2_constr.append(f"(assert (= y_1_{r}_1 (ite (= y_1_{r}_0 #b00) #b00 #b11)))\n")
        smtlib2_constr.append(f"(assert (= y_3_{r}_1 (ite (= y_3_{r}_0 #b00) #b00 #b11)))\n")
        smtlib2_constr.append(f"(assert (= y_5_{r}_1 (ite (= y_5_{r}_0 #b00) #b00 #b11)))\n")
        smtlib2_constr.append(f"(assert (= y_7_{r}_1 (ite (= y_7_{r}_0 #b00) #b00 #b11)))\n")
        smtlib2_constr.append(f"(assert (= y_9_{r}_1 (ite (= y_9_{r}_0 #b00) #b00 #b11)))\n")
        smtlib2_constr.append(f"(assert (= y_11_{r}_1 (ite (= y_11_{r}_0 #b00) #b00 #b11)))\n")
        smtlib2_constr.append(f"(assert (= y_13_{r}_1 (ite (= y_13_{r}_0 #b00) #b00 #b11)))\n")
        smtlib2_constr.append("\n")

        # XOR operations
        smtlib2_constr.append(
            f"(assert (= z_0_{r}_0\n"
            f"    (ite (= y_13_{r}_1 #b00) y_0_{r}_0\n"
            f"         (ite (and (= y_13_{r}_1 #b01) (= y_0_{r}_0 #b00)) #b01\n"
            f"         (ite (and (= y_13_{r}_1 #b01) (= y_0_{r}_0 #b01)) #b01\n"
            f"         (ite (and (= y_13_{r}_1 #b01) (= y_0_{r}_0 #b10)) #b11\n"
            f"         (ite (and (= y_13_{r}_1 #b01) (= y_0_{r}_0 #b11)) #b11\n"
            f"         (ite (and (= y_13_{r}_1 #b10) (= y_0_{r}_0 #b00)) #b10\n"
            f"         (ite (and (= y_13_{r}_1 #b10) (= y_0_{r}_0 #b01)) #b11\n"
            f"         (ite (and (= y_13_{r}_1 #b10) (= y_0_{r}_0 #b10)) #b10\n"
            f"         (ite (and (= y_13_{r}_1 #b10) (= y_0_{r}_0 #b11)) #b11\n"
            f"         (ite (= y_13_{r}_1 #b11) #b11 #b00))))))))))))\n"
        )
        smtlib2_constr.append("\n")

        smtlib2_constr.append(
            f"(assert (= z_1_{r}_0\n"
            f"    (ite (= y_1_{r}_1 #b00) y_2_{r}_0\n"
            f"         (ite (and (= y_1_{r}_1 #b01) (= y_2_{r}_0 #b00)) #b01\n"
            f"         (ite (and (= y_1_{r}_1 #b01) (= y_2_{r}_0 #b01)) #b01\n"
            f"         (ite (and (= y_1_{r}_1 #b01) (= y_2_{r}_0 #b10)) #b11\n"
            f"         (ite (and (= y_1_{r}_1 #b01) (= y_2_{r}_0 #b11)) #b11\n"
            f"         (ite (and (= y_1_{r}_1 #b10) (= y_2_{r}_0 #b00)) #b10\n"
            f"         (ite (and (= y_1_{r}_1 #b10) (= y_2_{r}_0 #b01)) #b11\n"
            f"         (ite (and (= y_1_{r}_1 #b10) (= y_2_{r}_0 #b10)) #b10\n"
            f"         (ite (and (= y_1_{r}_1 #b10) (= y_2_{r}_0 #b11)) #b11\n"
            f"         (ite (= y_1_{r}_1 #b11) #b11 #b00))))))))))))\n"
        )
        smtlib2_constr.append("\n")

        smtlib2_constr.append(
            f"(assert (= z_2_{r}_0\n"
            f"    (ite (= y_3_{r}_1 #b00) y_4_{r}_0\n"
            f"         (ite (and (= y_3_{r}_1 #b01) (= y_4_{r}_0 #b00)) #b01\n"
            f"         (ite (and (= y_3_{r}_1 #b01) (= y_4_{r}_0 #b01)) #b01\n"
            f"         (ite (and (= y_3_{r}_1 #b01) (= y_4_{r}_0 #b10)) #b11\n"
            f"         (ite (and (= y_3_{r}_1 #b01) (= y_4_{r}_0 #b11)) #b11\n"
            f"         (ite (and (= y_3_{r}_1 #b10) (= y_4_{r}_0 #b00)) #b10\n"
            f"         (ite (and (= y_3_{r}_1 #b10) (= y_4_{r}_0 #b01)) #b11\n"
            f"         (ite (and (= y_3_{r}_1 #b10) (= y_4_{r}_0 #b10)) #b10\n"
            f"         (ite (and (= y_3_{r}_1 #b10) (= y_4_{r}_0 #b11)) #b11\n"
            f"         (ite (= y_3_{r}_1 #b11) #b11 #b00))))))))))))\n"
        )
        smtlib2_constr.append("\n")

        smtlib2_constr.append(
            f"(assert (= z_3_{r}_0\n"
            f"    (ite (= y_5_{r}_1 #b00) y_6_{r}_0\n"
            f"         (ite (and (= y_5_{r}_1 #b01) (= y_6_{r}_0 #b00)) #b01\n"
            f"         (ite (and (= y_5_{r}_1 #b01) (= y_6_{r}_0 #b01)) #b01\n"
            f"         (ite (and (= y_5_{r}_1 #b01) (= y_6_{r}_0 #b10)) #b11\n"
            f"         (ite (and (= y_5_{r}_1 #b01) (= y_6_{r}_0 #b11)) #b11\n"
            f"         (ite (and (= y_5_{r}_1 #b10) (= y_6_{r}_0 #b00)) #b10\n"
            f"         (ite (and (= y_5_{r}_1 #b10) (= y_6_{r}_0 #b01)) #b11\n"
            f"         (ite (and (= y_5_{r}_1 #b10) (= y_6_{r}_0 #b10)) #b10\n"
            f"         (ite (and (= y_5_{r}_1 #b10) (= y_6_{r}_0 #b11)) #b11\n"
            f"         (ite (= y_5_{r}_1 #b11) #b11 #b00))))))))))))\n"
        )
        smtlib2_constr.append("\n")

        smtlib2_constr.append(
            f"(assert (= z_4_{r}_0\n"
            f"    (ite (= y_7_{r}_1 #b00) y_8_{r}_0\n"
            f"         (ite (and (= y_7_{r}_1 #b01) (= y_8_{r}_0 #b00)) #b01\n"
            f"         (ite (and (= y_7_{r}_1 #b01) (= y_8_{r}_0 #b01)) #b01\n"
            f"         (ite (and (= y_7_{r}_1 #b01) (= y_8_{r}_0 #b10)) #b11\n"
            f"         (ite (and (= y_7_{r}_1 #b01) (= y_8_{r}_0 #b11)) #b11\n"
            f"         (ite (and (= y_7_{r}_1 #b10) (= y_8_{r}_0 #b00)) #b10\n"
            f"         (ite (and (= y_7_{r}_1 #b10) (= y_8_{r}_0 #b01)) #b11\n"
            f"         (ite (and (= y_7_{r}_1 #b10) (= y_8_{r}_0 #b10)) #b10\n"
            f"         (ite (and (= y_7_{r}_1 #b10) (= y_8_{r}_0 #b11)) #b11\n"
            f"         (ite (= y_7_{r}_1 #b11) #b11 #b00))))))))))))\n"
        )
        smtlib2_constr.append("\n")

        smtlib2_constr.append(
            f"(assert (= z_5_{r}_0\n"
            f"    (ite (= y_9_{r}_1 #b00) y_10_{r}_0\n"
            f"         (ite (and (= y_9_{r}_1 #b01) (= y_10_{r}_0 #b00)) #b01\n"
            f"         (ite (and (= y_9_{r}_1 #b01) (= y_10_{r}_0 #b01)) #b01\n"
            f"         (ite (and (= y_9_{r}_1 #b01) (= y_10_{r}_0 #b10)) #b11\n"
            f"         (ite (and (= y_9_{r}_1 #b01) (= y_10_{r}_0 #b11)) #b11\n"
            f"         (ite (and (= y_9_{r}_1 #b10) (= y_10_{r}_0 #b00)) #b10\n"
            f"         (ite (and (= y_9_{r}_1 #b10) (= y_10_{r}_0 #b01)) #b11\n"
            f"         (ite (and (= y_9_{r}_1 #b10) (= y_10_{r}_0 #b10)) #b10\n"
            f"         (ite (and (= y_9_{r}_1 #b10) (= y_10_{r}_0 #b11)) #b11\n"
            f"         (ite (= y_9_{r}_1 #b11) #b11 #b00))))))))))))\n"
        )
        smtlib2_constr.append("\n")

        smtlib2_constr.append(
            f"(assert (= z_6_{r}_0\n"
            f"    (ite (= y_11_{r}_1 #b00) y_12_{r}_0\n"
            f"         (ite (and (= y_11_{r}_1 #b01) (= y_12_{r}_0 #b00)) #b01\n"
            f"         (ite (and (= y_11_{r}_1 #b01) (= y_12_{r}_0 #b01)) #b01\n"
            f"         (ite (and (= y_11_{r}_1 #b01) (= y_12_{r}_0 #b10)) #b11\n"
            f"         (ite (and (= y_11_{r}_1 #b01) (= y_12_{r}_0 #b11)) #b11\n"
            f"         (ite (and (= y_11_{r}_1 #b10) (= y_12_{r}_0 #b00)) #b10\n"
            f"         (ite (and (= y_11_{r}_1 #b10) (= y_12_{r}_0 #b01)) #b11\n"
            f"         (ite (and (= y_11_{r}_1 #b10) (= y_12_{r}_0 #b10)) #b10\n"
            f"         (ite (and (= y_11_{r}_1 #b10) (= y_12_{r}_0 #b11)) #b11\n"
            f"         (ite (= y_11_{r}_1 #b11) #b11 #b00))))))))))))\n"
        )
        smtlib2_constr.append("\n")

        # Permutation
        smtlib2_constr.append(f"(assert (= x_0_{r}_0 y_13_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= x_1_{r}_0 z_0_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= x_2_{r}_0 y_1_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= x_3_{r}_0 z_1_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= x_4_{r}_0 y_3_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= x_5_{r}_0 z_2_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= x_6_{r}_0 y_5_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= x_7_{r}_0 z_3_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= x_8_{r}_0 y_7_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= x_9_{r}_0 z_4_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= x_10_{r}_0 y_9_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= x_11_{r}_0 z_5_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= x_12_{r}_0 y_11_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= x_13_{r}_0 z_6_{r}_0))\n\n")

    # Active constraints
    smtlib2_constr.append("(declare-fun active_1 () (_ BitVec 1))\n")
    smtlib2_constr.append("(declare-fun active_2 () (_ BitVec 1))\n")
    smtlib2_constr.append("(declare-fun active_3 () (_ BitVec 1))\n")
    smtlib2_constr.append("(declare-fun active_4 () (_ BitVec 1))\n")
    smtlib2_constr.append("(declare-fun active_5 () (_ BitVec 1))\n")
    smtlib2_constr.append("(declare-fun active_6 () (_ BitVec 1))\n")
    smtlib2_constr.append("(declare-fun active_7 () (_ BitVec 1))\n")
    
    smtlib2_constr.append(f"(assert (= active_1 (ite (= y_1_{rounds-1}_0 #b00) #b0 #b1)))\n")
    smtlib2_constr.append(f"(assert (= active_2 (ite (= y_3_{rounds-1}_0 #b00) #b0 #b1)))\n")
    smtlib2_constr.append(f"(assert (= active_3 (ite (= y_5_{rounds-1}_0 #b00) #b0 #b1)))\n")
    smtlib2_constr.append(f"(assert (= active_4 (ite (= y_7_{rounds-1}_0 #b00) #b0 #b1)))\n")
    smtlib2_constr.append(f"(assert (= active_5 (ite (= y_9_{rounds-1}_0 #b00) #b0 #b1)))\n")
    smtlib2_constr.append(f"(assert (= active_6 (ite (= y_11_{rounds-1}_0 #b00) #b0 #b1)))\n")
    smtlib2_constr.append(f"(assert (= active_7 (ite (= y_13_{rounds-1}_0 #b00) #b0 #b1)))\n")
    
    smtlib2_constr.append("(assert (= (bvand active_1 (bvand active_2 (bvand active_3 (bvand active_4 (bvand active_5 (bvand active_6 active_7)))))) #b0))\n\n")

    # Input constraints
    y_bits = []
    for i in range(14):
        y_bits.append(f"y_{i}_0_0")

    concat_expr = y_bits[0]
    for bit in y_bits[1:]:
        concat_expr = f"(concat {concat_expr} {bit})"

    smtlib2_constr.append(f"(assert (not (= {concat_expr} #b0000000000000000000000000000)))\n")

    for i in range(14):
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
    target = "type2-d14-r3"
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