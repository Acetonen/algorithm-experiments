from project.graphs_weak.graph_weak import SimpleGraph, Vertex


def create_vertexes_list_from_values(values_list):
    return [Vertex(value) if value else None for value in values_list]


def test_weak_search():
    graph = SimpleGraph(6)
    graph.vertex = create_vertexes_list_from_values([1, 2, 3, 4, 5, 6])
    for pair in [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 2)]:
        graph.AddEdge(*pair)

    assert [vertex.Value for vertex in graph.WeakVertices()] == [5, 6]


def test_depth_first_search_empty():
    graph = SimpleGraph(6)
    graph.vertex = create_vertexes_list_from_values([1, 2, 3, 4, 5, 6])
    for pair in [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (2, 4), (1, 5), (2, 5)]:
        graph.AddEdge(*pair)

    assert graph.WeakVertices() == []