url = input("enter your url: ")
a = []
for i in url:
    print(i)
    if i == "?":
        break
    a.append(i)

with open("url.txt", "w") as file:
    file.write("".join(a))
