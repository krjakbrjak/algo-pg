from dataclasses import dataclass, field
from typing import Dict, List, Optional, Set


@dataclass
class Node:
    label: int

    def __eq__(self, other):
        if not isinstance(other, Node):
            raise TypeError

        return self.label == other.label

    def __hash__(self):
        return hash(self.label)


@dataclass
class Connection:
    node: Node
    weight: Optional[int] = 1


@dataclass
class AdjacencyList:
    connections: Dict[int, List[Connection]] = field(default_factory=dict)

    def connect(self, node: Node, to: Node, weight: Optional[int] = 1):
        self.connections.update(
            {
                node.label: self.connections.get(node.label, [])
                + [Connection(node=to, weight=weight)]
            }
        )


@dataclass
class Graph:
    nodes: Set[Node] = field(default_factory=set)
    adjacency_list: AdjacencyList = field(default_factory=AdjacencyList)

    def connect(self, node: Node, to: Node, weight: Optional[int] = 1):
        self.adjacency_list.connect(node, to, weight)
        self.nodes.add(node)
        self.nodes.add(to)
