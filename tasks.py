import json
from datetime import datetime

DATA_FILE = "tasks.json"

def load_tasks():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except:
        return {"pending": [], "done": []}

def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task():
    tasks = load_tasks()
    name = input("Enter task name: ")
    time_est = input("Estimated time (e.g. 30 min or 2 hours): ")
    
    task = {
        "id": len(tasks["pending"]) + len(tasks["done"]) + 1,
        "name": name,
        "time_estimate": time_est,
        "time_taken": None,
        "added_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "owner": "Vinayak-Gamerzz"
    }
    
    tasks["pending"].append(task)
    save_tasks(tasks)
    print("✅ Task added successfully!")

def complete_task():
    tasks = load_tasks()
    if not tasks["pending"]:
        print("No pending tasks!")
        return
    
    print("\n=== Pending Tasks ===")
    for i, task in enumerate(tasks["pending"], 1):
        print(f"{i}. {task['name']} (Estimate: {task['time_estimate']})")
    
    try:
        choice = int(input("\nWhich task is done? Enter number: ")) - 1
        task = tasks["pending"].pop(choice)
        
        time_taken = input("Actual time taken (e.g. 45 min): ")
        task["time_taken"] = time_taken
        task["completed_at"] = datetime.now().strftime("%Y-%m-%d %H:%M")
        
        tasks["done"].append(task)
        save_tasks(tasks)
        
        print(f"🎉 Task completed! '{task['name']}' done in {time_taken}")
    except:
        print("Invalid number!")

def view_tasks():
    tasks = load_tasks()
    
    print("\n=== 📋 PENDING TASKS ===")
    if not tasks["pending"]:
        print("All tasks completed! Great job 🔥")
    else:
        for task in tasks["pending"]:
            print(f"• {task['name']} | Estimate: {task['time_estimate']} | Added: {task['added_at']}")
    
    print("\n=== ✅ DONE TASKS ===")
    if not tasks["done"]:
        print("No tasks completed yet.")
    else:
        for task in tasks["done"]:
            print(f"✓ {task['name']} | Estimate: {task['time_estimate']} | Taken: {task['time_taken']} | Done: {task['completed_at']}")

def main():
    print("📝 To-Do List with Time Tracking - Flavourtown Project")
    print("Made by Vinayak-Gamerzz\n")
    
    while True:
        print("1. Add New Task")
        print("2. Complete Task (with time taken)")
        print("3. View All Tasks")
        print("4. Exit")
        choice = input("Choose (1/2/3/4): ")
        
        if choice == "1":
            add_task()
        elif choice == "2":
            complete_task()
        elif choice == "3":
            view_tasks()
        elif choice == "4":
            print("Thanks for using! 🍪 Made for Hack Club Flavourtown by Vinayak-Gamerzz")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()


    #it is maded by vinayak_gamerzz for hack club flavourtown project
    # its my first project in python and i am very happy to share it with you all :)
    # if you have any suggestions or want to contribute , feel free to reach me out on github : Vinayak-Gamerzz, Slack : 