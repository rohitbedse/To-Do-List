to_do_list = []

def add_task(task):
    to_do_list.append(task)
    print(f"Task '{task}' added to the to-do list.")

def view_list():
    if not to_do_list:
        print("The to-do list is empty.")
    else:
        print("To-Do List:")
        for index, task in enumerate(to_do_list, start=1):
            print(f"{index}. {task}")

def remove_task(task_index):
    if 1 <= task_index <= len(to_do_list):
        removed_task = to_do_list.pop(task_index - 1)
        print(f"Task '{removed_task}' removed from the to-do list.")
    else:
        print("Invalid task index. Please provide a valid task index.")

while True:
    print("\nOptions:")
    print("1. Add a task")
    print("2. View the to-do list")
    print("3. Remove a task")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter the task: ")
        add_task(task)
    elif choice == "2":
        view_list()
    elif choice == "3":
        view_list()
        task_index = int(input("Enter the index of the task to remove: "))
        remove_task(task_index)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
