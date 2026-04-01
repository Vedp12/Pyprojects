def readfile(file_path):
    with open(file_path) as file:
        for line in file:
            yield line.strip()


file_path = "/home/tux_106/Documents/avengers.txt"
for line in readfile(file_path):
    print(line)
