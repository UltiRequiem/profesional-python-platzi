from datetime import datetime as dt


def execution_time(func):
    def wrapper(*args, **kwargs):
        init = dt.now()
        func(*args, **kwargs)
        final = dt.now()
        print(f"Total execution time is {final - init} seconds.")

    return wrapper


@execution_time
def test_execution_time():
    for _ in range(100000):
        pass


@execution_time
def test_sum(a: int, b: int) -> int:
    return a + b


@execution_time
def say_hi(name: str = "Zero") -> str:
    return f"Hi {name}!"


if __name__ == "__main__":
    test_execution_time()
    test_sum(5, 5)
    say_hi()
    say_hi("Susaku")
