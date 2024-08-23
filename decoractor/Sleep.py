import functools
import time


def Sleep(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        time.sleep(0.25)
        func(*args, **kwargs)
        time.sleep(0.25)

    return wrapper
