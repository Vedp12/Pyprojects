import csv
import datetime

list_1 = []
while True:
    try:
        user = int(input("enter value="))
    except ValueError:
        print("value is wrong")
        continue
    match user:
        case 1:
            add_1 = input("enter task")
            list_1.append(f"{add_1}")

        case 2:
            try:
                delete_1 = int(input("delete task"))
            except ValueError:
                print("value is wrong")
                continue
            list_1.pop(delete_1)

        case 3:
            print(list_1)
            with open("task.csv", "w") as file:
                csv_writer = csv.writer(file)
                headers = ["numbers", "task", "datetime"]
                csv_writer.writerow(headers)
                for enu, i in enumerate(list_1):
                    print("data is storing")
                    csv_writer.writerow([enu + 1, i, datetime.datetime.now()])

        case 4:
            print(list_1)
            with open("task.csv", "r") as file:
                csv_reader = csv.reader(file)
                print(csv_reader)
                for i in csv_reader:
                    print(i)
        case 5:
            break
