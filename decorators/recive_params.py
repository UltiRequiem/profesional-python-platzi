def with_custom_msg(msg):
    def with_msg(func):
        print(f"{msg}")

        def wrapper(*args, **kwargs):
            func(*args, **kwargs)

        return wrapper

    return with_msg


@with_custom_msg("Hello!")
def multiply(a: int, b: int):
    print(f"The result of {a} * {b} is {a*b}.")


if __name__ == "__main__":
    multiply(10, 2)
