def runthis():
    global first
    global second
    global op

    first = float(input("first number: "))
    print(
        "operators are '+' for addition,"
        " '-' for subtraction,"
        " '*' for multiplication,"
        " '/' for division,"
        " '%' for modulus,"
        " 'square' for squaring the first number,"
        " 'cube' for cubing the first number,"
        " 'more than cube' for exponents larger than 3,"
        " 'square root' for square rooting the first number and"
        " 'cube root' for cube rooting the 1st number"
        )
    second = input("operator: ")
    op = float(input("second number: "))

    def addition():
        if second == "+":
            print(first + op)

    def subtraction():
        if second == "-":
            print(first - op)

    def multiplication():
        if second == "*":
            print(first * op)

    def division():
        if second == "/":
            print(first / op)

    def mod():
        if second == "%":
            print(first % op)

    def square():
        if second == "square":
            print(first ** 2)

    def cube():
        if second == "cube":
            print(first ** 3)

    def tothepowerof():
        if second == "more than cube":
            print(first ** op)

    def squareroot():
        if second == "square root":
            print(first ** 0.5)

    def cuberoot():
        if second == "cube root":
            print(first ** 1 / 3)

    addition()
    subtraction()
    multiplication()
    division()
    square()
    cube()
    tothepowerof()
    squareroot()
    cuberoot()
    mod()
