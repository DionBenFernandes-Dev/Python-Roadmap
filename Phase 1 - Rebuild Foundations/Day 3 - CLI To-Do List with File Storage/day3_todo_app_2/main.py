# todo app version: 2
# add: datetime, history

import os
import datetime

TASK_FILE = "tasks.txt"
HISTORY_FILE = "history.txt"

def show_tasks():
    if not os.path.exists(TASK_FILE):
        print("\nNo tasks.txt available. Please choose option 2 to create file.\n")
        return
    
    with open(TASK_FILE, "r") as f:
        tasks = [lines.strip() for lines in f.readlines()]

    if not tasks:
        print("\nNo tasks in your lists.\n")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks,1): #enumerate() function adds a counter to each item in a list or any other iterable, and returns a list of tuples containing the index position and the element for each element of the iterable.
            print(f"{i}. {task}")
        print()

def add_tasks(task):
    with open(TASK_FILE, "a") as f:
        f.write(task + f" | (added: {datetime.datetime.now().strftime("%d-%m-%Y %H:%M")})\n")
    print(f"\nAdded: {task}\n")

def complete_tasks(index):
    with open(TASK_FILE, "r") as f:
        tasks = f.readlines()
    
    if 0 < index <= len(tasks):
        with open(TASK_FILE, "w") as f:
            completed = tasks.pop(index - 1).strip()
            f.writelines(tasks)
            print(f"\nCompleted: {completed}\n")
            with open(HISTORY_FILE, "a") as h:
                h.write(completed)
    else:
        print("\nInvalid Task number.\n")

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
                print("Empty task not added.\n")
        elif choice == 3:
            show_tasks()
            try:
                index = int(input("Enter task number to complete: "))
                complete_tasks(index)
            except ValueError:
                print("Invalid input. Please enter a number.\n")
        elif choice == 4:
            print("Exiting. Your tasks are saved!")
            break
        else:
            print("Invalid option. Try again.\n")

if __name__ == "__main__":
    main()



