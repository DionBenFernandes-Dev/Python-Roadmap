import json
import datetime

tasks = [
    {
        "task": "Buy milk", 
        "completed": False, 
        "archived": False, 
        "date-time": datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
    },
    {
        "task": "Buy eggs", 
        "completed": True, 
        "archived": False, 
        "date-time": datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
    }
]
with open("test.json", "w") as f:
    json.dump(tasks, f, indent=4)

with open("test.json", "r") as f:
    task = json.load(f)

print(task)
print(task[0]["task"])
print(task[1]["completed"])

for (i,t) in enumerate(task,1):
    print(f"{i}. {t["task"]}\t| {"Completed" if t["completed"] else "Not Completed"}\t| {t["date-time"]}")

complete = task[0]
del task[0]
print(task)
print(complete)