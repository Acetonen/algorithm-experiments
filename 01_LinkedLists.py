class Node:

    def __init__(self, v):
        self.value = v
        self.next = None

    def __repr__(self):
        return 'Node value: {}'.format(self.value)


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node:
            print(node.value, end=' ')
            node = node.next

        print(
            "\nhead: {} tail: {}".format(
                getattr(self.head, 'value', None), getattr(self.tail, 'value', None)
            )
        )

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

    def working_with_head_deletion(self):
        if self.current_node.next:
            self.head = self.current_node.next
            self.current_node = self.current_node.next  # noqa

            if not all:
                self.exit_cycle = True

        else:
            self.head = None
            self.tail = None
            self.exit_cycle = True  # noqa

    def delete(self, val, all=False):  # noqa
        self.prev_node = None
        self.current_node = self.head
        self.exit_cycle = False

        while self.current_node and not self.exit_cycle:
            if self.current_node.value == val:
                if not self.prev_node:
                    self.working_with_head_deletion()

                else:
                    self.prev_node.next = self.current_node.next
                    self.current_node = self.current_node.next
                    if not all:
                        self.exit_cycle = True  # noqa
            else:
                self.prev_node = self.current_node  # noqa
                self.current_node = self.current_node.next  # noqa

            if not self.current_node:
                self.tail = self.prev_node

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        length = 0
        node = self.head

        while node:
            length += 1
            node = node.next

        return length

    def insert(self, after_node, new_node):
        if not after_node:
            new_node.next = self.head
            self.head = new_node

            if not self.tail:
                self.tail = new_node
        else:
            node = self.head
            while node:
                if node == after_node:
                    new_node.next = after_node.next
                    after_node.next = new_node

                    if self.tail is after_node:
                        self.tail = new_node

                node = node.next