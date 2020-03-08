class SimpleTreeNode:
    def __init__(self, val, parent):
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # pragma: no mutate
        self.Children = list()  # список дочерних узлов


class SimpleTree:
    def __init__(self, root):
        self.Root = root  # pragma: no mutate

    def AddChild(self, parent_node, new_child):
        parent_node.Children.append(new_child)
        new_child.Parent = parent_node

    def _recursive_node_delete(self, current_node, node_to_delete):
        if current_node == node_to_delete:
            current_node.Parent.Children.remove(node_to_delete)
            return

        for node in current_node.Children:
            self._recursive_node_delete(node, node_to_delete)

    def DeleteNode(self, node_to_delete):
        if not self.Root.Children or not self.Root:
            self.Root = None  # pragma: no mutate
            return

        self._recursive_node_delete(self.Root, node_to_delete)

    def _recursive_node_list_append(self, result_list, node, *, find_value=None, leafs_only=False):
        if (
            (not find_value and not leafs_only)  # noqa
            or node.NodeValue == find_value
            or (leafs_only and not node.Children)
        ):
            result_list.append(node)

        for child in node.Children:
            self._recursive_node_list_append(result_list, child, find_value=find_value, leafs_only=leafs_only)

    def GetAllNodes(self):
        result_list = list()

        if not self.Root:
            return result_list

        self._recursive_node_list_append(result_list, self.Root)

        return result_list

    def FindNodesByValue(self, value):
        result_list = list()

        if not self.Root:
            return result_list

        self._recursive_node_list_append(result_list, self.Root, find_value=value)

        return result_list

    def MoveNode(self, original_node, new_parent):
        self.DeleteNode(original_node)
        self.AddChild(new_parent, original_node)

    def Count(self):
        return len(self.GetAllNodes())

    def LeafCount(self):
        result_list = list()
        self._recursive_node_list_append(result_list, self.Root, leafs_only=True)

        return len(result_list)
