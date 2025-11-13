import os
import time

def set_smtlib2(rounds):
    smtlib2_constr = []
    smtlib2_constr.append("(set-logic QF_BV)\n\n")

    # Variable declarations
    for r in range(rounds):
        for i in range(16):
            smtlib2_constr.append(f"(declare-fun x_{i}_{r}_0 () (_ BitVec 2))\n")
        
        for i in [1, 3, 5, 7, 9, 11, 13, 15]:
            smtlib2_constr.append(f"(declare-fun y_{i}_{r}_1 () (_ BitVec 2))\n")
        
        for i in range(8):
            smtlib2_constr.append(f"(declare-fun z_{i}_{r}_0 () (_ BitVec 2))\n")
        
        for i in range(16):
            smtlib2_constr.append(f"(declare-fun y_{i}_{r}_0 () (_ BitVec 2))\n")
        
        for i in range(16, 32):
            smtlib2_constr.append(f"(declare-fun x_{i}_{r}_0 () (_ BitVec 2))\n")
        
        for i in [17, 19, 21, 23, 25, 27, 29, 31]:
            smtlib2_constr.append(f"(declare-fun y_{i}_{r}_1 () (_ BitVec 2))\n")
        
        for i in range(8, 16):
            smtlib2_constr.append(f"(declare-fun z_{i}_{r}_0 () (_ BitVec 2))\n")
        
        for i in range(16, 32):
            smtlib2_constr.append(f"(declare-fun y_{i}_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append("\n")

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
        # Assign statements
        if r > 0:
            for i in range(32):
                smtlib2_constr.append(f"(assert (= y_{i}_{r}_0 x_{i}_{r-1}_0))\n")
        smtlib2_constr.append("\n")

        # Pass through F
        odd_indices_first = [1, 3, 5, 7, 9, 11, 13, 15]
        for i in odd_indices_first:
            smtlib2_constr.append(f"(assert (= y_{i}_{r}_1 (ite (= y_{i}_{r}_0 #b00) #b00 #b11)))\n")
        
        odd_indices_second = [17, 19, 21, 23, 25, 27, 29, 31]
        for i in odd_indices_second:
            smtlib2_constr.append(f"(assert (= y_{i}_{r}_1 (ite (= y_{i}_{r}_0 #b00) #b00 #b11)))\n")
        smtlib2_constr.append("\n")


        # XOR
        smtlib2_constr.append(f"(assert (= (Table (concat (concat y_31_{r}_1 y_0_{r}_0) z_0_{r}_0)) #b1))\n")
        for i in range(1, 8):
            y1_idx = 2*i - 1  # 1, 3, 5, 7, 9, 11, 13
            y2_idx = 2*i      # 2, 4, 6, 8, 10, 12, 14
            smtlib2_constr.append(f"(assert (= (Table (concat (concat y_{y1_idx}_{r}_1 y_{y2_idx}_{r}_0) z_{i}_{r}_0)) #b1))\n")
            smtlib2_constr.append("\n")

        smtlib2_constr.append(f"(assert (= (Table (concat (concat y_15_{r}_1 y_16_{r}_0) z_8_{r}_0)) #b1))\n")

        for i in range(9, 16):
            y1_idx = 2*i - 1  # 17, 19, 21, 23, 25, 27, 29
            y2_idx = 2*i      # 18, 20, 22, 24, 26, 28, 30
            smtlib2_constr.append(f"(assert (= (Table (concat (concat y_{y1_idx}_{r}_1 y_{y2_idx}_{r}_0) z_{i}_{r}_0)) #b1))\n")
            smtlib2_constr.append("\n")

        # Permutation
        smtlib2_constr.append(f"(assert (= x_0_{r}_0 y_31_{r}_0))\n")
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
        smtlib2_constr.append(f"(assert (= x_13_{r}_0 z_6_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= x_14_{r}_0 y_13_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= x_15_{r}_0 z_7_{r}_0))\n")

        smtlib2_constr.append(f"(assert (= x_16_{r}_0 y_15_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= x_17_{r}_0 z_8_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= x_18_{r}_0 y_17_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= x_19_{r}_0 z_9_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= x_20_{r}_0 y_19_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= x_21_{r}_0 z_10_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= x_22_{r}_0 y_21_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= x_23_{r}_0 z_11_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= x_24_{r}_0 y_23_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= x_25_{r}_0 z_12_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= x_26_{r}_0 y_25_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= x_27_{r}_0 z_13_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= x_28_{r}_0 y_27_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= x_29_{r}_0 z_14_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= x_30_{r}_0 y_29_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= x_31_{r}_0 z_15_{r}_0))\n\n")

    # Active constraints
    for i in range(16):
        smtlib2_constr.append(f"(declare-fun active_{i+1} () (_ BitVec 1))\n")
    
    # Active conditions
    active_y_indices = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]
    for i, idx in enumerate(active_y_indices):
        smtlib2_constr.append(f"(assert (= active_{i+1} (ite (= y_{idx}_{rounds-1}_0 #b00) #b0 #b1)))\n")
    
    # AND all active variables
    and_expr = "active_1"
    for i in range(2, 17):
        and_expr = f"(bvand {and_expr} active_{i})"
    smtlib2_constr.append(f"(assert (= {and_expr} #b0))\n\n")



    y_bits = [f"y_{i}_0_0" for i in range(32)]
    
    concat_expr = y_bits[0]
    for bit in y_bits[1:]:
        concat_expr = f"(concat {concat_expr} {bit})"
    
    smtlib2_constr.append(f"(assert (not (= {concat_expr} #b{'0'*64})))\n")



    for i in range(32):
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
    target = "type2-d32-r3"
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