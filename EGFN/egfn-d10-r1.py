import os
import time

def set_smtlib2(rounds):
    smtlib2_constr = []
    smtlib2_constr.append("(set-logic QF_BV)\n\n")

    # Declare variables
    for r in range(rounds):
        for i in range(10):
            smtlib2_constr.append(f"(declare-fun x_{i}_{r}_0 () (_ BitVec 2))\n")
        
        for i in range(5):
            smtlib2_constr.append(f"(declare-fun x_{i}_{r}_1 () (_ BitVec 2))\n")
        
        for i in range(5, 10):
            smtlib2_constr.append(f"(declare-fun z_{i}_{r}_0 () (_ BitVec 2))\n")
        
        for i in range(4):
            smtlib2_constr.append(f"(declare-fun z_9_{r}_{i+1} () (_ BitVec 2))\n")
        
        for i in range(6, 9):
            smtlib2_constr.append(f"(declare-fun z_{i}_{r}_1 () (_ BitVec 2))\n")
        
        for i in range(10):
            smtlib2_constr.append(f"(declare-fun y_{i}_{r} () (_ BitVec 2))\n")
        
        smtlib2_constr.append("\n")

    for r in range(rounds):
        if r > 0:
            for i in range(10):
                smtlib2_constr.append(f"(assert (= x_{i}_{r}_0 y_{i}_{r-1}))\n")
        smtlib2_constr.append("\n")

        # F function
        for i in range(5):
            smtlib2_constr.append(f"(assert (= x_{i}_{r}_1 (ite (= x_{i}_{r}_0 #b00) #b00 #b11)))\n")
        smtlib2_constr.append("\n")

        # XOR operation
        def create_xor_assertion(result_var, input1_var, input2_var):
            return (
                f"(assert (= {result_var}\n"
                f"    (ite (= {input1_var} #b00) {input2_var}\n"
                f"         (ite (and (= {input1_var} #b01) (= {input2_var} #b00)) #b01\n"
                f"         (ite (and (= {input1_var} #b01) (= {input2_var} #b01)) #b01\n"
                f"         (ite (and (= {input1_var} #b01) (= {input2_var} #b10)) #b11\n"
                f"         (ite (and (= {input1_var} #b01) (= {input2_var} #b11)) #b11\n"
                f"         (ite (and (= {input1_var} #b10) (= {input2_var} #b00)) #b10\n"
                f"         (ite (and (= {input1_var} #b10) (= {input2_var} #b01)) #b11\n"
                f"         (ite (and (= {input1_var} #b10) (= {input2_var} #b10)) #b10\n"
                f"         (ite (and (= {input1_var} #b10) (= {input2_var} #b11)) #b11\n"
                f"         (ite (= {input1_var} #b11) #b11 #b00))))))))))))\n"
            )

        smtlib2_constr.append(create_xor_assertion(f"z_5_{r}_0", f"x_4_{r}_1", f"x_5_{r}_0"))
        smtlib2_constr.append("\n")

        smtlib2_constr.append(create_xor_assertion(f"z_6_{r}_0", f"x_3_{r}_1", f"x_6_{r}_0"))
        smtlib2_constr.append("\n")

        smtlib2_constr.append(create_xor_assertion(f"z_7_{r}_0", f"x_2_{r}_1", f"x_7_{r}_0"))
        smtlib2_constr.append("\n")

        smtlib2_constr.append(create_xor_assertion(f"z_8_{r}_0", f"x_1_{r}_1", f"x_8_{r}_0"))
        smtlib2_constr.append("\n")

        smtlib2_constr.append(create_xor_assertion(f"z_9_{r}_0", f"x_0_{r}_1", f"x_9_{r}_0"))
        smtlib2_constr.append("\n")

        smtlib2_constr.append(create_xor_assertion(f"z_9_{r}_1", f"x_1_{r}_0", f"z_9_{r}_0"))
        smtlib2_constr.append("\n")

        smtlib2_constr.append(create_xor_assertion(f"z_9_{r}_2", f"x_2_{r}_0", f"z_9_{r}_1"))
        smtlib2_constr.append("\n")

        smtlib2_constr.append(create_xor_assertion(f"z_9_{r}_3", f"x_3_{r}_0", f"z_9_{r}_2"))
        smtlib2_constr.append("\n")

        smtlib2_constr.append(create_xor_assertion(f"z_9_{r}_4", f"x_4_{r}_0", f"z_9_{r}_3"))
        smtlib2_constr.append("\n")

        smtlib2_constr.append(create_xor_assertion(f"z_8_{r}_1", f"x_4_{r}_0", f"z_8_{r}_0"))
        smtlib2_constr.append("\n")

        smtlib2_constr.append(create_xor_assertion(f"z_7_{r}_1", f"x_4_{r}_0", f"z_7_{r}_0"))
        smtlib2_constr.append("\n")

        smtlib2_constr.append(create_xor_assertion(f"z_6_{r}_1", f"x_4_{r}_0", f"z_6_{r}_0"))
        smtlib2_constr.append("\n")

        # Permutation
        smtlib2_constr.append(f"(assert (= y_0_{r} z_5_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_1_{r} z_6_{r}_1))\n")
        smtlib2_constr.append(f"(assert (= y_2_{r} z_7_{r}_1))\n")
        smtlib2_constr.append(f"(assert (= y_3_{r} z_8_{r}_1))\n")
        smtlib2_constr.append(f"(assert (= y_4_{r} z_9_{r}_4))\n")
        smtlib2_constr.append(f"(assert (= y_5_{r} x_0_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_6_{r} x_1_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_7_{r} x_2_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_8_{r} x_3_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_9_{r} x_4_{r}_0))\n\n")

    # Active constraints
    for i in range(1, 6):
        smtlib2_constr.append(f"(declare-fun active_{i} () (_ BitVec 1))\n")
    
    smtlib2_constr.append(f"(assert (= active_1 (ite (= x_0_{rounds-1}_0 #b00) #b0 #b1)))\n")
    smtlib2_constr.append(f"(assert (= active_2 (ite (= x_1_{rounds-1}_0 #b00) #b0 #b1)))\n")
    smtlib2_constr.append(f"(assert (= active_3 (ite (= x_2_{rounds-1}_0 #b00) #b0 #b1)))\n")
    smtlib2_constr.append(f"(assert (= active_4 (ite (= x_3_{rounds-1}_0 #b00) #b0 #b1)))\n")
    smtlib2_constr.append(f"(assert (= active_5 (ite (= x_4_{rounds-1}_0 #b00) #b0 #b1)))\n")
    
    and_expr = "(bvand active_1 (bvand active_2 (bvand active_3 (bvand active_4 active_5))))"
    smtlib2_constr.append(f"(assert (= {and_expr} #b0))\n\n")

    concat_terms = [f"x_{i}_0_0" for i in range(10)]
    concat_expr = concat_terms[0]
    for term in concat_terms[1:]:
        concat_expr = f"(concat {concat_expr} {term})"
    smtlib2_constr.append(f"(assert (not (= {concat_expr} #b00000000000000000000)))\n")
    
    for i in range(10):
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
    target = "egfn-d10-r1"
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