from time import time
from functools import wraps


def timer_func(func):
    @wraps(func)    # Preserves the original function's metadata, not its behavior.
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f"Function {func.__name__!r} executed in {(t2-t1):.4f}s")
        return result
    return wrap_func


@timer_func
def long_time(n):
    for i in range(n):
        for j in range(100000):
            i*j


long_time(5)
long_time(50)
long_time(500)
print(long_time.__name__)
