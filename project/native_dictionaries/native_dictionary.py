class NativeDictionary:
    def __init__(self, size):
        self.size = size
        self.slots = [None for _ in range(self.size)]
        self.values = [None for _ in range(self.size)]

    def _increase_size(self):
        self.slots.append(None)
        self.values.append(None)
        self.size += 1

        return self.size - 1

    def _find_exists_key_index(self, key):
        for index in range(self.size):
            if self.slots[index] == key:
                return index

    def _return_index(self, key):
        for index in range(self.size):
            if self.slots[index] is None:
                return index

    def hash_fun(self, key):
        index = self._find_exists_key_index(key)

        if index:
            return index

        index = self._return_index(key)

        if index:
            return index

        return self._increase_size()

    def is_key(self, key):
        for slot in self.slots:
            if key == slot:
                return True

        return False

    def put(self, key, value):
        index = self.hash_fun(key)
        self.values[index] = value

    def get(self, key):
        if self.is_key(key):
            return self.values[self.hash_fun(key)]
