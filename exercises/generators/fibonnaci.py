def gen_fibonacci(max_num: int):
    num_one, num_two = 0, 1
    while num_one <= max_num:
        yield num_one
        num_one, num_two = num_two, num_one + num_two


if __name__ == "__main__":
    for number in gen_fibonacci(100):
        print(number)
