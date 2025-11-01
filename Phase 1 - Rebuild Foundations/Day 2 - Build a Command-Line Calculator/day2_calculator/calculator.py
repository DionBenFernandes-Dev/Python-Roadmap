# calculator

def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        print("⚠️  Cannot divide by zero.")
        return None
    
def main():
    print("🧮 Simple Python Calculator")
    print("---------------------------")
    print("Available operations: +  -  *  /")
    print("Type 'q' to quit.\n")

    while True:
        choice = input("Enter operation (+,-,*,/,q): ")

        if choice == 'q':
            print("👋 Exiting calculator. Goodbye!")
            break

        if choice not in ['+','-','*','/']:
            print("❌ Invalid operation. Try again.")
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

            if result is not None:
                print(f"✅ Result: {result}\n")
            
        except ValueError:
            print("⚠️  Invalid input! Please enter numbers only.\n")

if __name__ == "__main__":
    main()