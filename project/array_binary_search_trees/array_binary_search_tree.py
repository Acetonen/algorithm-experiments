class aBST:  # noqa
    def __init__(self, depth):
        # правильно рассчитайте размер массива для дерева глубины depth:
        self.tree_size = 2 ** (depth + 1) - 1
        self.Tree = [None for _ in range(self.tree_size)]

    def _recursive_node_find(self, key, index, add=False):
        result = None  # pragma: no mutate
        child_index = None  # pragma: no mutate
        node_key = self.Tree[index]

        if key > node_key:
            child_index = 2 * index + 2
        elif key < node_key:
            child_index = 2 * index + 1

        empty_child = child_index and self.Tree[child_index] is None

        if node_key == key:
            result = index
        elif child_index < len(self.Tree) and empty_child:
            result = -child_index

        # Continue recursion:
        if result is None and child_index < len(self.Tree):
            # noinspection PyUnboundLocalVariable
            result = self._recursive_node_find(key, child_index, add)

        return result

    def FindKeyIndex(self, key):
        index = 0

        if not self.Tree[index]:
            return -index

        return self._recursive_node_find(key, index)

    def AddKey(self, key):
        index = self.FindKeyIndex(key)
        empty_tree = index == 0 and self.Tree[0] is None

        if index is None:
            return -1
        if index < 0 or empty_tree:
            self.Tree[-index] = key
        else:
            return index
