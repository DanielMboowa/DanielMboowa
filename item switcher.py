import time

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
def hotbar():
    hotbar = [
        'torch',
        'sword',
        'rock',
        'potion',
        'shield',
    ]
    index = hotbar.index('shield')
    item = hotbar.pop(index)
    hotbar.insert(0, item)
hotbar()
