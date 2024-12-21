tasks={}
x=1
while True:
    print("To do list check this commend: ")
    print("    1-for add a task.")
    print("    2-for views the tasks.")
    print("    3-for deleting a tasks.")
    to_do=input("    4-exit the program.\nChoose an option: ")
    if to_do=="1":
        tasks[x] = input("\nAdd a task please: \n")
        x+=1
    elif to_do=="2":
        if tasks:
            print("\nThe tasks is: ")
            for num, task in tasks.items():
                print(f"\n        {num}: {task}")
        else:
            print("\nNo tasks to see :) ")
    elif to_do=="3":
        if tasks:
            try:
                tasks_num=int(input("\nSelect the number of the task you want to delete it: "))
                tasks.pop(tasks_num)
                print("Tasks deleted successfully! ")
            except KeyError:
                print("\nIII! DELETE A REAL TASKS. \n")
        else:
            print("\nNO TASKS TO DELETE! \n")
        x-=1
    else:
        print("\n\ndon't forget to complete all the tasks <3\n")
        break

