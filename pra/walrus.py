# no = [1,2,3,4,5]

# while(n:=len(no))>0:
#    print(no.pop())
name = []
name_list = list()
while (name_list := input("Enter the name: ")) != "q":
    name.append(name_list)
    for name1 in name:
        print(name1)
