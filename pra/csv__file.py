import csv

# Write Operations
with open("./users.csv", "w") as file:
    csv_writer = csv.writer(file)
    headers = ("First Name", "Last name", "Age")
    data = (
        ("Ved", "Patel", 20),
        ("Kayaan", "Patel", 13),
        ("Rudra", "Patel", 19),
    )
    csv_writer.writerow(headers)
    csv_writer.writerows(data)

# Read Operations
with open("./users.csv") as file:
    csv_reader = csv.reader(file)
    data = list(csv_reader)
