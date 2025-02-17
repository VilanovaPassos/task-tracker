#!/usr/bin/python3

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

#delete: delete the task with id key   
def delete(id):
    del tasks[id]

#update: updates the description and updateAt atributes in the task id
def update(id, description):
    tasks[id]["description"] = description
    tasks[id]["updatedAt"] = datetime.now().strftime("%d-%m-%Y - %H:%M")

#list_task: get the ids creating a list of keys in tasks and print each taks in a for loop 
def list_tasks():
    ids = tasks.keys()

    for id in ids:
        print(f"ID: {id} | Descricao: {tasks[id]["description"]} | Status: {tasks[id]["status"]} | Created at: {tasks[id]["createdAt"]} | Updated at: {tasks[id]["updatedAt"]}")
        print("---------------------------------------------------------------------------------------------------------------------------------------------------------------")

#mark_in_progress: change the status to "In-Progress"
def mark_in_progress(id):
    tasks[id]["status"] = "In-Progress"
    tasks[id]["updatedAt"] = datetime.now().strftime("%d-%m-%Y - %H:%M")

#mark_in_progress: change the status to "Done"
def mark_done(id):
    tasks[id]["status"] = "Done"
    tasks[id]["updatedAt"] = datetime.now().strftime("%d-%m-%Y - %H:%M")


#read tasks
tasks = get_tasks()

#check if recieve one argument
if len(sys.argv) > 1:
    if sys.argv[1] not in commands_list: 
        print(f"Command not found! Use one of the following commands {commands_list}")
    elif sys.argv[1] == commands_list[0]:
        #add
        add_task(get_id(), sys.argv[2])
        save_tasks()
    elif sys.argv[1] == commands_list[1]:
        #delete
        delete(sys.argv[2])
        save_tasks()
    elif sys.argv[1] == commands_list[2]:
        #update
        update(sys.argv[2], sys.argv[3])
        save_tasks()
    elif sys.argv[1] == commands_list[3]:
        #list
        list_tasks()
    elif sys.argv[1] == commands_list[4]:
        #mark-in-progress
        mark_in_progress(sys.argv[2])
        save_tasks()
    elif sys.argv[1] == commands_list[5]:
        #mark-done
        mark_done(sys.argv[2])
        save_tasks()
else:
    print(f"Use one of the following commands {commands_list}")