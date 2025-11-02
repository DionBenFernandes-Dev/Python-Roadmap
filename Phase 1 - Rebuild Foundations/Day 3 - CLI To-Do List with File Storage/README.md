# 🗓️ **Day 3 — CLI To-Do List with File Storage**

**Goal:** Build a simple command-line To-Do app that lets you **add, view, complete, and delete tasks**, all saved in a text file.

---

## ⏱️ **1-Hour Plan**

| Time      | Task                         | Description                                               |
| --------- | ---------------------------- | --------------------------------------------------------- |
| 0–10 min  | **Concept Refresh**          | CRUD operations (Create, Read, Update, Delete) with files |
| 10–35 min | **Code-Along**               | Build the working CLI app step-by-step                    |
| 35–50 min | **Add Enhancements**         | Add timestamps, status tracking, or numbering             |
| 50–60 min | **Mini Assignment + GitHub** | Extend one feature and document it                        |

---

## 🧠 **Concept Refresh (10 min)**

You’ll be using:

```python
# Append to file
with open("tasks.txt", "a") as f:
    f.write("Buy milk\n")

# Read from file
with open("tasks.txt", "r") as f:
    tasks = f.readlines()

# Rewrite (overwrite file)
with open("tasks.txt", "w") as f:
    f.writelines(updated_tasks)
```

CRUD =

* **Create** → Add new task
* **Read** → Show all tasks
* **Update** → Mark task as done
* **Delete** → Remove a task

---

## 💻 **Code-Along (25 min)**

### Folder setup:

```
day3_todo_app/
    └── todo.py
```

Open `todo.py` and start coding 👇

---

### **Step 1: Define Helper Functions**

```python
import os

FILE_PATH = "tasks.txt"

def show_tasks():
    if not os.path.exists(FILE_PATH):
        print("🗒️ No tasks found.\n")
        return

    with open(FILE_PATH, "r") as f:
        tasks = [line.strip() for line in f.readlines()]

    if not tasks:
        print("✅ No tasks in your list.\n")
    else:
        print("\n📝 Your Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        print()
```

---

### **Step 2: Add, Complete, Delete Tasks**

```python
def add_task(task):
    with open(FILE_PATH, "a") as f:
        f.write(task + "\n")
    print(f"✅ Added: {task}\n")

def complete_task(index):
    with open(FILE_PATH, "r") as f:
        tasks = f.readlines()

    if 0 < index <= len(tasks):
        completed = tasks.pop(index - 1)
        with open(FILE_PATH, "w") as f:
            f.writelines(tasks)
        print(f"🎯 Completed: {completed.strip()}\n")
    else:
        print("❌ Invalid task number.\n")
```

---

### **Step 3: The Main Menu Loop**

```python
def main():
    print("🧠 TO-DO LIST APP")
    print("-----------------")

    while True:
        print("Options:")
        print("1. View tasks")
        print("2. Add task")
        print("3. Complete task")
        print("4. Exit\n")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            task = input("Enter new task: ").strip()
            if task:
                add_task(task)
            else:
                print("⚠️ Empty task not added.\n")
        elif choice == "3":
            show_tasks()
            try:
                index = int(input("Enter task number to complete: "))
                complete_task(index)
            except ValueError:
                print("⚠️ Invalid input. Please enter a number.\n")
        elif choice == "4":
            print("👋 Exiting. Your tasks are saved!")
            break
        else:
            print("❌ Invalid option. Try again.\n")

if __name__ == "__main__":
    main()
```

---

### ✅ Run It:

```bash
python todo.py
```

Try:

```
1  → View tasks
2  → Add “Buy milk”
1  → See it appear
3  → Complete it
1  → Confirm it’s gone
```

---

## 🧩 **Mini-Assignment (10–15 min)**

Pick **any 1–2 extensions** below to deepen your logic & file handling skills 👇

### 🧮 Level 1 — Timestamps

Add the date & time to every task:

```python
from datetime import datetime
task = f"{task} (added: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')})"
```

### 🧾 Level 2 — Task Status

Mark tasks as ✅ Done or ⏳ Pending instead of deleting them.

* Store tasks as `Task | Status`
* Example: `"Buy milk | Pending"`
* Use `.split("|")` to parse and toggle status.

### 💾 Level 3 — JSON Storage

Save tasks in JSON for better structure:

```python
import json

tasks = [{"task": "Buy milk", "done": False}]
with open("tasks.json", "w") as f:
    json.dump(tasks, f, indent=4)
```

### 🧰 Bonus — Error Recovery

If the file is accidentally deleted, recreate it automatically at runtime.

---

## 🧠 **Optional Exploration (Extra Credit)**

* Create a *“Daily To-Do Summary”* function that shows how many tasks were done today.
* Use a Python scheduler (`schedule` library) to auto-show tasks daily at 9 AM.

---

## 🏁 **End-of-Day Deliverables**

✅ `todo.py`
✅ `tasks.txt` (auto-created)
✅ Optional: `tasks.json` if you extend
✅ A short `README.md`:

```markdown
# Day 3 - CLI To-Do List App
- Features: Add, view, complete tasks (saved to file)
- Libraries: os, datetime, json (optional)
- Learned CRUD operations & file I/O persistence
```

Push to GitHub:

```bash
git add .
git commit -m "Day 3: To-Do List CLI App"
git push
```

---

## 🧠 **Reflection Questions**

1. What’s the difference between reading and appending a file in Python?
2. Why should you always `.strip()` text read from files?
3. How would you modify the app to handle multiple users or lists?
