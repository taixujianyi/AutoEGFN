import os
import time

def set_smtlib2(rounds):
    smtlib2_constr = []
    smtlib2_constr.append("(set-logic QF_BV)\n\n")

    # Variable declarations
    for r in range(rounds):
        for i in range(6):
            smtlib2_constr.append(f"(declare-fun x_{i}_{r}_0 () (_ BitVec 2))\n")
        
        smtlib2_constr.append(f"(declare-fun z_3_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun z_4_{r}_0 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun z_5_{r}_0 () (_ BitVec 2))\n")
        
        smtlib2_constr.append(f"(declare-fun z_4_{r}_1 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun z_5_{r}_1 () (_ BitVec 2))\n")
        smtlib2_constr.append(f"(declare-fun z_5_{r}_2 () (_ BitVec 2))\n")
        
        for i in range(6):
            smtlib2_constr.append(f"(declare-fun y_{i}_{r}_0 () (_ BitVec 2))\n")
        
        for i in range(6):
            smtlib2_constr.append(f"(declare-fun y_{i}_{r}_1 () (_ BitVec 2))\n")
        
        for i in range(3):
            smtlib2_constr.append(f"(declare-fun y_{i}_{r}_2 () (_ BitVec 2))\n")
        
        smtlib2_constr.append("\n")

    for r in range(rounds):
        # Assign statements
        if r > 0:
            for i in range(6):
                smtlib2_constr.append(f"(assert (= y_{i}_{r}_0 x_{i}_{r-1}_0))\n")
        smtlib2_constr.append("\n")

        # Permutation
        smtlib2_constr.append(f"(assert (= y_0_{r}_1 y_3_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_1_{r}_1 y_4_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_2_{r}_1 y_5_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_3_{r}_1 y_0_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_4_{r}_1 y_1_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_5_{r}_1 y_2_{r}_0))\n")
        smtlib2_constr.append("\n")

        # XOR operations
        def create_xor_assertion(result_var, input1_var, input2_var, r):
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

        smtlib2_constr.append(create_xor_assertion(f"z_4_{r}_0", f"y_2_{r}_1", f"y_4_{r}_1", r))
        smtlib2_constr.append("\n")

        smtlib2_constr.append(create_xor_assertion(f"z_5_{r}_0", f"y_2_{r}_1", f"y_5_{r}_1", r))
        smtlib2_constr.append("\n")

        smtlib2_constr.append(create_xor_assertion(f"z_5_{r}_1", f"y_1_{r}_1", f"z_5_{r}_0", r))
        smtlib2_constr.append("\n")

        # F functions
        smtlib2_constr.append(f"(assert (= y_0_{r}_2 (ite (= y_0_{r}_1 #b00) #b00 #b11)))\n")
        smtlib2_constr.append(f"(assert (= y_1_{r}_2 (ite (= y_1_{r}_1 #b00) #b00 #b11)))\n")
        smtlib2_constr.append(f"(assert (= y_2_{r}_2 (ite (= y_2_{r}_1 #b00) #b00 #b11)))\n")
        smtlib2_constr.append("\n")

        smtlib2_constr.append(create_xor_assertion(f"z_5_{r}_2", f"y_0_{r}_2", f"z_5_{r}_1", r))
        smtlib2_constr.append("\n")

        smtlib2_constr.append(create_xor_assertion(f"z_4_{r}_1", f"y_1_{r}_2", f"z_4_{r}_0", r))
        smtlib2_constr.append("\n")

        smtlib2_constr.append(create_xor_assertion(f"z_3_{r}_0", f"y_2_{r}_2", f"y_3_{r}_1", r))
        smtlib2_constr.append("\n")

        # Permutation
        smtlib2_constr.append(f"(assert (= x_0_{r}_0 y_0_{r}_1))\n")
        smtlib2_constr.append(f"(assert (= x_1_{r}_0 y_1_{r}_1))\n")
        smtlib2_constr.append(f"(assert (= x_2_{r}_0 y_2_{r}_1))\n")
        smtlib2_constr.append(f"(assert (= x_3_{r}_0 z_3_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= x_4_{r}_0 z_4_{r}_1))\n")
        smtlib2_constr.append(f"(assert (= x_5_{r}_0 z_5_{r}_2))\n\n")

    # Active constraints
    for i in range(3):
        smtlib2_constr.append(f"(declare-fun active_{i+1} () (_ BitVec 1))\n")
    
    smtlib2_constr.append(f"(assert (= active_1 (ite (= y_0_{rounds-1}_1 #b00) #b0 #b1)))\n")
    smtlib2_constr.append(f"(assert (= active_2 (ite (= y_1_{rounds-1}_1 #b00) #b0 #b1)))\n")
    smtlib2_constr.append(f"(assert (= active_3 (ite (= y_2_{rounds-1}_1 #b00) #b0 #b1)))\n")
    
    and_expr = "(bvand active_1 (bvand active_2 active_3))"
    smtlib2_constr.append(f"(assert (= {and_expr} #b0))\n\n")



    y_bits = [f"y_{i}_0_0" for i in range(6)]
    
    concat_expr = y_bits[0]
    for bit in y_bits[1:]:
        concat_expr = f"(concat {concat_expr} {bit})"
    
    smtlib2_constr.append(f"(assert (not (= {concat_expr} #b{'0'*12})))\n")



    for i in range(6):
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
    target = "egfn-d6-r3"
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