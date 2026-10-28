from time import time


def timer_func(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f"Function {func.__name__!r} executed in {(t2-t1):.4f}s")
        return result
    return wrapper


@timer_func
def create_list(n):
    return list(range(1, n+1))


create_list(1_000_000)