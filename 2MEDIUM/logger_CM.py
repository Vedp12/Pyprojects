from contextlib import contextmanager


class Logger:
    def __init__(self, filename, mode="w"):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print("Log started")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type == True:
            print(f"error:{exc_value}")
        self.file.close()
        print("Log ended")


with Logger("log.txt") as log:
    log.write("Start\n")
    log.write("Processing...\n")
