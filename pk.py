print("Welcome to calculator")
while True:
    a = int(input("Enter the first number: "))
    b = int(input("Enter  the second number: "))
    o = input("Enter opcode from +,-,/,*: ")
    if o =="+":
        print(a+b)
    elif o=="-":
        print(a-b)
    elif o=="*":
        print(a*b)
    elif o =="/":
        print(a/b)

    decision = input("Enter 'quit' to exit or press any key to continue: ")
    if decision == 'quit':
        break