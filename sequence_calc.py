def runthis2():
    print("type 'arithmetic' for arithmetic progression, 'geometric' for geometric progression. ")
    droop = input("which sequence you want to solve: ")
    if droop == "arithmetic":
        def arithmetic():
            t1 = float(input("first term: "))
            n = int(input("term you want to find: "))
            dif = float(input("difference between terms: "))
            print("")
            print("")
            print("formula for finding Nth term: tn = t1 + (n - 1) * d")
            print("")
            print(f"so, formula is: {t1} + ({n} - 1) * {dif}")
            print("")
            tn = t1 + (n - 1) * dif
            print("Nth term = ")
            print(tn)


        arithmetic()


    elif droop == "geometric":
        def geometric():
            t1 = int(input("first term: "))
            r = int(input("common ratio of sequence: "))
            n = int(input("term you want to find: "))
            tn = t1 * (r ** (n - 1))
            print(tn)


        geometric()