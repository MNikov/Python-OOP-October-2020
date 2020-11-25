def cache(func):
    log = {}

    def wrapper(*args, **kwargs):
        if args not in log:
            res = func(*args, **kwargs)
            log[args] = res
            return res
        return log[args]

    wrapper.log = log
    return wrapper


# def cache(func): NOT WORKING AS EXPECTED
#     def wrapper(n):
#         value = func(n)
#         wrapper.log[n] = value
#         return value
#
#     wrapper.log = {}
#     return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(100)
print(fibonacci.log)
fibonacci(4)
print(fibonacci.log)
