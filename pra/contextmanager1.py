from contextlib import contextmanager


@contextmanager
def openfile(filename, mode):
    f = open(filename, mode)
    yield f
    f.close()


with openfile("sample.txt", "w") as f:
    f.write("Hello")
print(f.closed)
