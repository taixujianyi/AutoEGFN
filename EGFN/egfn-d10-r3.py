import os
import time

def set_smtlib2(rounds):
    smtlib2_constr = []
    smtlib2_constr.append("(set-logic QF_BV)\n\n")

    # Declare variables
    for r in range(rounds):
        for i in range(10):
            smtlib2_constr.append(f"(declare-fun x_{i}_{r}_0 () (_ BitVec 2))\n")
        
        for i in range(5, 10):
            smtlib2_constr.append(f"(declare-fun z_{i}_{r}_0 () (_ BitVec 2))\n")
        
        for i in range(6, 10):
            smtlib2_constr.append(f"(declare-fun z_{i}_{r}_1 () (_ BitVec 2))\n")
        
        for i in range(2, 5):
            smtlib2_constr.append(f"(declare-fun z_9_{r}_{i} () (_ BitVec 2))\n")
        
        for i in range(10):
            smtlib2_constr.append(f"(declare-fun y_{i}_{r}_0 () (_ BitVec 2))\n")
            smtlib2_constr.append(f"(declare-fun y_{i}_{r}_1 () (_ BitVec 2))\n")
        
        for i in range(5):
            smtlib2_constr.append(f"(declare-fun y_{i}_{r}_2 () (_ BitVec 2))\n")
        
        smtlib2_constr.append("\n")

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
            for i in range(10):
                smtlib2_constr.append(f"(assert (= y_{i}_{r}_0 x_{i}_{r-1}_0))\n")
        smtlib2_constr.append("\n")

        # Permutation
        smtlib2_constr.append(f"(assert (= y_0_{r}_1 y_5_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_1_{r}_1 y_6_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_2_{r}_1 y_7_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_3_{r}_1 y_8_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_4_{r}_1 y_9_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_5_{r}_1 y_0_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_6_{r}_1 y_1_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_7_{r}_1 y_2_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_8_{r}_1 y_3_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_9_{r}_1 y_4_{r}_0))\n\n")

        # XOR
        smtlib2_constr.append(f"(assert (= (Table (concat (concat y_4_{r}_1 y_6_{r}_1) z_6_{r}_0)) #b1))\n")
        smtlib2_constr.append(f"(assert (= (Table (concat (concat y_4_{r}_1 y_7_{r}_1) z_7_{r}_0)) #b1))\n")
        smtlib2_constr.append(f"(assert (= (Table (concat (concat y_4_{r}_1 y_8_{r}_1) z_8_{r}_0)) #b1))\n")
        smtlib2_constr.append(f"(assert (= (Table (concat (concat y_4_{r}_1 y_9_{r}_1) z_9_{r}_0)) #b1))\n")
        smtlib2_constr.append(f"(assert (= (Table (concat (concat y_3_{r}_1 z_9_{r}_0) z_9_{r}_1)) #b1))\n")
        smtlib2_constr.append(f"(assert (= (Table (concat (concat y_2_{r}_1 z_9_{r}_1) z_9_{r}_2)) #b1))\n")
        smtlib2_constr.append(f"(assert (= (Table (concat (concat y_1_{r}_1 z_9_{r}_2) z_9_{r}_3)) #b1))\n")

        for i in range(5):
            smtlib2_constr.append(f"(assert (= y_{i}_{r}_2 (ite (= y_{i}_{r}_1 #b00) #b00 #b11)))\n")
        smtlib2_constr.append("\n")

        # XOR
        smtlib2_constr.append(f"(assert (= (Table (concat (concat y_0_{r}_2 z_9_{r}_3) z_9_{r}_4)) #b1))\n")
        smtlib2_constr.append(f"(assert (= (Table (concat (concat y_1_{r}_2 z_8_{r}_0) z_8_{r}_1)) #b1))\n")
        smtlib2_constr.append(f"(assert (= (Table (concat (concat y_2_{r}_2 z_7_{r}_0) z_7_{r}_1)) #b1))\n")
        smtlib2_constr.append(f"(assert (= (Table (concat (concat y_3_{r}_2 z_6_{r}_0) z_6_{r}_1)) #b1))\n")
        smtlib2_constr.append(f"(assert (= (Table (concat (concat y_4_{r}_2 y_5_{r}_1) z_5_{r}_0)) #b1))\n")

        #Permutation
        for i in range(5):
            smtlib2_constr.append(f"(assert (= x_{i}_{r}_0 y_{i}_{r}_1))\n")
        smtlib2_constr.append(f"(assert (= x_5_{r}_0 z_5_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= x_6_{r}_0 z_6_{r}_1))\n")
        smtlib2_constr.append(f"(assert (= x_7_{r}_0 z_7_{r}_1))\n")
        smtlib2_constr.append(f"(assert (= x_8_{r}_0 z_8_{r}_1))\n")
        smtlib2_constr.append(f"(assert (= x_9_{r}_0 z_9_{r}_4))\n\n")

    # Active constraints
    for i in range(1, 6):
        smtlib2_constr.append(f"(declare-fun active_{i} () (_ BitVec 1))\n")
    
    smtlib2_constr.append(f"(assert (= active_1 (ite (= y_1_{rounds-1}_1 #b00) #b0 #b1)))\n")
    smtlib2_constr.append(f"(assert (= active_2 (ite (= y_2_{rounds-1}_1 #b00) #b0 #b1)))\n")
    smtlib2_constr.append(f"(assert (= active_3 (ite (= y_3_{rounds-1}_1 #b00) #b0 #b1)))\n")
    smtlib2_constr.append(f"(assert (= active_4 (ite (= y_4_{rounds-1}_1 #b00) #b0 #b1)))\n")
    smtlib2_constr.append(f"(assert (= active_5 (ite (= y_0_{rounds-1}_1 #b00) #b0 #b1)))\n")
    
    and_expr = "(bvand active_1 (bvand active_2 (bvand active_3 (bvand active_4 active_5))))"
    smtlib2_constr.append(f"(assert (= {and_expr} #b0))\n\n")

    concat_terms = [f"y_{i}_0_0" for i in range(10)]
    concat_expr = concat_terms[0]
    for term in concat_terms[1:]:
        concat_expr = f"(concat {concat_expr} {term})"
    smtlib2_constr.append(f"(assert (not (= {concat_expr} #b00000000000000000000)))\n")
    
    for i in range(10):
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
    target = "egfn-d10-r3"
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