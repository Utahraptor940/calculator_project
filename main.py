from calculator import *

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choice = input("Your choice(1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", Calculator.add(Calculator.add, num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", Calculator.subtract(Calculator.subtract, num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", Calculator.multiply(Calculator.multiply, num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", Calculator.divide(Calculator.divide, num1, num2))

        next_calculation = input("Another calculation? (yes/no): ")
        if next_calculation == "no":
            break

    else:
        print("Invalid Input")
