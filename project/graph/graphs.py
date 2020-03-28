class Vertex:

    def __init__(self, val):
        self.Value = val


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
