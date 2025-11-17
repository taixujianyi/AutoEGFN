import os
import time

def set_smtlib2(rounds):
    smtlib2_constr = []
    smtlib2_constr.append("(set-logic QF_BV)\n\n")
    
    pi_p = [1, 2, 3, 4, 5, 0, 7, 8, 9, 10, 11, 6, 12, 13]
    pi_q = [10, 7, 13, 11, 9, 8, 4, 1, 12, 5, 3, 2, 6, 0]
    k = len(pi_p)
    def p(k):
        return 2*pi_p[k] + 1
    def q(k):
        return 2*pi_q[k]
    d = 2*k
    pi =[]
    for i in range(k):
        pi.append(p(i))
        pi.append(q(i))
    #print("pi =", pi)

    # Variable declarations
    for r in range(rounds):
        for i in range(d):
            smtlib2_constr.append(f"(declare-fun x_{i}_{r}_0 () (_ BitVec 2))\n")
            smtlib2_constr.append(f"(declare-fun y_{i}_{r}_0 () (_ BitVec 2))\n")
            smtlib2_constr.append(f"(declare-fun y_{i}_{r}_1 () (_ BitVec 2))\n")
        
        for i in range(1, d, 2):
            smtlib2_constr.append(f"(declare-fun y_{i}_{r}_2 () (_ BitVec 2))\n")
        
        for i in range(k):
            smtlib2_constr.append(f"(declare-fun z_{i}_{r}_0 () (_ BitVec 2))\n")


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
            for i in range(d):
                smtlib2_constr.append(f"(assert (= y_{i}_{r}_0 x_{i}_{r-1}_0))\n")
        smtlib2_constr.append("\n")

        # Permutation
        for i in range(d):
            smtlib2_constr.append(f"(assert (= y_{i}_{r}_1 y_{pi[i]}_{r}_0))\n")

        # F function
        odd_indices_first = range(1, d, 2)
        for i in odd_indices_first:
            smtlib2_constr.append(f"(assert (= y_{i}_{r}_2 (ite (= y_{i}_{r}_1 #b00) #b00 #b11)))\n")
        

        # XOR
        for i in range(0, d, 2):
            z_index = i // 2
            smtlib2_constr.append(f"(assert (= (Table (concat (concat y_{i}_{r}_1 y_{i+1}_{r}_2) z_{z_index}_{r}_0)) #b1))\n")
            smtlib2_constr.append("\n")


        # Permutation
        for i in range(d):
            z_index = i // 2
            if i%2 == 0:
                smtlib2_constr.append(f"(assert (= x_{i}_{r}_0 z_{z_index}_{r}_0))\n")
            else:
                smtlib2_constr.append(f"(assert (= x_{i}_{r}_0 y_{i}_{r}_1))\n")


    # Active constraints
    for i in range(k):
        smtlib2_constr.append(f"(declare-fun active_{i+1} () (_ BitVec 1))\n")
    active_y_indices = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27]
    for i, idx in enumerate(active_y_indices):
        smtlib2_constr.append(f"(assert (= active_{i+1} (ite (= y_{idx}_{rounds-1}_1 #b00) #b0 #b1)))\n")    
    and_expr = "active_1"
    for i in range(2, k+1):
        and_expr = f"(bvand {and_expr} active_{i})"
    smtlib2_constr.append(f"(assert (= {and_expr} #b0))\n\n")


    y_bits = [f"y_{i}_0_0" for i in range(d)]
    concat_expr = y_bits[0]
    for bit in y_bits[1:]:
        concat_expr = f"(concat {concat_expr} {bit})"
    
    smtlib2_constr.append(f"(assert (not (= {concat_expr} #b{'0'*2*d})))\n")


    for i in range(d):
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
    target = "dflm19-d28-r3"
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