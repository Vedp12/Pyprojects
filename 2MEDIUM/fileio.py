print("1. Create Task\n2. View Task\n3. Delete task\n4. delete whole data \n *. exit")
User_task = int(input("Enter a Operation no to perform:"))

match User_task:
    case 1:     #^ Write
        with open('file.txt','a') as file:
            write_task = input("\n\nEnter a task: ")
            file.write(f"- {write_task}\n")
    
    case 2:
         with open('file.txt','r') as file:
             print(file.read())
        
    case 3:
        line_to_delete = int(input("Enter a number of line to delete: "))
        
        with open('file.txt','r') as file:
            lines = file.readlines()
        
        with open('file.txt','w') as file:
            for i, lines in enumerate(lines):
                if i != (line_to_delete - 1):
                    file.write(lines) 
    case 4:
        with open("file.txt","w") as file:
            file.write()
    case _:
        print("exit")