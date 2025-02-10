import sys
import json
from datetime import datetime

#create a list of accepted commands
commands_list  =["add", "delete", "update", "list", "mark-in-progress", "mark-done", ]
#create the task dictionary
tasks = {}

#add task: create a new task with to-do status, set timestamp and update the task dictionary
def add_task(id, description):
    task = {"description": description,
            "status": "To-Do",
            "createdAt": datetime.now().strftime("%d-%m-%Y"),
            "updatedAt": datetime.now().strftime("%d-%m-%Y")}
    
    tasks.update({id: task})

#save_task: write the tasks dictionary on a json file named tasks.json 
def save_tasks():
    with open("tasks.json", "w") as f:
        json.dump(tasks, f)

#get_tasks: try to read the json file, in case of failure return an empty dictinary
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
