for i in range(1, 10):
    for j in range(1, 10):
        if j != 9:
            print(i, "*", j, "=", i*j, sep="", end="\t")
        else:
            print(i, "*", j, "=", i*j, sep="", end="\n")
