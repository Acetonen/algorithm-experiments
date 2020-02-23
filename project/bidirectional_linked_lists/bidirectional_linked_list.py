class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None  # pragma: no mutate
        self.next = None  # pragma: no mutate


class LinkedList2:
    def __init__(self):
        self.head = None  # pragma: no mutate
        self.tail = None  # pragma: no mutate

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def find(self, val):
        node = self.head

        while node is not None:

            if node.value == val:
                return node

            node = node.next

    def find_all(self, val):
        result_list = list()
        node = self.head

        while node:
            if node.value == val:
                result_list.append(node)
            node = node.next

        return result_list

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):  # noqa
        length = 0
        node = self.head

        while node:
            length += 1
            node = node.next

        return length

    def _working_with_head_deletion(self, all_):  # pragma: no mutate
        if self.current_node.next:
            self.head = self.current_node.next
            self.head.prev = None
            self.current_node = self.current_node.next  # noqa

            if not all_:
                self.exit_cycle = True  # pragma: no mutate

        else:
            self.head = None
            self.tail = None
            self.exit_cycle = True  # noqa  # pragma: no mutate

    def _working_with_body_deletion(self, all_):
        self.current_node.prev.next = self.current_node.next

        if self.current_node.next:
            self.current_node.next.prev = self.current_node.prev
        else:
            self.tail = self.current_node.prev

        self.current_node = self.current_node.next  # noqa
        if not all_:
            self.exit_cycle = True  # noqa  # pragma: no mutate

    def delete(self, val, all_=False):
        self.current_node = self.head
        self.exit_cycle = False  # noqa  # pragma: no mutate

        while self.current_node and not self.exit_cycle:  # pragma: no mutate
            if self.current_node.value == val:
                if self.current_node.prev is None:
                    self._working_with_head_deletion(all_)
                else:
                    self._working_with_body_deletion(all_)
            else:
                self.current_node = self.current_node.next  # noqa

    def _insert_in_empty_list(self, new_node):
        self.head = new_node
        self.tail = new_node

    def _insert_in_tail(self, new_node):
        self.tail.next = new_node
        self.tail = new_node

    def _insert_in_body(self, after_node, new_node):
        node = self.head
        while node:
            if node == after_node:  # pragma: no mutate
                new_node.next = after_node.next
                new_node.prev = after_node
                after_node.next = new_node

                if self.tail is after_node:
                    self.tail = new_node

            node = node.next

    def insert(self, after_node, new_node):
        if not after_node and self.len() != 0:
            self._insert_in_tail(new_node)
        elif not after_node and self.len() == 0:
            self._insert_in_empty_list(new_node)
        else:
            self._insert_in_body(after_node, new_node)

    def add_in_head(self, new_node):
        if self.len():
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        else:
            self._insert_in_empty_list(new_node)
