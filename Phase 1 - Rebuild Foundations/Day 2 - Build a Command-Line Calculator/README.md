# 🗓️ **Day 2 — Build a Command-Line Calculator**

**Goal:** Strengthen your fundamentals — functions, loops, user input, error handling, and logic flow.

---

## ⏱️ **1-Hour Plan**

| Time      | Task                                | Description                                               |
| --------- | ----------------------------------- | --------------------------------------------------------- |
| 0–10 min  | **Concept Refresh**                 | Review input handling, conditionals, and functions.       |
| 10–35 min | **Code Along**                      | Build a working calculator (addition, subtraction, etc.). |
| 35–50 min | **Add Validation + Error Handling** | Handle wrong inputs, invalid operators, divide-by-zero.   |
| 50–60 min | **Mini-Assignment + Documentation** | Extend functionality + write README.                      |

---

## 🧠 **Concept Refresh (10 min)**

### Input and Type Conversion

```python
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
```

### Functions

```python
def add(a, b):
    return a + b
```

### Loops + Conditionals

```python
while True:
    choice = input("Enter choice: ")
    if choice == 'q':
        break
```

### Exception Handling

```python
try:
    result = a / b
except ZeroDivisionError:
    print("Cannot divide by zero")
```

---

## 💻 **Code-Along (25 min)**

Create a new folder:

```
day2_calculator/
    └── calculator.py
```

Open your file and start coding 👇

```python
# calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("⚠️ Cannot divide by zero.")
        return None

def main():
    print("🧮 Simple Python Calculator")
    print("---------------------------")
    print("Available operations: +  -  *  /")
    print("Type 'q' to quit.\n")

    while True:
        choice = input("Enter operation (+, -, *, /, q): ")

        if choice == 'q':
            print("👋 Exiting calculator. Goodbye!")
            break

        if choice not in ['+', '-', '*', '/']:
            print("❌ Invalid operation. Try again.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '+':
                result = add(num1, num2)
            elif choice == '-':
                result = subtract(num1, num2)
            elif choice == '*':
                result = multiply(num1, num2)
            elif choice == '/':
                result = divide(num1, num2)

            if result is not None:
                print(f"✅ Result: {result}\n")

        except ValueError:
            print("⚠️ Invalid input! Please enter numbers only.\n")

if __name__ == "__main__":
    main()
```

I use match instead of if-elif-else method 👇

```python
# calculator.py
match choice:
    case '+':
        result = add(num1, num2)
    case '-':
        result = sub(num1, num2)
    case '*':
        result = mul(num1, num2)
    case '/':
        result = div(num1, num2)
```

Run it:

```bash
python calculator.py
```

✅ You now have an interactive calculator!

---

## 🧩 **Mini-Assignment (10 min)**

Enhance the calculator — choose **any one or more** challenges below:

### 🧮 Level 1 (Logic)

1. Add new operations:

   * Power (`**`)
   * Modulus (`%`)
   * Square root (`math.sqrt()`)

### 🧾 Level 2 (UX & Design)

2. Display a history of all operations done during the session.
   (Store results in a list and print them when user exits.)

Example:

```python
history = []
# after each calculation:
history.append(f"{num1} {choice} {num2} = {result}")
```

### 💾 Level 3 (File Handling)

3. Save all calculations to a text file:

   * File: `calc_history.txt`
   * Each line: `5 + 3 = 8`

```python
with open("calc_history.txt", "a") as f:
    f.write(f"{num1} {choice} {num2} = {result}\n")
```

---

## 🧰 **Optional Exploration (Extra 10 min if you can)**

Try using **Python dictionaries** to simplify code:

```python
operations = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b if b != 0 else "Division by zero!"
}
```

Now you can call:

```python
result = operations[choice](num1, num2)
```

---

## 🏁 **End-of-Day Deliverables**

* ✅ `calculator.py`
* ✅ (optional) `calc_history.txt`
* ✅ A short `README.md`:

  ```markdown
  # Day 2 - Command Line Calculator
  - Learned functions, loops, and error handling.
  - Features: add, subtract, multiply, divide.
  - Extensions: history log, file saving.
  ```

Push it to GitHub:

```bash
git add .
git commit -m "Day 2: CLI Calculator"
git push
```

---

## 🧠 **Reflection Questions**

1. How do `try/except` blocks improve code reliability?
Answer.
```
It helps in handling expecting errors and ensure the program run even if faced one. It also helps in identifying error beyond what I have expected.
```
2. Why is `float()` used for inputs instead of `int()`?
Answer.
```
Float is used instead of int as it is easy to handle float since I am dividing them which has a chance to be a decimal number. If num1 & num2 is int and results in a float it would rise an error. Secondly using only input() would result in have numbers taken as str values.
```
3. How could you refactor your code to reduce repetition?
Answer.
```
Move repeated code to functions as well as Use loops and comprehensions. There is more but I have to use it first before stating it.
```
