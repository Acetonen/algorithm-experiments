import ctypes


class DynArray:
    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, index):
        if index < 0 or index >= self.count:
            raise IndexError('Index is out of bounds')

        return self.array[index]

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)

        for index in range(self.count):
            new_array[index] = self.array[index]

        self.array = new_array
        self.capacity = new_capacity

    def append(self, element):
        self._check_for_increase_size()

        self.array[self.count] = element
        self.count += 1

    def _check_index_range(self, index):
        if index < 0 or index > self.count:
            raise IndexError('Index is out of bounds')

    def _check_for_append(self, element, index):
        if index == self.count:
            self.append(element)
            return True

    def _check_for_increase_size(self):
        if self.count == self.capacity:
            self.resize(2 * self.capacity)

    def _check_for_reduce_size(self):
        if self.count < self.capacity / 2:
            new_capacity = self.capacity // 1.5 if self.capacity // 1.5 > 16 else 16
            self.resize(int(new_capacity))

    def insert(self, element, index):
        self._check_index_range(index)
        if self._check_for_append(element, index):
            return

        self._check_for_increase_size()

        tail = [self[i] for i in range(index, self.count)]
        self.array[index] = element
        self.count = index + 1

        for item in tail:
            self.append(item)

    def delete(self, index):
        self[index]  # Check out of range index

        tail = [self[i] for i in range(index + 1, self.count)]
        self.count = index

        for item in tail:
            self.append(item)

        self._check_for_reduce_size()