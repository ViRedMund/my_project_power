import time

n = input()

def time_check(amount_time):
    def inner(func):
        def wrapper(*args, **kwargs):
            time_start = time.perf_counter()
            time.sleep(amount_time)
            res = time_start - time.perf_counter()
            print(res, func(*args, **kwargs))
            return func(*args, **kwargs)
        return wrapper
    return inner


@time_check(5)
def pow(x, y):
    res = x**y
    return res



pow(8, 3)