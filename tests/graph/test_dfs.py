from algorithm.graph.dfs import DFS, graph_components
from algorithm.graph.node import AdjacencyList, Graph, Node


def test_dfs():
    graph = Graph()

    a = Node(label=1)
    b = Node(label=2)
    c = Node(label=3)
    d = Node(label=4)
    e = Node(label=5)
    f = Node(label=6)
    g = Node(label=7)
    # a
    graph.connect(a, e)
    graph.connect(a, c)
    graph.connect(a, b)
    # b
    graph.connect(b, a)
    graph.connect(b, d)
    graph.connect(b, f)
    # c
    graph.connect(c, a)
    graph.connect(c, g)
    # d
    graph.connect(d, b)
    # e
    graph.connect(e, a)
    graph.connect(e, f)
    # f
    graph.connect(f, b)
    graph.connect(f, e)
    # g
    graph.connect(g, c)

    traversal = []
    for node in DFS(graph=graph).run_recursion(a):
        traversal.append(node)

    assert traversal == [a, e, f, b, d, c, g]

    traversal = []
    for node in DFS(graph=graph).run_stack(a):
        traversal.append(node)

    assert traversal == [a, e, f, b, d, c, g]


def test_graph_components():
    graph = Graph()

    a = Node(label=1)
    b = Node(label=2)
    c = Node(label=3)
    d = Node(label=4)

    # a
    graph.connect(a, b)
    # b
    graph.connect(b, a)
    # c
    graph.connect(c, d)
    # d
    graph.connect(d, c)

    assert len(list(graph_components(graph))) == 2

    graph.connect(d, a)
    graph.connect(a, d)

    assert len(list(graph_components(graph))) == 1
