# Tracker: A CLI Task Tracker

Tracker is a simple command-line application designed to track your tasks.
With Tracker, you can add, update, change status, delete, and list all your tasks.

This application is a project from roadmap.sh. You can learn more [here](https://roadmap.sh/projects/task-tracker).

## Installation
Just clone this repository and run `tracker.py` with Python.

```sh
git clone https://github.com/VilanovaPassos/task-tracker.git
cd task-tracker
python3 tracker.py add "My first task"
```

## Usage
```sh
python3 tracker.py <command> <attribute>
```

### Adding a New Task
```sh
python3 tracker.py add "Buy groceries"
```
*Returns a message with the new task ID.*

### Updating and Deleting Tasks
```sh
python3 tracker.py update 1 "Buy groceries and cook dinner"
```
*Updates the description of the task with ID 1.*

```sh
python3 tracker.py delete 1
```
*Deletes the task with ID 1.*

### Marking a Task as In Progress or Done
```sh
python3 tracker.py mark-in-progress 1
```
*Changes the status of task ID 1 to "In Progress".*

```sh
python3 tracker.py mark-done 1
```
*Changes the status of task ID 1 to "Done".*

### Listing All Tasks
```sh
python3 tracker.py list
```

### Listing Tasks by Status
```sh
python3 tracker.py list Done
python3 tracker.py list Todo
python3 tracker.py list In-Progress