def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def mod(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x % y

def pow(x, y):
    return x ** y

def calculator():
    print("Enter the operation you want to perform:\n")
    print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Modulus\n6. Power\n7. Quit")

    while True:
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 7.")
            continue

        if choice == 7:
            print("Exiting the calculator. Goodbye!")
            break
        elif choice in [1, 2, 3, 4, 5, 6]:
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
            except ValueError:
                print("Invalid input. Please enter numerical values.")
                continue

            if choice == 1:
                result = add(num1, num2)
            elif choice == 2:
                result = sub(num1, num2)
            elif choice == 3:
                result = mul(num1, num2)
            elif choice == 4:
                result = div(num1, num2)
            elif choice == 5:
                result = mod(num1, num2)
            elif choice == 6:
                result = pow(num1, num2)

            print("Result is:", result)
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

calculator()
