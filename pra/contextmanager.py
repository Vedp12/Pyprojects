class openfile:
    def __init__(self, openfile, mode):
        self.openfile = openfile
        self.mode = mode

    def __enter__(self):
        self.file = open(self.openfile, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()


with open("sample.txt", "w") as Wi:
    Wi.write("Hello")
with open("sample.txt", "r") as Re:
    Re.read()
print(Wi.closed, Re.closed)
