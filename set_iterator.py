
class BidirectionalIterator:
    def __init__(self, iterable: set):
        self.iterable = list(iterable)
        self.index = -1

    def next(self):
        if self.index < len(self.iterable) - 1:
            self.index += 1
            return self.iterable[self.index]
        raise StopIteration("no more items")

    def previous(self):
        if self.index > 0:
            self.index = -1
            return self.iterable[self.index]
        raise StopIteration("no previous items")