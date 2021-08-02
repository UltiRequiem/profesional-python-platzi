def upper_case_first_param(func):
    def wrapper(text):
        return func(text.upper())

    return wrapper


@upper_case_first_param
def recibed_a_msg(name: str) -> str:
    return f"{name}, you has received a message."


@upper_case_first_param
def uppercase(msg: str) -> str:
    return msg


if __name__ == "__main__":
    print(recibed_a_msg("Cesar"))
    print(uppercase("hello world!"))
