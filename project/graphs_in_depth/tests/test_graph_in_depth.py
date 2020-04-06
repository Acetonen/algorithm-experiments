from project.graphs_in_depth.graph_in_depth import Vertex, SimpleGraph


def create_vertexes_list_from_values(values_list):
    return [Vertex(value) if value else None for value in values_list]


def test_depth_first_search():
    graph = SimpleGraph(6)
    graph.vertex = create_vertexes_list_from_values([1, 2, 3, 4, 5, 6])
    for pair in [(0, 1), (1, 2), (0, 3), (3, 4), (0, 5)]:
        graph.AddEdge(*pair)

    assert [vertex.Value for vertex in graph.DepthFirstSearch(0, 4)] == [1, 4, 5]
    assert [vertex.Value for vertex in graph.DepthFirstSearch(2, 4)] == [3, 2, 1, 4, 5]


def test_depth_first_search_empty():
    graph = SimpleGraph(5)
    graph.vertex = create_vertexes_list_from_values([1, 2, 3, 4, 5, 6])
    for pair in [(0, 1), (1, 2), (0, 3), (3, 4)]:
        graph.AddEdge(*pair)

    assert [vertex.Value for vertex in graph.DepthFirstSearch(0, 5)] == []