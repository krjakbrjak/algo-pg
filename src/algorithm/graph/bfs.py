from collections import deque
from dataclasses import dataclass, field
from typing import Iterator, Tuple

from algorithm.graph.node import Graph, Node


@dataclass
class BFS:
    graph: Graph = field(default_factory=Graph)
    visited: Tuple[int, ...] = field(default_factory=tuple)
    queue: deque = field(default_factory=deque)

    def run_stack(self, node: Node) -> Iterator[Node]:
        nodes: deque = deque()
        nodes.append(node)

        while len(nodes):
            i = nodes.popleft()
            if i.label not in self.visited:
                self.visited += (i.label,)
                yield i

            for neighbour in self.graph.adjacency_list.connections.get(i.label, []):
                if neighbour.node.label not in self.visited:
                    nodes.append(neighbour.node)
