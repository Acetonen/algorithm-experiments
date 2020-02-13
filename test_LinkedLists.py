import unittest

from linked_list import LinkedList, Node


class TestLinkedList(unittest.TestCase):
    @staticmethod
    def get_linked_list(list_of_numbers):
        linked_list = LinkedList()

        for node in [Node(number) for number in list_of_numbers]:
            linked_list.add_in_tail(node)

        return linked_list

    @staticmethod
    def get_node_values_list(linked_list):
        result_list = list()
        node = linked_list.head
        while node:
            result_list.append(node.value)
            node = node.next

        return result_list

    def test_len(self):
        linked_list = self.get_linked_list(list(range(5)))
        self.assertEqual(linked_list.len(), 5)

    def test_delete_empty_list(self):
        linked_list = self.get_linked_list(list())
        linked_list.delete(2)
        linked_list.delete(2, True)

        self.assertEqual(linked_list.head, None)
        self.assertEqual(linked_list.tail, None)
        self.assertEqual(linked_list.len(), 0)

    def test_delete_all_two(self):
        linked_list = self.get_linked_list([2, 3, 2, 4, 2, 5])
        linked_list.delete(2, True)

        self.assertEqual(linked_list.len(), 3)

    def test_delete_all_two_to_empty(self):
        linked_list = self.get_linked_list([2, 2, 2])
        linked_list.delete(2, True)

        self.assertEqual(linked_list.len(), 0)
        self.assertEqual(linked_list.head, None)
        self.assertEqual(linked_list.tail, None)

    def test_delete_one_value_list(self):
        linked_list = self.get_linked_list([2])
        linked_list.delete(2)

        self.assertEqual(linked_list.head, None)
        self.assertEqual(linked_list.tail, None)
        self.assertEqual(linked_list.len(), 0)

    def test_delete_first_value_in_two_value_list(self):
        linked_list = self.get_linked_list([2, 1])
        linked_list.delete(2)

        self.assertEqual(linked_list.head.value, 1)
        self.assertEqual(linked_list.tail.value, 1)
        self.assertEqual(linked_list.head.next, None)
        self.assertEqual(linked_list.tail.next, None)
        self.assertEqual(linked_list.len(), 1)

    def test_delete_second_value_in_two_value_list(self):
        linked_list = self.get_linked_list([2, 1])
        linked_list.delete(1)

        self.assertEqual(linked_list.head.value, 2)
        self.assertEqual(linked_list.tail.value, 2)
        self.assertEqual(linked_list.head.next, None)
        self.assertEqual(linked_list.tail.next, None)
        self.assertEqual(linked_list.len(), 1)

    def test_clean(self):
        linked_list = self.get_linked_list(list(range(5)))
        self.assertEqual(linked_list.len(), 5)
        linked_list.clean()
        self.assertEqual(linked_list.head, None)
        self.assertEqual(linked_list.tail, None)
        self.assertEqual(linked_list.len(), 0)

    def test_find_all(self):
        linked_list = self.get_linked_list([1, 2, 3, 4, 2])
        all_two = linked_list.find_all(2)
        self.assertEqual(len(all_two), 2)
        self.assertEqual(all_two[0].value, 2)
        self.assertEqual(all_two[1].value, 2)

    def test_find_all_but_none(self):
        linked_list = self.get_linked_list([1, 2, 3, 4, 2])
        all_six = linked_list.find_all(6)
        self.assertEqual(len(all_six), 0)

    def test_insert(self):
        linked_list = LinkedList()
        node_list = [Node(number) for number in [1, 2, 3, 4]]

        for node in node_list:
            linked_list.add_in_tail(node)

        linked_list.insert(node_list[0], Node(666))
        self.assertEqual(self.get_node_values_list(linked_list), [1, 666, 2, 3, 4])

        linked_list.insert(None, Node(111))
        self.assertEqual(self.get_node_values_list(linked_list), [111, 1, 666, 2, 3, 4])

        linked_list.clean()
        linked_list.insert(None, Node(111))
        self.assertEqual(self.get_node_values_list(linked_list), [111])


if __name__ == '__main__':
    unittest.main()
