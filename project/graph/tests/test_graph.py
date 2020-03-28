from collections import namedtuple

import pytest

from project.graph.graphs import SimpleGraph, Vertex

TestFixture = namedtuple('TestFixture', 'list result')


def get_vertexes_values_list(graph):
    return [vertex.Value if vertex else None for vertex in graph.vertex]


def create_vertexes_list_from_values(values_list):
    return [Vertex(value) if value else None for value in values_list]


@pytest.mark.parametrize('fixture', [
    TestFixture([], []),
    TestFixture([3, None, 3], [3, 666, 3]),
    TestFixture([None, None, None], [666, None, None]),
    TestFixture([1, 2, 3], [1, 2, 3]),
])
def test_add_vertex(fixture):
    graph = SimpleGraph(len(fixture.list))
    graph.vertex = create_vertexes_list_from_values(fixture.list)
    graph.AddVertex(666)

    assert get_vertexes_values_list(graph) == fixture.result


@pytest.mark.parametrize('fixture', [
    TestFixture([0, 2], [[0, 0, 1],
                         [0, 0, 0],
                         [1, 0, 0]]),
])
def test_add_edge(fixture):
    graph = SimpleGraph(3)
    graph.AddEdge(*fixture.list)

    assert graph.m_adjacency == fixture.result


@pytest.mark.parametrize('fixture', [
    TestFixture(
        [[0, 0, 1],
         [0, 0, 0],
         [1, 0, 0]],

        [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]
    ),
])
def test_remove_edge(fixture):
    graph = SimpleGraph(3)
    graph.m_adjacency = fixture.list
    graph.RemoveEdge(0, 2)

    assert graph.m_adjacency == fixture.result


@pytest.mark.parametrize('fixture', [
    TestFixture(
        [[1, 1, 1],
         [1, 0, 0],
         [1, 0, 0]],

        [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]
    ),
])
def test_remove_vertex(fixture):
    graph = SimpleGraph(3)
    graph.AddVertex(111)
    graph.AddVertex(222)
    graph.AddVertex(333)
    graph.AddEdge(0, 0)
    graph.AddEdge(0, 1)
    graph.AddEdge(0, 2)
    assert graph.m_adjacency == fixture.list

    graph.RemoveVertex(0)
    assert graph.m_adjacency == fixture.result


@pytest.mark.parametrize('fixture', [
    TestFixture(
        [[0, 0, 1],
         [0, 0, 0],
         [1, 0, 0]],
        None
    )
])
def test_is_edge(fixture):
    graph = SimpleGraph(3)
    graph.m_adjacency = fixture.list
    assert graph.IsEdge(0, 2) is True
    assert graph.IsEdge(0, 1) is False
