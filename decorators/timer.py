from datetime import datetime as dt


def execution_time(func):
    def wrapper(*args, **kwargs):
        init = dt.now()
        func(*args, **kwargs)
        final = dt.now()
        print(f"Total execution time of {func.__name__} is {final - init} seconds.")

    return wrapper


@execution_time
def test_execution_time(times: int = 10, i: int = 0, mount: int = 1):
    for _ in range(times):
        i += mount + _


@execution_time
def test_sum(a: int = 5, b: int = 5) -> int:
    return a + b


@execution_time
def say_hi(name: str = "Zero") -> str:
    return f"Hi {name}!"


if __name__ == "__main__":
    test_execution_time(10000)
    test_sum(5, 5)
    say_hi()
