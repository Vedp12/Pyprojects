# context manger

import time
from contextlib import contextmanager

"""
# @contextmanager
class Timer:
    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_value, traceback):
        end = time.time()
        print(f"Execution time beteen {end - self.start:.4f} seconds")


with Timer():
    total = 0
    for i in range(100000):
        total += i
"""


@contextmanager
def Timer():
    start = time.time()
    yield
    end = time.time()
    print(f"{end - start:.4f}")


with Timer():
    for i in range(1000000):
        pass
