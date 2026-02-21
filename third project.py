
import os

tasks=[]

filename = "task.txt"

if os.path.exists(filename):
    with open(filename,"r")as file:
        for line in file:
            parts=line.strip().split("|")
            if len(parts)==2:
               tasks.append({"task":parts[0],"deadline":parts[1]})
            else:
                tsaks.append({"task":parts[0],"deadline":"No deadline"})

        
def show_menu():
    print("\n===TO Do List Menue===")
    print("1.Add a tassk ")
    print("2.View task ") 
    print("3.Remove A Task")
    print("4.Upadete a task")
    print("5.Save and exit")

while True:
    show_menu()
    choice=input("Enter you choice(1-5):")

    if choice=='1':
        task_name=input("Enter a new task:")
        deadline=input("Enter deadline(e.g,,2025-10-30):")
        tasks.append({"task":task_name,"deadline":deadline})
        print("Task added with deadline!")

    elif choice=='2':
        if not tasks:
            print("No task yet")
        else:
            print("\n Your task")
            for i,t in enumerate(tasks,start=1):
                print(f"{i}.{t['task']}(Deadline:{t['deadline']})")
    elif choice=='3':
        if not tasks:
            print("No tasks to remove!")
        else:
            for i,t in enumerate(tasks,start=1):
                print(f"{i}.{t['task']}(Deadline:{t['Deadline']})")
            num=int(input("Enter task number to remove:"))
            if 1<=num<=len(tasks):
                removed=tasks.pop(num-1)
                print("Removed.",removed)
            else:
                print("invalid task number!")

    elif choice=='4':
        if not tasks:
            print("No task to updated!")
        else:
            for i,t in enumerate(tasks,start=1):
                print(f"{i}.{t['task']}(deadline:{t['deadline']})")
                num=int(input("enter task number to update:"))
                if 1<=num<= len(tasks):
                    new_task=input("enter new task name:")
                    new_deadline=input("enter new deadline:")
                    tasks[num-1]["task"]=new_task
                    tasks[num-1]["deadliine"]=new_deadline
                    print("Tassk Updated!")
                else:
                    print("invalid task number!")

    elif choice=='5':
        with open(filename,"w")as file:
            for t in tasks:
                file.write(f"{t['task']}|{t['deadline']}\n")
        print("Tasks saved with deadline ! bye")
        break
    else:
        print("invalid choice,please enter 1-5")
        
        print("invalid choice,please enter 1-4:")
