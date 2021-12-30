import random, copy
from typing import NewType

GRAPH = 0
NODE = 1
EDGE = 2
PRIM = 3
KRUSKAL = 4

A = 0
B = 1
C = 2
D = 3
E = 4
F = 5

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

nodeId = 0
edgeId = 0

class Factory:
    @staticmethod
    def getInstance(className):
        if className == GRAPH:
            return Graph()
        elif className == NODE:
            return Node()
        elif className == EDGE:
            return Edge()
        elif className == PRIM:
            return PrimAlgorithm()
        elif className == KRUSKAL:
            return KruskalAlgorithm()

class Graph:
    def __init__(self) -> None:
        self.nodes = {}
        self.edges = []
    
    def insertNode(self, node):
        self.nodes[node.id] = node

    def insertEdge(self, edge):
        cond = (self.nodes.get(edge.node1) is not None) and (self.nodes.get(edge.node2) is not None)
        if cond:
            self.nodes[edge.node1].edges.append(edge)
            self.nodes[edge.node2].edges.append(edge)
            self.edges.append(edge)
        else:
            raise Exception("Node doesn't exist.")
    
    def __repr__(self) -> str:
        return  f'nodes : {list(self.nodes.values())}\nedges : {self.edges}'

class Node:
    def __init__(self) -> None:
        global nodeId
        self.id = nodeId
        self.visited = False
        self.edges = []
        nodeId += 1

    def __repr__(self) -> str:
        return ALPHABET[self.id]

class Edge:
    def __init__(self) -> None:
        global edgeId
        self.id = edgeId
        self.node1 = -1
        self.node2 = -1
        self.weight = 0
        edgeId += 1
    
    def setting(self, node1, node2, weight):
        self.node1 = node1
        self.node2 = node2
        self.weight = weight
    
    def __repr__(self) -> str:
        return f'{ALPHABET[self.node1]} - {ALPHABET[self.node2]} ({self.weight})'

class Algorithm:
    def __init__(self) -> None:
        self.graph = None
    
    def setting(self, graph):
        self.graph = copy.copy(graph)

class PrimAlgorithm(Algorithm):
    def __init__(self) -> None:
        super().__init__()
    
    def __call__(self):
        graph = self.graph
        visited = []
        for i in range(len(graph.nodes)):
            nowNode = random.choice(tuple(graph.nodes.keys()))
            visited.append(nowNode)
            self.graph.nodes[nowNode].visited = True
            visited.append(nowNode)
            nowNode = graph[nowNode]
            
class KruskalAlgorithm(Algorithm):
    def __init__(self) -> None:
        super().__init__()

# 1. 그래프 생성
g = Factory.getInstance(GRAPH)

# 2. 그래프에 노드 6개 추가
for i in range(6):
    g.insertNode(Factory.getInstance(NODE))

# 3. 간선들 추가
edgeData = [
    (A, B, 15),
    (A, C, 10),
    (A, D,  9),
    (A, E, 40),
    (B, D, 12),
    (B, F, 13),
    (B, E, 25),
    (C, D, 12),
    (C, E, 40),
    (C, F, 32),
    (D, F, 25),
    (E, F, 10),
]
for data in edgeData:
    edge = Factory.getInstance(EDGE)
    edge.setting(*data)
    g.insertEdge(edge)

# 4. 그래프 출력
print(g)

# 5. 프림 알고리즘 실행
prim = Factory.getInstance(PRIM)
prim.setting(g)

# 6. 크루스칼 알고리즘 실행
kruskal = Factory.getInstance(KRUSKAL)
kruskal.setting(g)