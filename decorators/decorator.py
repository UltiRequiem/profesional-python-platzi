def decorator(func):
    def wrapper():
        print("Decoring")
        func()
        print("Done!")

    return wrapper


@decorator
def say_hi():
    print("Hi!")


if __name__ == "__main__":
    say_hi()
