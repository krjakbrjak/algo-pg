from dataclasses import dataclass
from typing import Iterator, List, Tuple

from algorithm.graph.node import AdjacencyList, Graph, Node


@dataclass
class DFS:
    graph: Graph
    visited: Tuple[int, ...] = tuple()

    def run_recursion(self, node: Node) -> Iterator[Node]:
        if node.label not in self.visited:
            self.visited += (node.label,)
            yield node
            for neighbour in self.graph.adjacency_list.connections.get(
                node.label, tuple()
            ):
                yield from self.run_recursion(neighbour.node)

    def run_stack(self, node: Node) -> Iterator[Node]:
        nodes: List[Node] = [node]
        while nodes:
            i = nodes[-1]
            if i.label not in self.visited:
                self.visited += (i.label,)
                yield i
            old_len = len(nodes)
            for neighbour in self.graph.adjacency_list.connections.get(i.label, []):
                if neighbour.node.label not in self.visited:
                    nodes.append(neighbour.node)
                    break
            if old_len == len(nodes):
                nodes.pop()


def graph_components(graph: Graph) -> Iterator[List[Node]]:
    dfs = DFS(graph=graph)
    for vertex in graph.nodes:
        components: List[Node] = []
        for i in dfs.run_stack(vertex):
            components.append(i)
        if components:
            yield components
