import os
import time

def set_smtlib2(rounds):
    smtlib2_constr = []
    smtlib2_constr.append("(set-logic QF_BV)\n\n")

    pi =[3, 8, 5, 6, 7, 4, 1, 12, 11, 2, 9, 21, 15, 19, 13, 17, 10, 16, 14, 20, 0, 18]
    d = len(pi)
    k = d // 2

    for r in range(rounds):
        for i in range(d):
            smtlib2_constr.append(f"(declare-fun x_{i}_{r}_0 () (_ BitVec 2))\n")
            smtlib2_constr.append(f"(declare-fun y_{i}_{r} () (_ BitVec 2))\n")

        for i in range(1, d, 2):
            smtlib2_constr.append(f"(declare-fun x_{i}_{r}_1 () (_ BitVec 2))\n")
        
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
                smtlib2_constr.append(f"(assert (= x_{i}_{r}_0 y_{i}_{r-1}))\n")
        smtlib2_constr.append("\n")

        # F function
        for i in range(1, d, 2):
            smtlib2_constr.append(f"(assert (= x_{i}_{r}_1 (ite (= x_{i}_{r}_0 #b00) #b00 #b11)))\n")

        # XOR
        for i in range(0, d, 2):
            z_index = i // 2
            x1_index = i + 1
            smtlib2_constr.append(f"(assert (= (Table (concat (concat x_{i}_{r}_0 x_{x1_index}_{r}_1) z_{z_index}_{r}_0)) #b1))\n")
            smtlib2_constr.append("\n")

        # Permutation
        for i in range(d):
            z_index = i // 2
            if i%2 == 0:
                smtlib2_constr.append(f"(assert (= y_{pi[i]}_{r} z_{z_index}_{r}_0))\n")
            else:
                smtlib2_constr.append(f"(assert (= y_{pi[i]}_{r} x_{i}_{r}_0))\n")

    # Active constraints
    for i in range(k):
        smtlib2_constr.append(f"(declare-fun active_{i+1} () (_ BitVec 1))\n")
    
    active_indices = range(1, d, 2)
    for i, idx in enumerate(active_indices):
        smtlib2_constr.append(f"(assert (= active_{i+1} (ite (= x_{idx}_{rounds-1}_0 #b00) #b0 #b1)))\n")
    and_expr = "active_1"
    for i in range(2, k+1):
        and_expr = f"(bvand {and_expr} active_{i})"
    smtlib2_constr.append(f"(assert (= {and_expr} #b0))\n\n")



    x_bits = [f"x_{i}_0_0" for i in range(d)]
    concat_expr = x_bits[0]
    for bit in x_bits[1:]:
        concat_expr = f"(concat {concat_expr} {bit})"
    smtlib2_constr.append(f"(assert (not (= {concat_expr} #b{'0'*2*d})))\n")



    for i in range(d):
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
    target = "ddgp22-d22-r1"
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