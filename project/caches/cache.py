COMPARE_DICT = {  # noqa
    -1: True,
    1: False,
    0: 'equal',  # pragma: no mutate
}


class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None  # pragma: no mutate
        self.next = None  # pragma: no mutate


class OrderedList:
    def __init__(self, asc):
        self.head = None  # pragma: no mutate
        self.tail = None  # pragma: no mutate
        self.__ascending = asc

    @property
    def ascending(self):
        return self.__ascending

    @staticmethod  # pragma: no mutate
    def compare(value1, value2):
        return (value1 < value2 and -1) or (value1 > value2 and 1) or 0  # noqa

    @staticmethod  # pragma: no mutate
    def compare_stas(value1, value2):
        return (value1 - value2) / (abs(value1 - value2) or True)

    @staticmethod  # pragma: no mutate
    def compare_shortest(value1, value2):
        return 0 if value1 == value2 else (-1, 1)[value1 > value2]  # pragma: no mutate

    def _add_in_empty_list(self, new_node):
        self.head = new_node
        self.tail = new_node

    def _add_in_head(self, new_node):
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def _check_tail(self, new_node):
        if new_node.next is None:
            self.tail = new_node

    def _make_compare(self, value1, value2) -> bool:
        compare_result = COMPARE_DICT[self.compare_stas(value1, value2)]

        return compare_result == self.__ascending

    def _insert_between_two_nodes(self, node, new_node):
        new_node.next = node.next
        if node.next is not None:
            node.next.prev = new_node
        node.next = new_node
        new_node.prev = node
        self._check_tail(new_node)

    def _add_in_body(self, new_node):
        node = self.head

        while node:
            if (
                self._make_compare(node.value, new_node.value) and node.next is None
                or node.next is not None and self._make_compare(new_node.value, node.next.value)
            ):
                self._insert_between_two_nodes(node, new_node)
                break  # pragma: no mutate

            node = node.next

    def add(self, value):
        new_node = Node(value)

        if self.len() == 0:
            self._add_in_empty_list(new_node)
        elif self._make_compare(new_node.value, self.head.value):
            self._add_in_head(new_node)
        else:
            self._add_in_body(new_node)

    def find(self, val):
        node = self.head

        while node is not None:

            if node.value == val:
                return node
            elif not self._make_compare(node.value, val):
                return

            node = node.next

    def _working_with_head_deletion(self):
        if self.current_node.next:
            self.head = self.current_node.next
            self.head.prev = None

        else:
            self.head = None
            self.tail = None

    def _working_with_body_deletion(self):
        self.current_node.prev.next = self.current_node.next

        if self.current_node.next:
            self.current_node.next.prev = self.current_node.prev
        else:
            self.tail = self.current_node.prev

    def delete(self, val):  # noqa
        self.current_node = self.head

        while self.current_node:
            if self.current_node.value == val:
                if self.current_node.prev is None:
                    self._working_with_head_deletion()
                else:
                    self._working_with_body_deletion()
                break  # pragma: no mutate
            else:
                self.current_node = self.current_node.next  # noqa

    def clean(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def len(self):  # noqa
        length = 0
        node = self.head

        while node:
            length += 1
            node = node.next

        return length

    def get_all(self):
        result = []
        node = self.head

        while node is not None:
            result.append(node)
            node = node.next

        return result


# noinspection DuplicatedCode
class NativeDictionary:
    def __init__(self, size):
        self.step = 3  # pragma: no mutate
        self.size = size  # pragma: no mutate
        self.slots = [None for _ in range(self.size)]  # pragma: no mutate
        self.values = [None for _ in range(self.size)]  # pragma: no mutate

    def hash_fun(self, value):
        result = 0
        constant = 17  # pragma: no mutate

        for char in str(value):
            result = (result * constant + ord(char)) % self.size

        return result

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


class NativeCache(NativeDictionary):
    def __init__(self, size):
        super().__init__(size)
        self.hits = [0 for _ in range(self.size)]  # pragma: no mutate
        self.hits_mapping = NativeDictionary(self.size)
        self.hits_order = OrderedList(True)

    def _remove_element_index_from_hits_mapping(self, index):
        if self.hits[index] > 1:
            mapping_set = self.hits_mapping.get(self.hits[index] - 1)
            mapping_set.remove(index)  # noqa

            if not mapping_set:
                self.hits_order.delete(self.hits[index] - 1)

    def _add_element_to_hits_mapping(self, index, mapping_set):
        mapping_set.append(index)  # noqa
        self.hits_mapping.put(self.hits[index], mapping_set)
        self.hits_order.add(self.hits[index])

    def _def_count_hits(self, index: int):
        """Use count_mapping - NativeDictionaries where keys are hits and values are lists of element indexes."""
        self.hits[index] += 1
        mapping_set = self.hits_mapping.get(self.hits[index])

        if not mapping_set:
            mapping_set = list()

        # Add element to hits_mapping:

        self._add_element_to_hits_mapping(index, mapping_set)
        self._remove_element_index_from_hits_mapping(index)

    def _remove_most_unpopular_element(self):
        if self.hits_order.len():
            minimal_count = self.hits_order.head.value
            minimal_count_list = self.hits_mapping.get(minimal_count)
            index = minimal_count_list.pop()
            if not minimal_count_list:
                self.hits_order.delete(minimal_count)
        else:
            index = 0

        self.hits[index] = 0

        return index

    def get(self, key):
        index = self.hash_fun(key)

        for _ in range(self.size):

            if self.slots[index] == key:
                self._def_count_hits(index)

                return self.values[index]

            elif self.slots[index] is None:
                break

            index += self.step
            index = index if index < self.size else index - self.size

    def put(self, key, value):
        index = self._seek_slot(key)

        if index is None:
            index = self._remove_most_unpopular_element()

        self.slots[index] = key
        self.values[index] = value

        return index
