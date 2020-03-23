print("You entered the calculator.")
flag = True
while flag:
    val_1 = float(input("input first number: "))
    val_2 = float(input("input double number: "))
    command = input("input operation: ")
    if command == "+":
        print(val_1 + val_2)
    elif command == "-":
        print(val_1 - val_2)
    elif command == "*":
        print(val_1 * val_2)
    elif command == "/":
        print(val_1 / val_2)
    elif command == "**":
        print(val_1 ** val_2)
    else:
        print("Input uncorect command")
    for i in range(3):
        command = (input("continue?(Y/N)"))
        if command == "Y":
            break
        elif command == "N":
            flag = False
            break
        else:
            print("Wrong command")
        if i == 2:
            print("Too much error!\nGet out!")
            flag = False
            break
