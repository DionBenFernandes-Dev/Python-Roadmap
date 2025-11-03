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


json_data = '[{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}, {"name": "Charlie", "age": 35}]'
data = json.loads(json_data)

# Remove the dictionary where 'name' is 'Bob'
data = [person for person in data if person['name'] != 'Bob']

updated_json_data = json.dumps(data, indent=2)
print(updated_json_data)