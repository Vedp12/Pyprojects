import csv

print("1.add, 2.edit, 3.view, 4.exit")
choice = int(input("Enter the choice: "))

match choice:
    case 1:
        print("\n-----ADD DATA-----\n")
        with open("expense.csv", "a") as file:
            header = ("No", "Date", "Amount", "Category")
            csv_writer = csv.DictWriter(file, fieldnames=header)
            No0 = int(input("Enter Number : "))
            Date1 = input("Enter Date : ")
            Amount2 = int(input("Enter Amount : "))
            Category3 = input("Enter Category : ")
            data = {
                "No": No0,
                "Date": Date1,
                "Amount": Amount2,
                "Category": Category3,
            }
            csv_writer.writerow(data)
    case 2:
        header = ["No", "Date", "Amount", "Category"]
        print("\n-----EDIT DATA-----\n")
        with open("expense.csv", "r") as file:
            csv_reader = csv.DictReader(file)
            data = list(csv_reader)
            user_no = int(input("Enter no to which you want to edit "))
            for row in data:
                if row["No"] == user_no:
                    choice_field = int(
                        input(
                            "\nWhat field you want to edit?\n 1. No, 2. Date, 3. Amount, 4. Category"
                        )
                    )
                    choice_data = input("Enter new value: ")
                    if choice_field == 1:
                        row["No"] = choice_data
                    elif choice_field == 2:
                        row["Date"] = choice_data
                    elif choice_field == 3:
                        row["Amount"] = choice_data
                    elif choice_field == 4:
                        row["Category"] = choice_data

        with open("expense.csv", "w", newline="") as file:
            csv_editor = csv.DictWriter(file, fieldnames=header)
            csv_editor.writerow(data)
            print("\nData updated successfully!")

    case 3:
        print("\n-----VIEW DATA -----\n")
        with open("expense.csv", "r") as files:
            csv_reader = csv.reader(files)
            for row in csv_reader:
                print(row)

    case 4:
        print("\n-----Programmed exited-----\n")

    case _:
        pass
"""

l1 = [1, 2, 3, 4, 5]
l2 = [2, 3, 4, 5, 6]
l3 = [5, 6, 7, 8, 9]
l4 = [4, 2, 5, 2, 7]

for ql1, ql2, ql3, ql4 in zip(l1, l2, l3, l4):
    print(ql1, ql2, ql3, ql4)
"""
