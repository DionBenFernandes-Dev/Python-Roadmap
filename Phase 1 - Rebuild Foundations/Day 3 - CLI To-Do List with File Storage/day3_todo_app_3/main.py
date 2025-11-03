# todo app version: 3
# add: datetime, history, archive, clear

import os
import datetime
import json

TASK_FILE = "tasks.txt"
HISTORY_FILE = "history.txt"
ARCHIVE_FILE = "archive.txt"

def show_tasks():
    if not os.path.exists(TASK_FILE):
        print("\nTask file unavailable. Creating new file...\n")
        open(TASK_FILE,"w").close()
        return
    
    with open(TASK_FILE,"r") as t:
        tasks = [lines.strip() for lines in t.readlines()]

    if not tasks:
        print("\nNo task available in your list.\n")
    else:
        print("\n Your Task:\n")
        for (i,task) in enumerate(tasks,1):
            print(f"{i}. {task}")
        print()

def show_history():
    if not os.path.exists(HISTORY_FILE):
        print("\nHistory file unavailable. Creating new file...\n")
        open(HISTORY_FILE,"w").close()
        return
    
    with open(HISTORY_FILE,"r") as h:
        tasks = [lines.strip() for lines in h.readlines()]

    if not tasks:
        print("\nNo data available in history.\n")
    else:
        print("\nHistory:\n")
        for (i,task) in enumerate(tasks,1):
            print(f"{i}. {task}")
        print()

def show_archive():
    if not os.path.exists(ARCHIVE_FILE):
        print("\nArchive file unavailable. Creating new file...\n")
        open(ARCHIVE_FILE,"w").close()
        return
    
    with open(ARCHIVE_FILE,"r") as a:
        tasks = [lines.strip() for lines in a.readlines()]

    if not tasks:
        print("\nNo data available in archive.\n")
    else:
        print("\nArchive:\n")
        for (i,task) in enumerate(tasks,1):
            print(f"{i}. {task}")
        print()

def clear_tasks():
    print("\nClearing All Tasks...\n")
    with open(TASK_FILE, "w") as t:
        pass

def clear_history():
    print("\nClearing All History...\n")
    with open(HISTORY_FILE, "w") as h:
        pass

def clear_archive():
    print("\nClearing All Archive...\n")
    with open(ARCHIVE_FILE, "w") as a:
        pass

def add_tasks(task):
    add_task = task + " | " + datetime.datetime.now().strftime("%d-%m-%Y %H-%M")
    with open(TASK_FILE, "a") as t:
        t.write(add_task + "\n")
    # with open(HISTORY_FILE, "a") as h:
    #     h.write(add_task + "\n")
    print(f"\nAdded: {add_task}\n")

def complete_tasks(index):
    with open(TASK_FILE, "r") as t:
        tasks = t.readlines()

    if 0 < index <= len(tasks):
        with open(TASK_FILE, "w") as t:
            completed = tasks.pop(index - 1).strip()
            t.writelines(tasks)
            print(f"\nComplete: {completed}\n")
        
        with open(HISTORY_FILE, "a") as h:
            h.write(completed + "\n")
    else:
        print("\nInvalid task number.\n")

def archive_tasks(index):
    with open(TASK_FILE, "r") as t:
        tasks = t.readlines()

    if 0 < index <= len(tasks):
        with open(TASK_FILE, "a") as a:
            archived = tasks.pop(index - 1).strip()
            a.writelines(archived)
            print(f"\nArchive: {archived}\n")
        
        with open(ARCHIVE_FILE, "a") as a:
            a.write(archived + "\n")
    else:
        print("\nInvalid task number.\n")

def main():
    print("\n🧠 TO-DO LIST APP")
    print("-"*30)

    while True:
        print("Options:")
        print("1. View tasks")
        print("2. Add task")
        print("3. Complete task")
        print("4. Archive task")
        print("5. View history")
        print("6. View archive")
        print("7. Clear tasks")
        print("8. Clear history")
        print("9. Clear archive")
        print("10. Exit\n")

        choice = int(input("Choose an option(1-5): "))

        if choice == 1:
            show_tasks()
        elif choice == 2:
            task = input("\nEnter new task: ").strip()
            if task:
                add_tasks(task)
            else:
                print("\nEmpty task cannot be added.\n")
        elif choice == 3:
            show_tasks()
            try:
                index = int(input("\nEnter index number to complete: "))
                complete_tasks(index)
            except ValueError:
                print("\nInvalid Input. Please enter a number.\n")
        elif choice == 4:
            show_tasks()
            try:
                index = int(input("\nEnter index number to archive: "))
                archive_tasks(index)
            except ValueError:
                print("\nInvalid Input. Please enter a number.\n")
        elif choice == 5:
            show_history()
        elif choice == 6:
            show_archive()
        elif choice == 7:
            clear_tasks()
        elif choice == 8:
            clear_history()
        elif choice == 9:
            clear_archive()
        elif choice == 10:
            print("\nExiting... Your tasks are saved!")
            break
        else:
            print("\nInvalid option. Try again.\n")

if __name__ == "__main__":
    main()
