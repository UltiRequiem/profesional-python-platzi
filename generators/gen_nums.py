def num_generators(max_num: int):
    for num in range(1, max_num):
        yield num


my_nums = num_generators(10)

while True:
    try:
        print(next(my_nums))
    except StopIteration:
        break
