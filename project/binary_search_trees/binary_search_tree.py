class BSTNode:
    def __init__(self, key, val, parent):
        self.NodeKey = key  # pragma: no mutate
        self.NodeValue = val  # pragma: no mutate
        self.Parent = parent  # pragma: no mutate
        self.LeftChild = None  # pragma: no mutate
        self.RightChild = None  # pragma: no mutate

    @property
    def is_list(self):
        return not self.LeftChild and not self.RightChild

    @property
    def what_child_am_i(self):
        if self.Parent:
            if self == self.Parent.LeftChild:
                return 'LeftChild'
            elif self == self.Parent.RightChild:
                return 'RightChild'


class BSTFind:
    def __init__(self, node=None, node_has_key=False, to_left=False):
        self.Node = node  # pragma: no mutate
        self.NodeHasKey = node_has_key  # pragma: no mutate
        self.ToLeft = to_left  # pragma: no mutate


class BST:
    def __init__(self, node):
        self.Root = node  # pragma: no mutate

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
        result = None  # pragma: no mutate
        child_node = None  # pragma: no mutate

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

        if not node:
            self.Root = BSTNode(key, value, None)
            return True

        return self._recursive_node_find(key, value, node, add=True)

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

    def _swap_nodes(self, aim_node, node_to_replace, direction):
        if node_to_replace.Parent != aim_node and direction:
            setattr(node_to_replace.Parent, direction, None)

        node_to_replace.Parent = aim_node.Parent
        node_to_replace.LeftChild = aim_node.LeftChild

        # Check if offspring has only right child and we must replace it and think about recursion in this root:
        if node_to_replace == aim_node.RightChild:
            node_to_replace.RightChild = None
        else:
            node_to_replace.RightChild = aim_node.RightChild

        # Check if deleted node is Root:
        if node_to_replace.Parent is None:
            self.Root = node_to_replace
        else:
            setattr(node_to_replace.Parent, aim_node.what_child_am_i, node_to_replace)

    def _find_offspring(self, result_node):
        offspring = self.FinMinMax(result_node.RightChild, find_max=False)

        if not offspring.is_list:
            # If offspring is not list -> working with his RightChild
            self._swap_nodes(offspring, offspring.RightChild, 'RightChild')

        self._swap_nodes(result_node, offspring, offspring.what_child_am_i)

    def _delete_child_from_parent(self, result_node):
        # If deleted node Root and it don't have right child -> clear tree
        if result_node == self.Root and self.Root.RightChild is None:
            self.Root = None  # pragma: no mutate
            return

        # If deleted Node don't have right child - clear deleted node from his parent:
        if result_node.RightChild is None and result_node.what_child_am_i:
            setattr(result_node.Parent, result_node.what_child_am_i, None)
        elif result_node.RightChild.is_list:
            # noinspection PyTypeChecker
            self._swap_nodes(result_node, result_node.RightChild, result_node.what_child_am_i)
        else:
            self._find_offspring(result_node)

    def DeleteNodeByKey(self, key):
        result = self.FindNodeByKey(key)

        if result.NodeHasKey:
            self._delete_child_from_parent(result.Node)
            return True

        return False
