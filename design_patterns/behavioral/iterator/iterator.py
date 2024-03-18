class RangeIterator:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        current = self.current
        self.current += 1
        return current


if __name__ == "__main__":
    range_iterator = RangeIterator(0, 10)
    for i in range_iterator:
        print(i)  # Outputs: 0 1 2 3 4 5 6 7 8 9
