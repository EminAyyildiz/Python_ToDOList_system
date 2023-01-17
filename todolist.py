# Written by EMİB AYYILDIZ
print("# Written by EMİB AYYILDIZ")
import datetime
import time
todo_list = []
def add_task(task_name, due_date):

    task = {"task_name": task_name, "due_date": due_date}
    todo_list.append(task)
    print("The task is being saved. Please wait...")
    time.sleep(1.5)
    print("Task successfully added :", task_name)

def view_to_do_list():

    if not todo_list:
        print("The tasks are being showed. Please wait...")
        time.sleep(1.5)
        print("Task List Empty.")
    else:
        for index, task in enumerate(todo_list):
            due_date = task["due_date"]
            due_date = datetime.datetime.strptime(due_date, "%d-%m-%Y").strftime("%d-%m-%Y")
            print("The tasks are being showed. Please wait...")
            time.sleep(1.5)
            print(f"{index + 1}. Task: {task['task_name']} - Last Date: {due_date}")

def delete_task(task_name):

    found = False
    for index, task in enumerate(todo_list):
        if task["task_name"] == task_name:
            task = todo_list.pop(index)
            found = True
            print("The tasks are being deleted. Please wait...")
            time.sleep(1.5)
            print("Task {} deleted successfully. ".format(task["task_name"]))
    if not found:
        print("Task not found.")

def save_tasks():

    with open("todo_list.txt", "w") as file:
        for task in todo_list:
            file.write(task["task_name"] + "," + task["due_date"] + "\n")
        print("The tasks are being saved. Please wait...")
        time.sleep(1.5)
        print("Tasks saved successfully.")

def load_tasks():
    global todo_list
    todo_list = []
    try:
        with open("todo_list.txt", "r") as file:
            tasks = file.readlines()
            for task in tasks:
                task_name, due_date = task.strip().split(",")
                todo_list.append({"task_name": task_name, "due_date": due_date})
            print("The tasks are being loaded. Please wait...")
            time.sleep(1.5)
            print("Saved tasks loaded successfully.")
    except FileNotFoundError:

        print("Saved task not found")

while True:

    print("****MENU**** \n1- Add Task \n2- Show all Task \n3- Delete Task \n4- Save Tasks \n5- Load Tasks \n6- EXIT")
    choice = input("Your choice : ")
    if choice == "1":
        task_name = input("Task Name: ")
        due_date = input("Last Date (GG-AA-YYYY): ")
        add_task(task_name, due_date)
    elif choice == "2":
        view_to_do_list()
    elif choice == "3":
        task_name = input("Task name to delete: ")
        delete_task(task_name)
    elif choice == "4":
        save_tasks()
    elif choice == "5":
        load_tasks()
    elif choice == "6":
        print("Exiting the app...")
        time.sleep(1.5)
        print("BYE BYE")
        break
    else:
        print("Invalid Choice")
