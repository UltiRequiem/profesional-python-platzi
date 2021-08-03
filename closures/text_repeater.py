def make_repeater_off(num: int):
    def repeater(string: str) -> str:
        return f"{string} " * num

    return repeater


def run():
    repeat_five = make_repeater_off(5)
    print(repeat_five("Hello"))

    repeat_ten = make_repeater_off(10)
    print(repeat_ten("Howo"))


if __name__ == "__main__":
    run()
