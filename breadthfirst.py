# !usr/bin/python3.10

# https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/


from collections import defaultdict
import numpy as np

class Graph: 
    def __init__(self, is_directed: bool = False):

        self.graph = defaultdict(list)
        self.is_directed = is_directed

    def addEdge(self, u: int, v: int) -> defaultdict[list]:

        """
        Creates a edge between specified nodes. The default is undirected graph.
        """

        if self.is_directed:
            if u not in self.graph[u]:
                self.graph[u].append(v)
        
        else:
            if v not in self.graph[u] or u not in self.graph[v]: 
                self.graph[u].append(v)
                self.graph[v].append(u)

    def adj_matrix(self) -> np.ndarray:

        """
        Creates an adjecency matrix of a given graph.
        """

        adj_matrix = np.zeros((len(self.graph), len(self.graph)))
        for e, i in enumerate(self.graph.values()):
            for j in i:
                adj_matrix[e][j] += 1
        return adj_matrix 

    def BFS(self, starting_node: int) -> list[int]: 

        """
        Breadth first searching algorithm 
        """

        starting_node = int(starting_node)
        Q = [starting_node]
        explored = [starting_node]

        while Q: 
            v = Q.pop(0)

            for w in self.graph[v]:
                if w not in explored: 
                    print(f"visited {w}th node")
                    explored.append(w)
                    Q.append(w)
        return explored        

g = Graph()
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(2, 3)
g.addEdge(3, 0)

print(g.adj_matrix())
print(g.BFS(2))