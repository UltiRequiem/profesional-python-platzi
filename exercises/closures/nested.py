def printer(msg):
    def nested():
        print(msg)

    return nested


if __name__ == "__main__":
    my_printer = printer("Hi!")
    my_printer()
