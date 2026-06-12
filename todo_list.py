tasks = []

while True:
    print("\n==== TO-DO LIST MENU")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Search Task")
    print("4. Delete Tasks")
    print("5. Exit")

    choice = input("Enter your choice:")

    if choice=="1":
        task_id=input("Enter Task ID:")
        task_name=input("Enter Task Name:")

        task={
            "id":task_id,
            "name":task_name  
        }

        tasks.append(task)
        print("Task added successfully!")

    elif choice=="2":
        if len(tasks)==0:
            print("No tasks are available")
        else:
            print("\n==== TASK LIST ====")
            for task in tasks:
                print(f"Task ID:{task['id']}, Task Name:{task['name']}")

    elif choice=="3":
        search_id=input("Enter Task ID to search:")

        found=False
        for task in tasks:
            if task["id"]==search_id:
                print("\nTask Found")
                print(f"Task ID: {task['id']}")
                print(f"Task Name: {task['name']}")
                found=True
                break
        if not found:
            print("task not found")

    elif choice=="4":
        delete_id=input("Enter Task ID to delete:")

        found=False
        for task in tasks:
            if task["id"]==delete_id:
                tasks.remove(task)
                print("Task deleted successfully!")
                found=True
                break

        if not found:
            print("Task not found!")

    elif choice=="5":
        print("Thank you for using to-do list!!")
        break
    else:
        print("Invalid choice! Please Try again.")
