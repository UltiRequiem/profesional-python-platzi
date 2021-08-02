class Fibonacci:
    def __init__(self, max_num):
        self.max_num = max_num

    def __iter__(self):
        self.num_one = 0
        self.num_two = 1
        self.counter = 0
        return self

    def __next__(self):
        if self.counter == 0:
            self.counter += 1
            return self.num_one
        elif self.counter == 1:
            self.counter += 1
            return self.num_two
        else:

            self.aux = self.num_one + self.num_two

            if self.aux >= self.max_num:
                raise StopIteration

            self.num_one, self.num_two = self.num_two, self.aux
            self.counter += 1
            return self.aux


def fibonacci_until(maximum: int) -> list[int]:
    return [num for num in Fibonacci(maximum)]


if __name__ == "__main__":
    print(fibonacci_until(4000))
