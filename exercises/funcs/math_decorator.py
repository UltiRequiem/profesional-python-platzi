def calc_messages(func):
    def wrapper(x, y):
        print("Starting the calc.")

        print(func(x + 1, y + 1))

        print("Calc done!")

    return wrapper


@calc_messages
def suma(x: int, y: int) -> int:
    return x + y


if __name__ == "__main__":
    suma(12, 45)
