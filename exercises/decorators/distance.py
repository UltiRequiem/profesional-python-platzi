import math


def get_distance_manhattan(func):
    def wrapper(*args, **kwargs) -> None:
        func(*args, **kwargs)
        print(
            f"The distance of Manhattan is {(args[0] - args[2]) - (args[1] - args[3])}."
        )

    return wrapper


@get_distance_manhattan
def get_distance_euclidean(x1: int, y1: int, x2: int, y2: int) -> None:
    print(f"The distance of Euclidean is {math.sqrt(((x1-x2)**2) + (y1-y2)**2)}")


def run():
    get_distance_euclidean(5, 2, 4, 7)


if __name__ == "__main__":
    run()
