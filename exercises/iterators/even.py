class EvenNumbers:
    def __init__(self, max_num=None, min_num=None):
        self.max = max_num
        self.min = min_num

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        if not self.max or self.num <= self.max:
            self.num += 2
            return self.num - 2
        else:
            raise StopIteration
