class NativeDictionary:
    def __init__(self, size):
        self.step = 3  # pragma: no mutate
        self.size = size  # pragma: no mutate
        self.slots = [None for _ in range(self.size)]  # pragma: no mutate
        self.values = [None for _ in range(self.size)]  # pragma: no mutate

    def hash_fun(self, key):
        return hash(key) % self.size

    def is_key(self, key):
        index = self.hash_fun(key)

        for _ in range(self.size):
            if self.slots[index] == key:
                return True

            index += self.step  # pragma: no mutate
            index = index if index < self.size else index - self.size

        return False

    def _seek_slot(self, key):
        index = self.hash_fun(key)

        for _ in range(self.size):
            if self.slots[index] is None or self.slots[index] == key:
                return index

            index += self.step  # pragma: no mutate
            index = index if index < self.size else index - self.size

    def put(self, key, value):
        index = self._seek_slot(key)

        if index is not None:
            self.slots[index] = key
            self.values[index] = value

        return index

    def get(self, key):
        index = self.hash_fun(key)

        for _ in range(self.size):
            if self.slots[index] == key:
                return self.values[index]

            index += self.step
            index = index if index < self.size else index - self.size
