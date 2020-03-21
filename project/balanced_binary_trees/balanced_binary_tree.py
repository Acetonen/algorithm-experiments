class BSTNode:

    def __init__(self, key, parent, level=0):
        self.NodeKey = key  # ключ узла
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок
        self.Level = level  # уровень узла


class BalancedBST:
    def __init__(self):
        self.Root = None  # корень дерева

    def _recursively_fill_tree(self, level, parent, array):
        if not array:
            return

        sub_index = len(array) // 2
        node_key = array[sub_index]
        node = BSTNode(node_key, parent, level)

        if parent is None:
            self.Root = node
        elif node_key < parent.NodeKey:
            parent.LeftChild = node
        elif node_key >= parent.NodeKey:
            parent.RightChild = node

        left_side = array[:sub_index]
        right_side = array[sub_index + 1:]

        self._recursively_fill_tree(level + 1, node, left_side)
        self._recursively_fill_tree(level + 1, node, right_side)

    def GenerateTree(self, array):
        array = sorted(array)

        self._recursively_fill_tree(1, None, array)

    def _recursive_lists_level_find(self, levels_list, node):
        for child in ('LeftChild', 'Root', 'RightChild'):
            if child is 'Root' and node.LeftChild is None and node.RightChild is None:
                levels_list.append(node.Level)
            elif getattr(node, child, None):
                self._recursive_lists_level_find(levels_list, getattr(node, child))

    def _get_lists_levels(self, node=None):
        levels_list = list()

        if node is None:
            if self.Root is not None:
                node = self.Root
            else:
                levels_list = list()

        self._recursive_lists_level_find(levels_list, self.Root)

        return levels_list

    def IsBalanced(self, root_node):
        lists_levels = self._get_lists_levels(root_node)
        print(lists_levels)
        if lists_levels:
            return max(lists_levels) - min(lists_levels) < 2

        return False  # сбалансировано ли дерево с корнем root_node
