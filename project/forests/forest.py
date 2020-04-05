class SimpleTreeNode:
    def __init__(self, val, parent, level=0):
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # pragma: no mutate
        self.Children = list()  # список дочерних узлов
        self.Level = level  # уровень узла


class SimpleTree:
    def __init__(self, root):
        self.Root = root  # pragma: no mutate

    def AddChild(self, parent_node, new_child):
        parent_node.Children.append(new_child)
        new_child.Parent = parent_node
        new_child.Level = parent_node.Level + 1

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

    def _remove_edge(self, parent, children):
        parent.Children.remove(children)
        children.Parent = None
        children.Level = 0

    def _check_even_tree(self, current_node, sub_root_nodes_count):
        result_list = list()

        if sub_root_nodes_count % 2 == 0:  # If last tree is even -> remove edge
            result_list.append(current_node.Parent)
            result_list.append(current_node)
            self._remove_edge(current_node.Parent, current_node)

        return result_list

    def EvenTrees(self):
        result_list = list()

        all_nodes = self.GetAllNodes()
        if not all_nodes or len(all_nodes) == 1:  # If list is empty or has only root node -> return
            return list()

        for node in sorted(all_nodes, key=lambda vertex: vertex.Level, reverse=True):
            sub_root_nodes_count = len(SimpleTree(node).GetAllNodes())

            if node is self.Root:  # End our search if we find root
                if sub_root_nodes_count % 2 == 1:  # If last tree is odd -> clear result list
                    return list()
                return result_list

            result_list.extend(self._check_even_tree(node, sub_root_nodes_count))
