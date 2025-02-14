import sys
import json
from datetime import datetime

#create a list of accepted commands
commands_list  =["add", "delete", "update", "list", "mark-in-progress", "mark-done", ]
#create the task dictionary
tasks = {}

#get_id: return the last id + 1 in the tasks dictionary or 1 if the dictionary is empty
def get_id():
    if len(tasks):
        return int(list(tasks)[-1]) + 1
    else:
        return 1

#add task: create a new task with to-do status, set timestamp and update the task dictionary
def add_task(id, description):
    task = {"description": description,
            "status": "To-Do",
            "createdAt": datetime.now().strftime("%d-%m-%Y - %H:%M"),
            "updatedAt": datetime.now().strftime("%d-%m-%Y - %H:%M")}
    
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
    
def delete(id):
    del tasks[id]

def update(id, description):
    tasks[id]["description"] = description
    tasks[id]["updatedAt"] = datetime.now().strftime("%d-%m-%Y - %H:%M")

def list_tasks():
    ids = tasks.keys()

    for id in ids:
        print(f"ID: {id} | Descricao: {tasks[id]["description"]} | Status: {tasks[id]["status"]} | Created at: {tasks[id]["createdAt"]} | Updated at: {tasks[id]["updatedAt"]}")
        print("---------------------------------------------------------------------------------------------------------------------------------------------------------------")


tasks = get_tasks()


if sys.argv[1] not in commands_list:
    print("nao pegou comando")
elif sys.argv[1] == commands_list[0]:
    add_task(get_id(), sys.argv[2])
    save_tasks()
elif sys.argv[1] == commands_list[1]:
    delete(sys.argv[2])
    save_tasks()
elif sys.argv[1] == commands_list[2]:
    update(sys.argv[2], sys.argv[3])
    save_tasks()
elif sys.argv[1] == commands_list[3]:
    list_tasks()

