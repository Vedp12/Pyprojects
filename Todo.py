Todos = []
while True:
    userno = int(input("\nEnter the number \n1. Add \n2. Remove \n3. Display "))
    match userno:

        case 1:
            while True:
                User_list = input("\nEnter Today's ToDo: ")
                if User_list != "e":
                    Todos.append(User_list)
                else:
                    break

        case 2:
            input_pop = int(input("\nEnter the no who you want to delete"))
            Todos.pop(input_pop)

        case 3:
            for no, Todo in enumerate(Todos):
                print(f"  {no+1}. {Todo}", end="")
        # print()

        case _:
            break
