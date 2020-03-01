# noinspection DuplicatedCode
class HashTable:
    def __init__(self, size, step):
        self.table_size = size  # pragma: no mutate
        self.step = step  # pragma: no mutate
        self.slots = [None for _ in range(self.table_size)]  # pragma: no mutate

    def hash_fun(self, value):
        result = 0
        constant = 17  # pragma: no mutate

        for char in str(value):
            result = (result * constant + ord(char)) % self.table_size

        return result

    def get_from_slots(self, index):
        return self.slots[index]

    def put(self, value):
        index = self.seek_slot(value)
        if index is not None:
            self.slots[index] = value

        return index

    def find(self, value):
        index = self.hash_fun(value)  # pragma: no mutate

        for _ in range(self.table_size):  # pragma: no mutate
            if self.get_from_slots(index) == value:  # pragma: no mutate
                return index

            index += self.step  # pragma: no mutate
            index = index if index < self.table_size else index - self.table_size  # pragma: no mutate


DEFAULT_STEP = 3  # pragma: no mutate
DEFAULT_SIZE = 20000  # pragma: no mutate


class PowerSet(HashTable):
    def __init__(self):
        super().__init__(DEFAULT_SIZE, DEFAULT_STEP)

    def size(self):
        set_size = 0
        for item in self.slots:
            if item is not None and item is not False:
                set_size += 1

        return set_size

    def seek_slot(self, value):
        index = self.hash_fun(value)

        for _ in range(self.table_size):
            if self.get_from_slots(index) == value or self.get_from_slots(index) is None:  # pragma: no mutate
                return index

            index += self.step
            index = index if index < self.table_size else index - self.table_size

    def find_value(self, value, remove=False):
        index = self.hash_fun(value)
        result = False

        for _ in range(self.table_size):

            if self.get_from_slots(index) == value:

                if remove:
                    self.slots[index] = False  # noqa

                result = True
                break  # pragma: no mutate

            elif self.get_from_slots(index) is None:  # pragma: no mutate
                break  # pragma: no mutate

            index += self.step  # pragma: no mutate
            index = index if index < self.table_size else index - self.table_size  # pragma: no mutate

        return result

    # noinspection DuplicatedCode
    def get(self, value):
        return self.find_value(value)

    def remove(self, value):
        return self.find_value(value, remove=True)

    def intersection(self, set2):
        results_set = PowerSet()

        for element in self.slots:
            if element is not None and set2.get(element) is True:
                results_set.put(element)  # noqa

        return results_set

    def union(self, set2):
        results_set = PowerSet()

        for element in self.slots + set2.slots:
            results_set.put(element)  # noqa

        return results_set

    def difference(self, set2):
        results_set = PowerSet()

        for element in self.slots:
            if element is not None and set2.get(element) is False:
                results_set.put(element)  # noqa

        return results_set

    def issubset(self, set2):
        for element in set2.slots:
            if element is not None and self.get(element) is False:
                return False

        return True
