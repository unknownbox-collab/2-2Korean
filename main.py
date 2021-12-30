import random, copy

GRAPH = 0
NODE = 1
EDGE = 2
PRIM = 3
KRUSKAL = 4
SOLIN = 5

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
        elif className == SOLIN:
            return SolinAlgorithm()

class Graph:
    def __init__(self) -> None:
        self.nodes = {}
        self.edges = []
        self.edgesByNode1 = {}
        self.edgesByNode2 = {}
    
    def insertNode(self, node):
        self.nodes[node.id] = node
    
    def addEdgeWhatever(self, edge):
        self.edges.append(edge)

        if edge.node1 in self.edgesByNode1.keys():
            self.edgesByNode1[edge.node1].append(edge)
        else: 
            self.edgesByNode1[edge.node1] = [edge]
        
        if edge.node2 in self.edgesByNode2.keys():
            self.edgesByNode2[edge.node2].append(edge)
        else: 
            self.edgesByNode2[edge.node2] = [edge]

    def insertEdge(self, edge):
        if edge.node1 in self.nodes.keys() and edge.node2 in self.nodes.keys():
            if edge.node1 in self.edgesByNode1.keys() and edge.node2 in self.edgesByNode2.keys():
                node1Tonode2 = edge.node2 in map(lambda x: x.node2, self.edgesByNode1[edge.node1])
                node2Tonode1 = edge.node1 in map(lambda x: x.node1, self.edgesByNode2[edge.node2])
                if not (node1Tonode2 or node2Tonode1):
                    self.addEdgeWhatever(edge)
                else:
                    raise Exception("Target node already has same edge.")
            else:
                self.addEdgeWhatever(edge)
        else:
            raise Exception("Target node does not exist.")
    
    def __repr__(self) -> str:
        return  f'nodes : {list(self.nodes.values())}\nedges : {self.edges}'

class Node:
    def __init__(self) -> None:
        global nodeId
        self.id = nodeId
        self.visited = False
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
        for i in range(len(graph.nodes)):
            nowNode = random.choice(tuple(graph.nodes.keys()))
            self.graph.nodes[nowNode].visited = True
            nowNode = graph[nowNode]
            cand = {}
            target = max(tuple(cand.values()), key = lambda x : x.weight)
            
class KruskalAlgorithm(Algorithm):
    def __init__(self) -> None:
        super().__init__()

class SolinAlgorithm(Algorithm):
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

# 7. 솔린 알고리즘 실행
solin = Factory.getInstance(SOLIN)
solin.setting(g)