# usr/bin/python3.10

from collections import defaultdict
import numpy as np

class Graph: 
    def __init__(self, is_directed: bool=False):

        self.graph = defaultdict(list)
        self.is_directed = is_directed
        self.adj_matrix = []

    def addEdge(self, u: int, v: int) -> defaultdict[list]:
        """
        Creates a edge between specified nodes. The default is undirected graph.
        """
        if self.is_directed:
            self.graph[u].append(v)
            return self.graph
        
        else:
            if v not in self.graph[u] or u not in self.graph[v]: 
                self.graph[u].append(v)
                self.graph[v].append(u)
            return self.graph


    def adjecency_matrix(self) -> np.ndarray:
        """
        Creates an adjecency matrix of a given graph.
        """
        self.adj_matrix = np.zeros((len(self.graph), len(self.graph)))
        for e, i in enumerate(self.graph.values()):
            for j in i:
                self.adj_matrix[e][j] += 1

        return self.adj_matrix