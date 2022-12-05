# !usr/bin/python3.10

# https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/


from collections import defaultdict
import numpy as np

class Graph: 
    def __init__(self, is_directed: bool=False):

        self.graph = defaultdict(list)
        self.is_directed = is_directed
        self.adj_matrix = np.zeros((1))

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

    def adjecency_matrix(self) -> np.ndarray:

        """
        Creates an adjecency matrix of a given graph.
        """

        self.adj_matrix = np.zeros((len(self.graph), len(self.graph)))
        for e, i in enumerate(self.graph.values()):
            for j in i:
                self.adj_matrix[e][j] += 1
        return self.adj_matrix 

    def BFS(self, start_node: int, end_node: int=0, is_shortest: bool=False) -> list[int]: 

        """
        Breadth first searching algorithm 
        """
        try:
            assert type(start_node) == int
        except AssertionError:
            print(f"Node type ({start_node}) must be an integer")

        print(self.graph)

        Q = [start_node]
        explored = [start_node]


        while Q:

            if end_node and end_node in explored:
                break

            v = Q.pop(0)

            for w in self.graph[v]:                     
                if w not in explored: 
                    explored.append(w)
                    Q.append(w) 

        distance = self.back_tracing(start_node, end_node)
        print(distance)
        return explored, distance      

    def back_tracing(self, start_node, end_node):

        """
        Finds the shortest path between two nodes using adjecency matrix.
        """

        # mat = self.adjecency_matrix() # use this if you are not instantiating adjecency matrix from outer
        distance = 0
        for i in range(end_node, 0, -1):
            back = self.adj_matrix[i] # change this to mat if it not instantiated
            distance += 1
            for j in np.where(back>0)[0]:
                if j == start_node:
                    return distance
        return distance

g = Graph()
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(2, 3)
g.addEdge(3, 0)
g.addEdge(3, 4)
g.addEdge(4, 5 )

g.adjecency_matrix()
g.BFS(0, 5, True)
