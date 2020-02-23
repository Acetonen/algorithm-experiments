class HashTable:
    def __init__(self, size, step):
        self.size = size
        self.step = step
        self.slots = [None for _ in range(self.size)]

    def hash_fun(self, value):
        return hash(value) % self.size

    def seek_slot(self, value):
        index = self.hash_fun(value)

        for _ in range(self.size):
            if self.slots[index] is None:
                return index

            index += self.step
            index = index if index < self.size else index - self.size

    def put(self, value):
        index = self.seek_slot(value)
        if index is not None:
            self.slots[index] = value

        return index

    def find(self, value):
        index = self.hash_fun(value)

        for _ in range(self.size):
            if self.slots[index] == value:
                return index

            index += self.step
            index = index if index < self.size else index - self.size
