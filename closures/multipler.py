def make_multipler(x: int):
    def multipler(n: int) -> int:
        return x * n

    return multipler


times_10 = make_multipler(10)
times_4 = make_multipler(4)

print(times_10(10))
print(times_4(10))
