from typing import List

from algorithm.graph.dfs import graph_components
from algorithm.graph.node import Graph, Node


def label_for_index(row: int, column: int, inp: List[List[int]]):
    return row * len(inp[0]) + column


def value_for_label(label: int, inp: List[List[int]]):
    return inp[label // len(inp[0])][label % len(inp[0])]


def two_d_map_to_graph(inp: List[List[int]]) -> Graph:
    """
    Converts a 2d array to a graph. Each element in the
    2d array corresponds to a node in a graph. Two nodes
    are connected if both array elements are not zero.
    Nodes labels are calculated from the element position.
    """
    g = Graph()
    for i in range(len(inp)):
        for j in range(len(inp[0])):
            g.nodes.add(Node(i * len(inp) + j))
            if inp[i][j]:
                if j < len(inp[0]) - 1 and inp[i][j + 1]:
                    g.connect(Node(label_for_index(i, j, inp)), Node(label_for_index(i, j + 1, inp)))
                if j > 0 and inp[i][j - 1]:
                    g.connect(Node(label_for_index(i, j, inp)), Node(label_for_index(i, j - 1, inp)))
                if i < len(inp) - 1 and inp[i + 1][j]:
                    g.connect(Node(label_for_index(i, j, inp)), Node(label_for_index(i + 1, j, inp)))
                if i > 0 and inp[i - 1][j]:
                    g.connect(Node(label_for_index(i, j, inp)), Node(label_for_index(i - 1, j, inp)))
    return g


def largest_graph_sum(inp: List[List[int]]) -> int:
    """
    Finds all the components in the graph and sums up
    all elements from the original map that correspond to
    the nodes in a particular component. DFS is utilized to
    find all components in the graph.
    :param inp: 2d array
    """
    g = two_d_map_to_graph(inp)
    sums: List[int] = []
    for component in graph_components(g):
        sums.append(sum([value_for_label(i.label, inp) for i in component]))
    return max(sums)


def test_largest_graph_sum():
    two_d_map = [[3, 0, 0, 1, 2],
                 [0, 1, 4, 0, 1],
                 [5, 0, 0, 3, 3]]
    assert largest_graph_sum(two_d_map) == 10
