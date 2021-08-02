def my_gen():
    print("Hello, world!")
    n = 0
    yield n

    print("Hello heaven!")
    n = 1
    yield n

    print("Hello hell!")
    n = 2
    yield n


my_gen_instance = my_gen()

while True:
    try:
        print(next(my_gen_instance))
    except StopIteration:
        break
