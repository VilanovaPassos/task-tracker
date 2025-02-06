import sys
import json
from datetime import datetime

commands_list  =["add", "delete", "update", "list", "mark-in-progress", "mark-done", ]
tasks = {}

def add_task(id, description):
    task = {"description": description,
            "status": "To-Do",
            "createdAt": datetime.now().strftime("%d-%m-%Y"),
            "updatedAt": datetime.now().strftime("%d-%m-%Y")}
    
    tasks.update({id: task})

def save_tasks():
    with open("tasks.json", "w") as f:
        json.dump(tasks, f)

def get_tasks():
    try:
        with open("tasks.json", "r") as f:
            return json.load(f)
    except:
        return {}

tasks = get_tasks()


if sys.argv[1] not in commands_list:
    print("nao pegou comando")
elif sys.argv[1] == commands_list[0]:
    add_task(len(tasks) + 1, sys.argv[2])
    save_tasks()

print(tasks)    
