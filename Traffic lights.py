import time
from itertools import cycle
def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f'Execution time for {func.__name__}: {execution_time:.8f} seconds')
        return result
    return wrapper


@timeit
lights = [
    ('Green',3),
    ('Yellow',1.5),
    ('Red',3),
]
colors = cycle(lights)
for i in range(2):
    while True:
        c,s = next(colors)
        print(c)
        time.sleep(s)