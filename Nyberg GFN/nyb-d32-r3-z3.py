import os
import time

def set_smtlib2(rounds):
    smtlib2_constr = []
    smtlib2_constr.append("(set-logic QF_BV)\n\n")

    # Declare variables for all rounds
    for r in range(rounds):
        for i in range(32):
            smtlib2_constr.append(f"(declare-fun x_{i}_{r}_0 () (_ BitVec 2))\n")
        
        for i in range(32):
            smtlib2_constr.append(f"(declare-fun y_{i}_{r}_0 () (_ BitVec 2))\n")
            smtlib2_constr.append(f"(declare-fun y_{i}_{r}_1 () (_ BitVec 2))\n")
        
        for i in [16, 18, 20, 22, 24, 26, 28, 30]:
            smtlib2_constr.append(f"(declare-fun y_{i}_{r}_2 () (_ BitVec 2))\n")
        for i in [17, 19, 21, 23, 25, 27, 29, 31]:
            smtlib2_constr.append(f"(declare-fun y_{i}_{r}_2 () (_ BitVec 2))\n")
        
        for i in range(16):
            smtlib2_constr.append(f"(declare-fun z_{i}_{r}_0 () (_ BitVec 2))\n")
        
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
            for i in range(32):
                smtlib2_constr.append(f"(assert (= y_{i}_{r}_0 x_{i}_{r-1}_0))\n")
            smtlib2_constr.append("\n")

        # Permutation
        for i in range(31):
            smtlib2_constr.append(f"(assert (= y_{i}_{r}_1 y_{i+1}_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_31_{r}_1 y_0_{r}_0))\n")
        smtlib2_constr.append("\n")

        # F function
        even_indices = [16, 18, 20, 22, 24, 26, 28, 30]
        odd_indices = [17, 19, 21, 23, 25, 27, 29, 31]
        for i in even_indices + odd_indices:
            smtlib2_constr.append(f"(assert (= y_{i}_{r}_2 (ite (= y_{i}_{r}_1 #b00) #b00 #b11)))\n")
        smtlib2_constr.append("\n")


        # XOR
        xor_pairs = [
            (16, 15), (17, 14), (18, 13), (19, 12), (20, 11), (21, 10), 
            (22, 9), (23, 8), (24, 7), (25, 6), (26, 5), (27, 4), 
            (28, 3), (29, 2), (30, 1), (31, 0)
        ]
        for i, (y_idx, target_idx) in enumerate(xor_pairs):
            smtlib2_constr.append(f"(assert (= (Table (concat (concat y_{y_idx}_{r}_2 y_{target_idx}_{r}_1) z_{i}_{r}_0)) #b1))\n")
            smtlib2_constr.append("\n")

        # Permutation
        for i in range(16):
            smtlib2_constr.append(f"(assert (= x_{i}_{r}_0 z_{15-i}_{r}_0))\n")
        for i in range(16, 32):
            smtlib2_constr.append(f"(assert (= x_{i}_{r}_0 y_{i}_{r}_1))\n")
        
        smtlib2_constr.append("\n")

    # Active constraints
    and_terms = []
    for i in [17, 19, 21, 23, 25, 27, 29, 31, 16, 18, 20, 22, 24, 26, 28, 30]:
        and_terms.append(f"y_{i}_{rounds-1}_1")
    
    # Build nested bvand expression
    and_expr = and_terms[0]
    for term in and_terms[1:]:
        and_expr = f"(bvand {and_expr} {term})"
    
    smtlib2_constr.append(f"(assert (= {and_expr} #b00))\n\n")

    # Non-zero constraint for initial state
    concat_terms = []
    for i in range(32):
        concat_terms.append(f"y_{i}_0_0")
    
    # Build nested concat expression
    concat_expr = concat_terms[0]
    for term in concat_terms[1:]:
        concat_expr = f"(concat {concat_expr} {term})"
    
    smtlib2_constr.append(f"(assert (not (= {concat_expr} #b0000000000000000000000000000000000000000000000000000000000000000)))\n")

    # No 0b11 constraints for initial y values
    for i in range(32):
        smtlib2_constr.append(f"(assert (not (= y_{i}_0_0 #b11)))\n")
        smtlib2_constr.append(f"(assert (not (= y_{i}_0_0 #b10)))\n")
    smtlib2_constr.append("\n")

    smtlib2_constr.append("(check-sat)\n")
    # Remove get-model for faster solving: (get-model)

    return smtlib2_constr

def run_stp(target, rounds):
    smtlib2_code = set_smtlib2(rounds)
    filename = f"{target}-round{rounds}.smt2"
    with open(filename, "w") as f:
        f.writelines(smtlib2_code)

    command = f"z3 {filename}"
    output = os.popen(command)
    return output

def remove_file(target, rounds):
    for i in range(1, rounds + 1):
        filename = f"{target}-round{i}.smt2"
        if os.path.exists(filename):
            os.remove(filename)

if __name__ == '__main__':
    start = time.time()
    target = "nyb-d32-r3"
    rounds = 1
    print("round =", rounds)
    result = run_stp(target, rounds)
    result_str = result.read()
    #print("result =", result_str)

    while "unsat" not in result_str:
        rounds += 1
        print("round =", rounds)
        result = run_stp(target, rounds)
        result_str = result.read()
        #print("result =", result_str)
    else:
        print("max-r3 =", rounds - 1)
        print("result =", result_str)

    end = time.time()
    print("time: {:.2f} s".format(end - start))
    remove_file(target, rounds)