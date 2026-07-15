import csv

with open("updated.csv", "r") as csvs:
    csv_reader = csv.reader(csvs)

    with open("new_mail.csv", "w") as new_writer_csv:
        csv_writer = csv.writer(new_writer_csv, delimiter="-")

        for line in csv_reader:
            csv_writer.writerow(line)
            # print(cl)
