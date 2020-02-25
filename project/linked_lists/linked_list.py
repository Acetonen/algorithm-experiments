class Node:
    def __init__(self, value):
        self.value = value
        self.next = None  # pragma: no mutate


class LinkedList:
    def __init__(self):
        self.head = None  # pragma: no mutate
        self.tail = None  # pragma: no mutate

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        result_list = list()
        node = self.head

        while node:
            if node.value == val:
                result_list.append(node)
            node = node.next

        return result_list

    def working_with_head_deletion(self, all_):
        if self.current_node.next:
            self.head = self.current_node.next
            self.current_node = self.current_node.next  # noqa

            if not all_:
                self.exit_cycle = True  # pragma: no mutate

        else:
            self.head = None
            self.tail = None
            self.exit_cycle = True  # noqa  # pragma: no mutate

    def delete(self, val, all_=False):  # noqa
        self.prev_node = None
        self.current_node = self.head
        self.exit_cycle = False  # pragma: no mutate

        while self.current_node and not self.exit_cycle:  # pragma: no mutate
            if self.current_node.value == val:
                if self.prev_node is None:
                    self.working_with_head_deletion(all_)

                else:
                    self.prev_node.next = self.current_node.next
                    self.current_node = self.current_node.next
                    if not all_:
                        self.exit_cycle = True  # noqa
            else:
                self.prev_node = self.current_node  # noqa
                self.current_node = self.current_node.next  # noqa

            if not self.current_node:
                self.tail = self.prev_node

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

    def _insert_in_tail(self, new_node):
        new_node.next = self.head
        self.head = new_node

        if not self.tail:
            self.tail = new_node

    def _insert_in_body(self, new_node, after_node):
        node = self.head
        while node:
            if node == after_node:  # pragma: no mutate
                new_node.next = after_node.next
                after_node.next = new_node

                if self.tail is after_node:
                    self.tail = new_node

            node = node.next

    def insert(self, after_node, new_node):
        if after_node is None:
            self._insert_in_tail(new_node)
        else:
            self._insert_in_body(new_node, after_node)
