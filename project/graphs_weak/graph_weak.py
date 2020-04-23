from collections import deque
from itertools import combinations


class FindWay(Exception):
    def __init__(self, result):
        self.result = result


class Vertex:
    def __init__(self, value):
        self.Value = value
        self.Hit = False

    def __repr__(self):
        return str(self.Value)


class SimpleGraph:
    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0 for _ in range(size)] for _ in range(size)]
        self.vertex = [None for _ in range(size)]

    def AddVertex(self, vertex_value):
        for index, place in enumerate(self.vertex):
            if place is None:
                self.vertex[index] = Vertex(vertex_value)  # noqa
                break

    def AddEdge(self, vertex1_index, vertex2_index):
        self.m_adjacency[vertex1_index][vertex2_index] = 1
        self.m_adjacency[vertex2_index][vertex1_index] = 1

    def RemoveEdge(self, vertex1_index, vertex2_index):
        self.m_adjacency[vertex1_index][vertex2_index] = 0
        self.m_adjacency[vertex2_index][vertex1_index] = 0

    def RemoveVertex(self, vertex_index):
        for row in self.m_adjacency:
            row[vertex_index] = 0

        for column, _ in enumerate(self.m_adjacency[vertex_index]):
            self.m_adjacency[vertex_index][column] = 0

    def IsEdge(self, vertex1_index, vertex2_index):
        return self.m_adjacency[vertex1_index][vertex2_index] == 1

    def clean_vertex_hits(self):
        for vertex in self.vertex:
            if vertex is not None:
                vertex.Hit = False

    def _go_deeper(self, current_index, result_stack, to_index):
        for index, edge in enumerate(self.m_adjacency[current_index]):
            if edge == 1 and self.vertex[index].Hit is False:
                if self._try_to_find_from_near_vertexes(index, result_stack, to_index):
                    return True

    def _search_nearest(self, current_index, to_index, result_stack):
        for index, edge in enumerate(self.m_adjacency[current_index]):
            if edge == 1 and index == to_index:
                result_stack.append(self.vertex[index])  # noqa
                return True

    def _try_to_find_from_near_vertexes(self, current_index, result_stack, to_index):
        self.vertex[current_index].Hit = True
        result_stack.append(self.vertex[current_index])  # noqa

        if self._search_nearest(current_index, to_index, result_stack):
            raise FindWay

        if not self._go_deeper(current_index, result_stack, to_index):
            result_stack.pop()

    def DepthFirstSearch(self, from_index, to_index):
        result_stack = list()
        self.clean_vertex_hits()

        try:
            self._try_to_find_from_near_vertexes(from_index, result_stack, to_index)
        except FindWay:
            pass

        return result_stack

    def _add_nearest_to_que(self, current_trace, que):
        for index, edge in enumerate(self.m_adjacency[current_trace[-1]]):
            if edge == 1 and self.vertex[index].Hit is False:
                que.append(current_trace + [index])

    def _try_to_find_in_breadth(self, current_trace, to_index, que):
        current_index = current_trace[-1]
        self.vertex[current_index].Hit = True

        if current_index == to_index:
            raise FindWay(current_trace)
        self._add_nearest_to_que(current_trace, que)

        if que:
            self._try_to_find_in_breadth(que.popleft(), to_index, que)

    def BreadthFirstSearch(self, from_index, to_index):
        result = list()
        self.clean_vertex_hits()
        que = deque()

        try:
            self._try_to_find_in_breadth([from_index], to_index, que)
        except FindWay as exit_:
            result = exit_.result

        return [self.vertex[index] for index in result]

    def _get_nearest_vertexes_list(self, current_index):
        return [index for index, edge in enumerate(self.m_adjacency[current_index]) if edge == 1]  # noqa

    def _find_at_least_one_edge(self, nearest):
        for pair in combinations(nearest, 2):
            if self.IsEdge(*pair):
                return True

    def WeakVertices(self):
        weak_vertices_list = list()

        for index, vertex in enumerate(self.vertex):
            nearest = self._get_nearest_vertexes_list(index)

            if not self._find_at_least_one_edge(nearest):
                weak_vertices_list.append(vertex)

        return weak_vertices_list
