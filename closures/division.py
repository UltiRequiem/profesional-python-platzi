def make_divisor_by(num: int):
    """
    Returns a function returns the division of x  by n
    """

    def divisor(x: int) -> int:
        return x // num

    return divisor


def run() -> None:
    divisor_by_10 = make_divisor_by(10)

    print(divisor_by_10(99))
    print(divisor_by_10(100))


if __name__ == "__main__":
    run()
