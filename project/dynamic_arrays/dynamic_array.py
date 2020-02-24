import ctypes

REDUCE_COEFFICIENT = 1.5
MINIMAL_CAPACITY = 16


class DynArray:
    def __init__(self):
        self.count = 0
        self.capacity = MINIMAL_CAPACITY
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    def __getitem__(self, index):
        if index < 0 or index >= self.count:
            raise IndexError('Index is out of bounds')  # pragma: no mutate

        return self.array[index]

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

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
            raise IndexError('Index is out of bounds')  # pragma: no mutate

    def _check_for_append(self, element, index):
        if index == self.count:
            self.append(element)
            return True

    def _check_for_increase_size(self):
        if self.count == self.capacity:
            self.resize(2 * self.capacity)

    def _check_for_reduce_size(self):
        if self.count < self.capacity / 2:
            reduced_size = int(self.capacity / REDUCE_COEFFICIENT)
            new_capacity = reduced_size if reduced_size >= MINIMAL_CAPACITY else MINIMAL_CAPACITY  # pragma: no mutate
            self.resize(new_capacity)

    def insert(self, index, element):
        self._check_index_range(index)
        if self._check_for_append(element, index):
            return

        self._check_for_increase_size()

        tail = [self[ind] for ind in range(index, self.count)]
        self.array[index] = element
        self.count = index + 1

        for array_item in tail:
            self.append(array_item)

    def delete(self, index):
        # Check out of range index
        self[index]  # noqa

        tail = [self[ind] for ind in range(index + 1, self.count)]
        self.count = index

        for array_item in tail:
            self.append(array_item)

        self._check_for_reduce_size()
