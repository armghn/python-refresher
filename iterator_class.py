class EvenNumbers:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        x = self.start
        self.start += 2
        return x


even = EvenNumbers(10, 20)
for n in even:
    print(n)