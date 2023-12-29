import time


class Cached:
    def __init__(self, function):
        self.cache = {}
        self.function = function

    def __call__(self, *args, **kwargs):
        key = str(args) + str(kwargs)
        if key in self.cache:
            return self.cache[key]

        value = self.function(*args, **kwargs)
        self.cache[key] = value
        return value


def fib_no_cache(n: int) -> int:
    if n <= 2:
        return 1
    else:
        return fib_no_cache(n - 1) + fib_no_cache(n - 2)


@Cached
def fib(n: int) -> int:
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    start = time.time()
    first = fib(40)
    end = time.time()
    print(f"result with cache: {first}, time: {end - start}")
    start = time.time()
    second = fib_no_cache(40)
    end = time.time()
    print(f"result without cache: {second}, time: {end - start}")
