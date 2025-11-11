import os
import time

def set_smtlib2(rounds):
    smtlib2_constr = []
    smtlib2_constr.append("(set-logic QF_BV)\n\n")

    # Declare variables
    for r in range(rounds):
        for i in range(7):
            smtlib2_constr.append(f"(declare-fun x_{i}_{r}_0 () (_ BitVec 2))\n")
        
        smtlib2_constr.append(f"(declare-fun x_0_{r}_1 () (_ BitVec 2))\n")
        
        for i in range(6):
            smtlib2_constr.append(f"(declare-fun z_{i}_{r}_0 () (_ BitVec 2))\n")
        
        for i in range(7):
            smtlib2_constr.append(f"(declare-fun y_{i}_{r} () (_ BitVec 2))\n")
        
        smtlib2_constr.append("\n")

    for r in range(rounds):
        if r > 0:
            for i in range(7):
                smtlib2_constr.append(f"(assert (= x_{i}_{r}_0 y_{i}_{r-1}))\n")
        smtlib2_constr.append("\n")

        # F function
        smtlib2_constr.append(f"(assert (= x_0_{r}_1 (ite (= x_0_{r}_0 #b00) #b00 #b11)))\n")
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

        smtlib2_constr.append(create_xor_assertion(f"z_0_{r}_0", f"x_0_{r}_1", f"x_1_{r}_0", r))
        smtlib2_constr.append("\n")

        smtlib2_constr.append(create_xor_assertion(f"z_1_{r}_0", f"x_0_{r}_1", f"x_2_{r}_0", r))
        smtlib2_constr.append("\n")

        smtlib2_constr.append(create_xor_assertion(f"z_2_{r}_0", f"x_0_{r}_1", f"x_3_{r}_0", r))
        smtlib2_constr.append("\n")

        smtlib2_constr.append(create_xor_assertion(f"z_3_{r}_0", f"x_0_{r}_1", f"x_4_{r}_0", r))
        smtlib2_constr.append("\n")

        smtlib2_constr.append(create_xor_assertion(f"z_4_{r}_0", f"x_0_{r}_1", f"x_5_{r}_0", r))
        smtlib2_constr.append("\n")

        smtlib2_constr.append(create_xor_assertion(f"z_5_{r}_0", f"x_0_{r}_1", f"x_6_{r}_0", r))
        smtlib2_constr.append("\n")

        # Permutation (1 2 3 4 5 6 0)
        smtlib2_constr.append(f"(assert (= y_0_{r} z_5_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_1_{r} x_0_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_2_{r} z_0_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_3_{r} z_1_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_4_{r} z_2_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_5_{r} z_3_{r}_0))\n")
        smtlib2_constr.append(f"(assert (= y_6_{r} z_4_{r}_0))\n\n")

    # Active constraints
    smtlib2_constr.append("(declare-fun active_1 () (_ BitVec 1))\n")
    smtlib2_constr.append(f"(assert (= active_1 (ite (= x_0_{rounds-1}_0 #b00) #b0 #b1)))\n")
    smtlib2_constr.append("(assert (= active_1 #b0))\n\n")

    concat_expr = "(concat x_0_0_0 (concat x_1_0_0 (concat x_2_0_0 (concat x_3_0_0 (concat x_4_0_0 (concat x_5_0_0 x_6_0_0))))))"
    smtlib2_constr.append(f"(assert (not (= {concat_expr} #b00000000000000)))\n")
    for i in range(7):
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
    target = "TH-d7-r1"
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