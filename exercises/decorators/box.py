from sys import argv


def wrap(func):
    def wrapper(txt: str = "Chec tha docs on https://github.com/UltiRequiem/boxie"):
        print(" " + "_" * (len(txt) + 1))
        print("/" + "_" * len(txt) + "/|")
        print("|" + " " * len(txt) + "||")
        func("|" + txt + "||")
        print("|" + "_" * len(txt) + "|/")

    return wrapper


@wrap
def print_console(txt):
    print(txt)


def run():
    print_console(argv[1])


if __name__ == "__main__":
    run()
