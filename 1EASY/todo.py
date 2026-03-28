Task_list = []
while True:
    Task = int(input("1.Add 2.Delete 3.View = "))
       
    
    if Task == 1:
        Todo = input("Enter today's task : ")
        Task_list.append(Todo)
        print(Task_list)
    elif Task == 2:
        if Task_list!=0:
            remove1 = int(input("Remove item by no:"))
            Task_list.pop(remove1)
        else:
            print("List is empty")
            break
        
    elif Task == 3:
        for Task_list in Task_list:
            print(Task_list)
    else:
            break

