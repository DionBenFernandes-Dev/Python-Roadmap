# calculator version: 3

import math

def main():
    
    operation = {
        '+': lambda a,b: a+b,
        '-': lambda a,b: a-b,
        '*': lambda a,b: a*b,
        '/': lambda a,b: a/b if b != 0 else print("\nCannot divide by 0.\n"),
        '**': lambda a,b: a**b,
        '%': lambda a,b: a%b,
        'sqrt': lambda a,b: [math.sqrt(a), math.sqrt(b)],
    }

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

            result = operation[choice](num1,num2)

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