from functools import lru_cache
import time

@lru_cache(maxsize=None)
def user(name, id):
    time.sleep(3)
    if id % 2 == 0:
        return f"{name}\nID is recognised as {id}"
    else:
        return f"{name}\n{id}"

# Print the returned value
print(user("ved", 10))
print(user("kay", 13))
print(user("ved", 10))  # Instant, prints cached result
print(user("kay", 13))  # Instant, prints cached result
