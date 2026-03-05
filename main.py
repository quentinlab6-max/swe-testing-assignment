from calculator import Calculator

calc = Calculator()

while True:
    print("\nQuick-Calc")
    print("1 Add")
    print("2 Subtract")
    print("3 Multiply")
    print("4 Divide")
    print("5 Clear")
    print("6 Exit")

    choice = input("Choose option: ")

    if choice == "6":
        break

    if choice == "5":
        print("Result:", calc.clear())
        continue

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == "1":
        print("Result:", calc.add(a, b))

    elif choice == "2":
        print("Result:", calc.subtract(a, b))

    elif choice == "3":
        print("Result:", calc.multiply(a, b))

    elif choice == "4":
        try:
            print("Result:", calc.divide(a, b))
        except ValueError as e:
            print(e)