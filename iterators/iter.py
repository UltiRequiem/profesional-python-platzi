my_iterable = iter(range(1, 5 + 1))

while True:
    try:
        element = next(my_iterable)
        print(element)
    except StopIteration:
        break
