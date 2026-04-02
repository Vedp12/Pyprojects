import os
from contextlib import contextmanager


@contextmanager
def change_dir(dis):
    try:
        cwd = os.getcwd()
        os.chdir(dis)
        yield
    finally:
        os.chdir(cwd)


with change_dir("OOP"):
    print(os.listdir())
