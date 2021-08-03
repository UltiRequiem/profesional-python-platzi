def remove_duplicates(lst: list | tuple) -> list:
    return list(set(lst))


def remove_duplicates_test():
    my_lst = [1, 1, 1, 1, 1, 2, 2, 2, 3, 3]
    print(f"Old list: {my_lst} / Filtered list: {remove_duplicates(my_lst)}")


if __name__ == "__main__":
    remove_duplicates_test()
