import os

FILE_PATH = "tasks.txt"

def show_tasks():
    if not os.path.exists(FILE_PATH):
        print("🗒️ No tasks file found.\n")
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

def add_tasks(task):
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
        print(f"🎯 Completed: {completed.s}\n")
    else:
        print("❌ Invalid task number.\n")

def main():
    print("\n🧠 TO-DO LIST APP")
    print("-"*30)

    while True:
        print("Options:")
        print("1. View tasks")
        print("2. Add task")
        print("3. Complete task")
        print("4. Exit\n")

        choice = int(input("Choose an option(1-4): "))

        if choice == 1:
            show_tasks()
        elif choice == 2:
            task = input("Enter new task: ").strip()
            if task:
                add_tasks(task)
            else:
                print("⚠️  Empty task not added.\n")
        elif choice == 3:
            show_tasks()
            try:
                index = int(input("Enter task number to complete: "))
                complete_task(index)
            except ValueError:
                print("⚠️  Invalid input. Please enter a number.\n")
        elif choice == 4:
            print("👋 Exiting. Your tasks are saved!")
            break
        else:
            print("❌ Invalid option. Try again.\n")

if __name__ == "__main__":
    main()