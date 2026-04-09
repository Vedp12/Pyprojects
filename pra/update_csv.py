import csv

with open("users.csv") as files:
    csv_reader = csv.DictReader(files)
    data = list(csv_reader)

    header = ["first name", "last name", "Age"]

with open("users.csv", "w", newline="") as files:
    csv_writer = csv.DictWriter(
        files,
        fieldnames=header,
    )
    csv_writer.writeheader()
    for row in data:
        if row["first name"] == "Tux":
            row["Age"] = 22
        csv_writer.writerow(row)
