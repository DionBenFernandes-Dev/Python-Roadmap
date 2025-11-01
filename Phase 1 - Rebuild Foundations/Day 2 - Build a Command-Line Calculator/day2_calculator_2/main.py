# calculator version: 2
# added more operation: Power(**), Modulus(%) and Square Root(math.sqrt())
# added history and saved them in a file

import math

# Addition
def add(a,b):
    return a + b

# Subtraction
def sub(a,b):
    return a - b

# Multiplication
def mul(a,b):
    return a * b

# Division
def div(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Cannot be divided by zero")

# Power of
def powof(a,b):
    return pow(a,b)

# Mudulus
def modu(a,b):
    return a % b

# Square Root of both a & b
def squrt(a,b):
    return [math.sqrt(a), math.sqrt(b)]

def main():
    print("Simple Python Calculator")
    print("-"*30)
    print("Available operation: +, -, *, /, **, %, sqrt")
    print("Type 'q' to quit.\n")

    history = []

    while True:
        choice = input("Enter the operation(+,-,*,/,**,%,sqrt,q): ")

        if choice == 'q':
            print("\n👋 Exiting calculator. Goodbye!")
            break

        if choice not in ['+', '-', '*', '/', '**', '%', 'sqrt', 'q']:
            print("\nInvalid Operation, try again...\n")
            continue

        try:

            num1 = float(input("Enter 1st number: "))
            num2 = float(input("Enter 2nd number: "))

            match choice:
                case '+':
                    result = add(num1, num2)
                case '-':
                    result = sub(num1, num2)
                case '*':
                    result = mul(num1, num2)
                case '/':
                    result = div(num1, num2)
                case '**':
                    result = powof(num1, num2)
                case '%':
                    result = modu(num1, num2)
                case 'sqrt':
                    result = squrt(num1, num2)

            if result is not None:
                print(f"Result: {result}\n")
                history.append(f"{num1} {choice} {num2} = {result}")

        except ValueError:
            print("Invalid Input. Please enter numbers only.\n")

        except Exception as e:
            print(f"Error: {e}")
    
    if len(history) != 0:
        print("\nHistory:\n")
        with open("history.txt", "a") as file:
            for h in history:
                print(h)
                file.write(f"{h}\n")

if __name__ == "__main__":
    main()