import csv

with open("dict_users.csv", "w") as files:
    headers = ("first name", "last name", "Age")
    csv_writer = csv.DictWriter(files, fieldnames=headers)

    csv_writer.writeheader()
    data = (
        {"first name": "Tux", "last name": "official", "Age": 20},
        {"first name": "Ved", "last name": "Patel", "Age": 21},
        {"first name": "kayaan", "last name": "Patel", "Age": 13},
    )
    csv_writer.writerows(data)
with open("dict_users.csv", "r") as files:
    csv_reader = csv.DictReader(files)
    for row in csv_reader:
        print(row["first name"], row["last name"], row["Age"])
