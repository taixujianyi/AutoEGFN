import os
import time

def set_smtlib2(rounds):
    smtlib2_constr = []
    smtlib2_constr.append("(set-logic QF_BV)\n\n")

    # Declare variables
    for r in range(rounds):
        for i in range(16):
            smtlib2_constr.append(f"(declare-fun x_{i}_{r}_0 () (_ BitVec 2))\n")
        
        for i in range(8, 16):
            smtlib2_constr.append(f"(declare-fun z_{i}_{r}_0 () (_ BitVec 2))\n")
        
        for i in range(9, 16):
            smtlib2_constr.append(f"(declare-fun z_{i}_{r}_1 () (_ BitVec 2))\n")
        
        for i in range(15, 16):
            for j in range(2, 8):
                smtlib2_constr.append(f"(declare-fun z_{i}_{r}_{j} () (_ BitVec 2))\n")
        
        for i in range(16):
            smtlib2_constr.append(f"(declare-fun y_{i}_{r}_0 () (_ BitVec 2))\n")
            smtlib2_constr.append(f"(declare-fun y_{i}_{r}_1 () (_ BitVec 2))\n")
        
        for i in range(8):
            smtlib2_constr.append(f"(declare-fun y_{i}_{r}_2 () (_ BitVec 2))\n")
        
        smtlib2_constr.append("\n")

    for r in range(rounds):
        if r > 0:
            for i in range(16):
                smtlib2_constr.append(f"(assert (= y_{i}_{r}_0 x_{i}_{r-1}_0))\n")
        smtlib2_constr.append("\n")

        # Permutation
        smtlib2_constr.append(f"(assert (= y_0_{r}_1 y_8_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_1_{r}_1 y_9_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_2_{r}_1 y_10_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_3_{r}_1 y_11_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_4_{r}_1 y_12_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_5_{r}_1 y_13_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_6_{r}_1 y_14_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_7_{r}_1 y_15_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_8_{r}_1 y_0_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_9_{r}_1 y_1_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_10_{r}_1 y_2_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_11_{r}_1 y_3_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_12_{r}_1 y_4_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_13_{r}_1 y_5_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_14_{r}_1 y_6_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_15_{r}_1 y_7_{r}_0))\n")
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

        for i in range(9, 16):
            smtlib2_constr.append(create_xor_assertion(f"z_{i}_{r}_0", f"y_7_{r}_1", f"y_{i}_{r}_1"))
            smtlib2_constr.append("\n")

        for i, control_idx in enumerate(range(6, -1, -1)):
            if i == 0:
                smtlib2_constr.append(create_xor_assertion(f"z_15_{r}_1", f"y_{control_idx}_{r}_1", f"z_15_{r}_0"))
            else:
                smtlib2_constr.append(create_xor_assertion(f"z_15_{r}_{i+1}", f"y_{control_idx}_{r}_1", f"z_15_{r}_{i}"))
            smtlib2_constr.append("\n")

        # F function
        for i in range(8):
            smtlib2_constr.append(f"(assert (= y_{i}_{r}_2 (ite (= y_{i}_{r}_1 #b00) #b00 #b11)))\n")
        smtlib2_constr.append("\n")

        smtlib2_constr.append(create_xor_assertion(f"z_15_{r}_7", f"y_0_{r}_2", f"z_15_{r}_6"))
        smtlib2_constr.append("\n")
        
        smtlib2_constr.append(create_xor_assertion(f"z_14_{r}_1", f"y_1_{r}_2", f"z_14_{r}_0"))
        smtlib2_constr.append("\n")
        
        smtlib2_constr.append(create_xor_assertion(f"z_13_{r}_1", f"y_2_{r}_2", f"z_13_{r}_0"))
        smtlib2_constr.append("\n")
        
        smtlib2_constr.append(create_xor_assertion(f"z_12_{r}_1", f"y_3_{r}_2", f"z_12_{r}_0"))
        smtlib2_constr.append("\n")
        
        smtlib2_constr.append(create_xor_assertion(f"z_11_{r}_1", f"y_4_{r}_2", f"z_11_{r}_0"))
        smtlib2_constr.append("\n")
        
        smtlib2_constr.append(create_xor_assertion(f"z_10_{r}_1", f"y_5_{r}_2", f"z_10_{r}_0"))
        smtlib2_constr.append("\n")
        
        smtlib2_constr.append(create_xor_assertion(f"z_9_{r}_1", f"y_6_{r}_2", f"z_9_{r}_0"))
        smtlib2_constr.append("\n")
        
        smtlib2_constr.append(create_xor_assertion(f"z_8_{r}_0", f"y_7_{r}_2", f"y_8_{r}_1"))
        smtlib2_constr.append("\n")

        for i in range(8):
            smtlib2_constr.append(f"(assert (= x_{i}_{r}_0 y_{i}_{r}_1))\n")
        
        smtlib2_constr.append(f"(assert (= x_8_{r}_0 z_8_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= x_9_{r}_0 z_9_{r}_1))\n")
        smtlib2_constr.append(f"(assert (= x_10_{r}_0 z_10_{r}_1))\n")
        smtlib2_constr.append(f"(assert (= x_11_{r}_0 z_11_{r}_1))\n")
        smtlib2_constr.append(f"(assert (= x_12_{r}_0 z_12_{r}_1))\n")
        smtlib2_constr.append(f"(assert (= x_13_{r}_0 z_13_{r}_1))\n")
        smtlib2_constr.append(f"(assert (= x_14_{r}_0 z_14_{r}_1))\n")
        smtlib2_constr.append(f"(assert (= x_15_{r}_0 z_15_{r}_7))\n")
        smtlib2_constr.append("\n")

    # Active constraints
    active_vars = []
    for i in range(8):
        active_vars.append(f"active_{i+1}")
        smtlib2_constr.append(f"(declare-fun active_{i+1} () (_ BitVec 1))\n")
    
    indices = [1, 2, 3, 4, 5, 6, 7, 0]
    for i, idx in enumerate(indices):
        smtlib2_constr.append(f"(assert (= active_{i+1} (ite (= y_{idx}_{rounds-1}_1 #b00) #b0 #b1)))\n")
    
    and_expr = active_vars[0]
    for var in active_vars[1:]:
        and_expr = f"(bvand {and_expr} {var})"
    smtlib2_constr.append(f"(assert (= {and_expr} #b0))\n\n")

    concat_terms = [f"y_{i}_0_0" for i in range(16)]
    concat_expr = concat_terms[0]
    for term in concat_terms[1:]:
        concat_expr = f"(concat {concat_expr} {term})"
    smtlib2_constr.append(f"(assert (not (= {concat_expr} #b00000000000000000000000000000000)))\n")
    
    for i in range(16):
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
    target = "egfn-d16-r3"
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