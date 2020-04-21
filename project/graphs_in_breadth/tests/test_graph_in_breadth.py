from project.graphs_in_breadth.graph_in_breadth import Vertex, SimpleGraph


def create_vertexes_list_from_values(values_list):
    return [Vertex(value) if value else None for value in values_list]


# noinspection DuplicatedCode
def test_breadth_first_search_empty():
    graph = SimpleGraph(5)
    graph.vertex = create_vertexes_list_from_values([1, 2, 3, 4, 5, 6])
    for pair in [(0, 1), (1, 2), (0, 3), (3, 4)]:
        graph.AddEdge(*pair)

    assert [vertex.Value for vertex in graph.BreadthFirstSearch(0, 5)] == []


# noinspection DuplicatedCode
def test_breadth_first_search():
    graph = SimpleGraph(6)
    graph.vertex = create_vertexes_list_from_values([1, 2, 3, 4, 5, 6])
    for pair in [(0, 1), (1, 2), (0, 3), (3, 4), (0, 5)]:
        graph.AddEdge(*pair)

    assert [vertex.Value for vertex in graph.BreadthFirstSearch(0, 4)] == [1, 4, 5]  # [0, 3, 4]
    assert [vertex.Value for vertex in graph.BreadthFirstSearch(2, 4)] == [3, 2, 1, 4, 5]
