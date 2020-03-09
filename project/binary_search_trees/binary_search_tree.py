class BSTNode:
    def __init__(self, key, val, parent):
        self.NodeKey = key  # pragma: no mutate
        self.NodeValue = val  # pragma: no mutate
        self.Parent = parent  # pragma: no mutate
        self.LeftChild = None  # pragma: no mutate
        self.RightChild = None  # pragma: no mutate


class BSTFind:
    def __init__(self, node=None, node_has_key=True, to_left=False):
        self.Node = node  # pragma: no mutate
        self.NodeHasKey = node_has_key  # pragma: no mutate
        self.ToLeft = to_left  # pragma: no mutate


class BST:
    def __init__(self, node):
        self.Root = node  # pragma: no mutate
        self.min_max_result = None  # pragma: no mutate

    @staticmethod  # pragma: no mutate
    def _get_not_find_result(add, node):
        if add:
            return False

        return BSTFind(node, node_has_key=True, to_left=False)

    @staticmethod  # pragma: no mutate
    def _get_find_result(add, node, child_node, key, value):
        if add:
            setattr(node, child_node, BSTNode(key, value, node))
            return True

        return BSTFind(node, node_has_key=False, to_left=child_node == 'LeftChild')

    def _recursive_node_find(self, key, value, node, add=False):
        result = None
        child_node = None

        if key > node.NodeKey:
            child_node = 'RightChild'  # pragma: no mutate
        elif key < node.NodeKey:
            child_node = 'LeftChild'  # pragma: no mutate

        if node.NodeKey == key:
            result = self._get_not_find_result(add, node)
        elif child_node and getattr(node, child_node) is None:
            result = self._get_find_result(add, node, child_node, key, value)

        # Continue recursion:
        if result is None:
            # noinspection PyUnboundLocalVariable
            result = self._recursive_node_find(key, value, getattr(node, child_node), add)

        return result

    def FindNodeByKey(self, key):
        node = self.Root

        if not node:
            return BSTFind(None, node_has_key=False, to_left=False)

        return self._recursive_node_find(key, None, node)

    def AddKeyValue(self, key, value):
        node = self.Root

        return self._recursive_node_find(key, value, node, add=True)

    @staticmethod  # pragma: no mutate
    def _delete_child_from_parent(result, key):
        parent_node = result.Node.Parent
        if parent_node.NodeKey < key:
            parent_node.RightChild = None
        else:
            parent_node.LeftChild = None

    def DeleteNodeByKey(self, key):
        result = self.FindNodeByKey(key)
        if result.NodeHasKey:
            self._delete_child_from_parent(result, key)
            return True

        return False

    def _recursive_node_list_append(self, result_list, node):
        result_list.append(node)

        for child in [node.LeftChild, node.RightChild]:
            if child:
                self._recursive_node_list_append(result_list, child)

    def Count(self):
        result_list = list()

        if not self.Root:
            return 0

        self._recursive_node_list_append(result_list, self.Root)

        return len(result_list)

    def FinMinMax(self, from_node, find_max):
        result = None
        direction = 'RightChild' if find_max else 'LeftChild'

        while from_node:
            result = from_node
            from_node = getattr(from_node, direction)

        return result
