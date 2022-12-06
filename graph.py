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
        Creates an edge between the specified nodes. The default is an undirected graph.
        """
        if self.is_directed:
            self.graph[u].append(v)
        
        else:
            if v not in self.graph[u] or u not in self.graph[v]: 
                self.graph[u].append(v)
                self.graph[v].append(u)

    def adjacency_matrix(self) -> np.ndarray:
        """
        Creates an adjacency matrix of a given graph.
        """
        m = max([max(i) for i in self.graph.values()])
        if m not in self.graph.keys():
            self.graph[m] = []

        self.adj_matrix = np.zeros((len(self.graph), len(self.graph)))

        for i in sorted(self.graph.keys()):
            for j in self.graph[i]:
                if j not in self.graph.keys():
                    self.graph[j] = []
                self.adj_matrix[i][j] += 1
        return self.adj_matrix