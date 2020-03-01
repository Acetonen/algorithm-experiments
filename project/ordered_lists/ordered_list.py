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
                or node.next is not None and self._make_compare(new_node.value, node.next.value)  # pragma: no mutate
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


class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super().__init__(asc)

    @staticmethod
    def clean_from_start_spaces(string):
        for index, char in enumerate(string):
            if char != ' ':
                return string[index:]

    @staticmethod
    def clean_from_end_spaces(string):
        reverse_string = list(string)
        reverse_string.reverse()

        for index, char in enumerate(reverse_string):
            if char != ' ':
                return string[:-index] if index else string

    def clean_from_spaces(self, value):
        return self.clean_from_start_spaces(self.clean_from_end_spaces(value))

    def compare(self, value1: str, value2: str) -> int:
        value1 = self.clean_from_spaces(value1)
        value2 = self.clean_from_spaces(value2)

        return (value1 < value2 and -1) or (value1 > value2 and 1) or 0  # noqa
