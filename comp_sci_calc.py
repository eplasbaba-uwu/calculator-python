def runthis4():
    print("List of functions: "
          "dec-to-bin, "
          "bin-to-dec, "
          "bin-to-hex, "
          "hex-to-bin, "
          "dec-to-hex, "
          "hex-to-dec"
          )
    ligma = input("Enter function: ")
    if ligma == "dec-to-bin":
        num = int(input("Enter any positive integer : "))
        binary = []
        while num != 1:
            binary.append(num % 2)
            num = num // 2
        binary.reverse()
        answer = 1
        for x in binary:
            answer = answer * 10 + x
        print("Answer is :" + str(answer))
    elif ligma == "bin-to-dec":
        binary = str(input("Enter binary number: "))
        flag = False
        for each in binary:
            if each != '0' and each != '1':
                print("Error in input")
                flag = False
                break
            else:
                flag = True
        if flag == True:
            result = 0
            exp = len(binary) - 1
            for x in range(0, len(binary)):
                result = int(binary[x]) * (2 ** exp) + result
                exp -= 1
            print(result)
    elif ligma == "bin-to-hex":
        print("Enter the Binary Number: ", end="")
        bnum = int(input())

        h = 0
        m = 1
        chk = 1
        i = 0
        hnum = []
        while bnum != 0:
            rem = bnum % 10
            h = h + (rem * m)
            if chk % 4 == 0:
                if h < 10:
                    hnum.insert(i, chr(h + 48))
                else:
                    hnum.insert(i, chr(h + 55))
                m = 1
                h = 0
                chk = 1
                i = i + 1
            else:
                m = m * 2
                chk = chk + 1
            bnum = int(bnum / 10)

        if chk != 1:
            hnum.insert(i, chr(h + 48))
        if chk == 1:
            i = i - 1

        print("\nEquivalent Hexadecimal Value = ", end="")
        while i >= 0:
            print(end=hnum[i])
            i = i - 1
        print()
    elif ligma == "hex-to-bin":
        ini_string = input("Enter hexadecimal value: ")
        scale = 16

        # Printing initial string
        print("Initial string", ini_string)

        # Code to convert hex to binary
        res = bin(int(ini_string, scale)).zfill(8)

        # Print the resultant string
        print("Resultant string", str(res))
    elif ligma == "dec-to-hex":
        number = int(input("Enter decimal value: "))
        str_number = str(number)
        hexvalue = hex(number)
        print(f"Hexadecimal value of {str_number} is: " + hexvalue)

    elif ligma == "hex-to-dec":
        test_string = input("Enter hexadecimal value: ")

        # printing original string
        print("The original string : " + str(test_string))

        # using int()
        # converting hexadecimal string to decimal
        res = int(test_string, 16)

        # print result
        print("The decimal number of hexadecimal string : " + str(res))
    else:
        print("Invalid Input")