def gen_by_2(max_num: int):
    return (x * 2 for x in range(1, max_num + 1))


my_gen_instance = gen_by_2(10)

while True:
    try:
        print(next(my_gen_instance))
    except StopIteration:
        break
