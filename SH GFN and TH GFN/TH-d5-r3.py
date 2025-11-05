import os

def set_cvc(round):
    cvc_constr = []
    for r in range(round):
        cvc_constr.append("\nx_0_{0}_0, x_1_{0}_0, x_2_{0}_0, x_3_{0}_0, x_4_{0}_0 : BITVECTOR(2);\n".format(r))
        cvc_constr.append("z_0_{0}_0, z_1_{0}_0, z_2_{0}_0, z_3_{0}_0 : BITVECTOR(2);\n".format(r))
        cvc_constr.append("y_0_{0}_0, y_1_{0}_0, y_2_{0}_0, y_3_{0}_0, y_4_{0}_0 : BITVECTOR(2);\n\n".format(r))
        cvc_constr.append("y_0_{0}_1, y_1_{0}_1, y_2_{0}_1, y_3_{0}_1, y_4_{0}_1 : BITVECTOR(2);\n\n".format(r))
        cvc_constr.append("y_0_{0}_2 : BITVECTOR(2);\n".format(r))

    for r in range(round):
        #Assign
        if r > 0:
            cvc_constr.append("ASSERT y_0_{0}_0 = x_0_{1}_0;\n".format(r, r-1))
            cvc_constr.append("ASSERT y_1_{0}_0 = x_1_{1}_0;\n".format(r, r-1))
            cvc_constr.append("ASSERT y_2_{0}_0 = x_2_{1}_0;\n".format(r, r-1))
            cvc_constr.append("ASSERT y_3_{0}_0 = x_3_{1}_0;\n".format(r, r-1))
            cvc_constr.append("ASSERT y_4_{0}_0 = x_4_{1}_0;\n".format(r, r-1))
        cvc_constr.append("\n")

        #Perm {1 2 3 4 0}
        cvc_constr.append("ASSERT y_0_{0}_1 = y_1_{0}_0;\n".format(r))
        cvc_constr.append("ASSERT y_1_{0}_1 = y_2_{0}_0;\n".format(r))
        cvc_constr.append("ASSERT y_2_{0}_1 = y_3_{0}_0;\n".format(r))
        cvc_constr.append("ASSERT y_3_{0}_1 = y_4_{0}_0;\n".format(r))
        cvc_constr.append("ASSERT y_4_{0}_1 = y_0_{0}_0;\n".format(r))

        #pass thorough F
        cvc_constr.append("ASSERT IF y_0_{0}_1=0bin00 THEN y_0_{0}_2=0bin00 ELSE y_0_{0}_2=0bin11 ENDIF;\n".format(r))
        cvc_constr.append("\n")

        #XOR
        cvc_constr.append("ASSERT IF y_0_{0}_2=0bin00 THEN z_0_{0}_0=y_1_{0}_1 ELSE 0bin1 = 0bin1 ENDIF;\n".format(r))
        cvc_constr.append("ASSERT IF y_0_{0}_2=0bin01 AND y_1_{0}_1=0bin00 THEN z_0_{0}_0=0bin01 ELSE 0bin1 = 0bin1 ENDIF;\n".format(r))
        cvc_constr.append("ASSERT IF y_0_{0}_2=0bin01 AND y_1_{0}_1=0bin01 THEN z_0_{0}_0=0bin00 ELSE 0bin1 = 0bin1 ENDIF;\n".format(r))
        cvc_constr.append("ASSERT IF y_0_{0}_2=0bin01 AND y_1_{0}_1=0bin10 THEN z_0_{0}_0=0bin11 ELSE 0bin1 = 0bin1 ENDIF;\n".format(r))
        cvc_constr.append("ASSERT IF y_0_{0}_2=0bin01 AND y_1_{0}_1=0bin11 THEN z_0_{0}_0=0bin11 ELSE 0bin1 = 0bin1 ENDIF;\n".format(r))
        cvc_constr.append("ASSERT IF y_0_{0}_2=0bin10 AND y_1_{0}_1=0bin00 THEN z_0_{0}_0=0bin10 ELSE 0bin1 = 0bin1 ENDIF;\n".format(r))
        cvc_constr.append("ASSERT IF y_0_{0}_2=0bin10 AND y_1_{0}_1=0bin01 THEN z_0_{0}_0=0bin11 ELSE 0bin1 = 0bin1 ENDIF;\n".format(r))
        cvc_constr.append("ASSERT IF y_0_{0}_2=0bin10 AND y_1_{0}_1=0bin10 THEN z_0_{0}_0=0bin00 ELSE 0bin1 = 0bin1 ENDIF;\n".format(r))
        cvc_constr.append("ASSERT IF y_0_{0}_2=0bin10 AND y_1_{0}_1=0bin11 THEN z_0_{0}_0=0bin11 ELSE 0bin1 = 0bin1 ENDIF;\n".format(r))
        cvc_constr.append("ASSERT IF y_0_{0}_2=0bin11 THEN z_0_{0}_0=0bin11 ELSE 0bin1 = 0bin1 ENDIF;\n".format(r))
        cvc_constr.append("\n")

        cvc_constr.append("ASSERT IF y_0_{0}_2=0bin00 THEN z_1_{0}_0=y_2_{0}_1 ELSE 0bin1 = 0bin1 ENDIF;\n".format(r))
        cvc_constr.append("ASSERT IF y_0_{0}_2=0bin01 AND y_2_{0}_1=0bin00 THEN z_1_{0}_0=0bin01 ELSE 0bin1 = 0bin1 ENDIF;\n".format(r))
        cvc_constr.append("ASSERT IF y_0_{0}_2=0bin01 AND y_2_{0}_1=0bin01 THEN z_1_{0}_0=0bin00 ELSE 0bin1 = 0bin1 ENDIF;\n".format(r))
        cvc_constr.append("ASSERT IF y_0_{0}_2=0bin01 AND y_2_{0}_1=0bin10 THEN z_1_{0}_0=0bin11 ELSE 0bin1 = 0bin1 ENDIF;\n".format(r))
        cvc_constr.append("ASSERT IF y_0_{0}_2=0bin01 AND y_2_{0}_1=0bin11 THEN z_1_{0}_0=0bin11 ELSE 0bin1 = 0bin1 ENDIF;\n".format(r))
        cvc_constr.append("ASSERT IF y_0_{0}_2=0bin10 AND y_2_{0}_1=0bin00 THEN z_1_{0}_0=0bin10 ELSE 0bin1 = 0bin1 ENDIF;\n".format(r))
        cvc_constr.append("ASSERT IF y_0_{0}_2=0bin10 AND y_2_{0}_1=0bin01 THEN z_1_{0}_0=0bin11 ELSE 0bin1 = 0bin1 ENDIF;\n".format(r))
        cvc_constr.append("ASSERT IF y_0_{0}_2=0bin10 AND y_2_{0}_1=0bin10 THEN z_1_{0}_0=0bin00 ELSE 0bin1 = 0bin1 ENDIF;\n".format(r))
        cvc_constr.append("ASSERT IF y_0_{0}_2=0bin10 AND y_2_{0}_1=0bin11 THEN z_1_{0}_0=0bin11 ELSE 0bin1 = 0bin1 ENDIF;\n".format(r))
        cvc_constr.append("ASSERT IF y_0_{0}_2=0bin11 THEN z_1_{0}_0=0bin11 ELSE 0bin1 = 0bin1 ENDIF;\n".format(r))
        cvc_constr.append("\n")

        cvc_constr.append("ASSERT IF y_0_{0}_2=0bin00 THEN z_2_{0}_0=y_3_{0}_1 ELSE 0bin1 = 0bin1 ENDIF;\n".format(r))
        cvc_constr.append("ASSERT IF y_0_{0}_2=0bin01 AND y_3_{0}_1=0bin00 THEN z_2_{0}_0=0bin01 ELSE 0bin1 = 0bin1 ENDIF;\n".format(r))
        cvc_constr.append("ASSERT IF y_0_{0}_2=0bin01 AND y_3_{0}_1=0bin01 THEN z_2_{0}_0=0bin00 ELSE 0bin1 = 0bin1 ENDIF;\n".format(r))
        cvc_constr.append("ASSERT IF y_0_{0}_2=0bin01 AND y_3_{0}_1=0bin10 THEN z_2_{0}_0=0bin11 ELSE 0bin1 = 0bin1 ENDIF;\n".format(r))
        cvc_constr.append("ASSERT IF y_0_{0}_2=0bin01 AND y_3_{0}_1=0bin11 THEN z_2_{0}_0=0bin11 ELSE 0bin1 = 0bin1 ENDIF;\n".format(r))
        cvc_constr.append("ASSERT IF y_0_{0}_2=0bin10 AND y_3_{0}_1=0bin00 THEN z_2_{0}_0=0bin10 ELSE 0bin1 = 0bin1 ENDIF;\n".format(r))
        cvc_constr.append("ASSERT IF y_0_{0}_2=0bin10 AND y_3_{0}_1=0bin01 THEN z_2_{0}_0=0bin11 ELSE 0bin1 = 0bin1 ENDIF;\n".format(r))
        cvc_constr.append("ASSERT IF y_0_{0}_2=0bin10 AND y_3_{0}_1=0bin10 THEN z_2_{0}_0=0bin00 ELSE 0bin1 = 0bin1 ENDIF;\n".format(r))
        cvc_constr.append("ASSERT IF y_0_{0}_2=0bin10 AND y_3_{0}_1=0bin11 THEN z_2_{0}_0=0bin11 ELSE 0bin1 = 0bin1 ENDIF;\n".format(r))
        cvc_constr.append("ASSERT IF y_0_{0}_2=0bin11 THEN z_2_{0}_0=0bin11 ELSE 0bin1 = 0bin1 ENDIF;\n".format(r))
        cvc_constr.append("\n")

        cvc_constr.append("ASSERT IF y_0_{0}_2=0bin00 THEN z_3_{0}_0=y_4_{0}_1 ELSE 0bin1 = 0bin1 ENDIF;\n".format(r))
        cvc_constr.append("ASSERT IF y_0_{0}_2=0bin01 AND y_4_{0}_1=0bin00 THEN z_3_{0}_0=0bin01 ELSE 0bin1 = 0bin1 ENDIF;\n".format(r))
        cvc_constr.append("ASSERT IF y_0_{0}_2=0bin01 AND y_4_{0}_1=0bin01 THEN z_3_{0}_0=0bin00 ELSE 0bin1 = 0bin1 ENDIF;\n".format(r))
        cvc_constr.append("ASSERT IF y_0_{0}_2=0bin01 AND y_4_{0}_1=0bin10 THEN z_3_{0}_0=0bin11 ELSE 0bin1 = 0bin1 ENDIF;\n".format(r))
        cvc_constr.append("ASSERT IF y_0_{0}_2=0bin01 AND y_4_{0}_1=0bin11 THEN z_3_{0}_0=0bin11 ELSE 0bin1 = 0bin1 ENDIF;\n".format(r))
        cvc_constr.append("ASSERT IF y_0_{0}_2=0bin10 AND y_4_{0}_1=0bin00 THEN z_3_{0}_0=0bin10 ELSE 0bin1 = 0bin1 ENDIF;\n".format(r))
        cvc_constr.append("ASSERT IF y_0_{0}_2=0bin10 AND y_4_{0}_1=0bin01 THEN z_3_{0}_0=0bin11 ELSE 0bin1 = 0bin1 ENDIF;\n".format(r))
        cvc_constr.append("ASSERT IF y_0_{0}_2=0bin10 AND y_4_{0}_1=0bin10 THEN z_3_{0}_0=0bin00 ELSE 0bin1 = 0bin1 ENDIF;\n".format(r))
        cvc_constr.append("ASSERT IF y_0_{0}_2=0bin10 AND y_4_{0}_1=0bin11 THEN z_3_{0}_0=0bin11 ELSE 0bin1 = 0bin1 ENDIF;\n".format(r))
        cvc_constr.append("ASSERT IF y_0_{0}_2=0bin11 THEN z_3_{0}_0=0bin11 ELSE 0bin1 = 0bin1 ENDIF;\n".format(r))
        cvc_constr.append("\n")

        #Perm
        cvc_constr.append("ASSERT x_0_{0}_0 = y_0_{0}_1;\n".format(r))
        cvc_constr.append("ASSERT x_1_{0}_0 = z_0_{0}_0;\n".format(r))
        cvc_constr.append("ASSERT x_2_{0}_0 = z_1_{0}_0;\n".format(r))
        cvc_constr.append("ASSERT x_3_{0}_0 = z_2_{0}_0;\n".format(r))
        cvc_constr.append("ASSERT x_4_{0}_0 = z_3_{0}_0;\n".format(r))

    cvc_constr.append("active_1 : BITVECTOR(1);\n")
    cvc_constr.append("ASSERT IF y_0_{0}_1 = 0bin00 THEN active_1 = 0bin0 ELSE active_1 = 0bin1 ENDIF;\n".format(round-1))
    cvc_constr.append("ASSERT active_1 = 0bin0;\n")
    cvc_constr.append("\n")

    cvc_constr.append("ASSERT y_0_0_0@y_1_0_0@y_2_0_0@y_3_0_0@y_4_0_0 /= 0bin0000000000;\n")
    cvc_constr.append("ASSERT y_0_0_0 /= 0bin11;\n")
    cvc_constr.append("ASSERT y_1_0_0 /= 0bin11;\n")
    cvc_constr.append("ASSERT y_2_0_0 /= 0bin11;\n")
    cvc_constr.append("ASSERT y_3_0_0 /= 0bin11;\n")
    cvc_constr.append("ASSERT y_4_0_0 /= 0bin11;\n")
    cvc_constr.append("\n")

    cvc_constr.append("QUERY FALSE;\nCOUNTEREXAMPLE;\n")

    return cvc_constr

def run(target, round):
    cvc = set_cvc(round)

    filename = target + "-round{0}.cvc".format(round)
    with open(filename, "w") as f:
        for item in cvc:
            f.write(item)
        f.close()
    command = 'stp ' + filename
    output = os.popen(command)
    return output

def remove_file(target, round):
    for i in range(1, round + 1):
        filename = target + "-round{0}.cvc".format(i)
        command_remove = './' + filename
        os.remove(command_remove)


if __name__ == '__main__':

    target = "TH-d5-r3"

    round = 1
    print("round = ", round)
    result = run(target, round)
    result1 = result.read()
    print("result1 = ", result1)

    while result1.find('Invalid.') >= 0:
        round = round + 1
        print("round = ", round)
        result = run(target, round)
        result1 = result.read()
        print("result1 = ", result1)
    else:
        print("max-r3 = ", round - 1)

    remove_file(target, round)
