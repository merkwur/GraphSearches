# usr/bin/python3.10

from collections import defaultdict
import numpy as np

class Graph: 
    def __init__(self):
        self.graph = defaultdict(list[int])
        self.adj_matrix = []

    def create_graph(self, nodes: list or tuple[tuple or list[int]], is_directed: bool=False) -> defaultdict[int, list[int]]:
        """
        Creates an edge between two specified nodes. 
        Conventially, nodes = list[tuple(int: a, int: b)].
        In directed graph, tuple/s contains 'from a', and "to b" nodes respectively.
        The default is an undirected graph.
        """
        
        if type(nodes) not in [list, tuple]:
            raise TypeError("nodes type must be a list of tuples that contains a pair of integer 'list[tuple(int, int)]'")

        if len(nodes) < 1: 
            raise ValueError("nodes cannot be an empty list")
    

        if is_directed:
            for node in nodes:
                if type(node) not in [tuple, list]:
                    raise TypeError("all the list elements must be a tuple or list that contains a pair of integers")
                if len(node) != 2:
                    raise ValueError("tuple must contains exactly 2 integers; 'from' node and 'to' node")

                if node[1] not in self.graph[node[0]]:
                    if not self.graph[node[0]]:
                        self.graph[node[0]] = []
                    self.graph[node[0]].append(node[1])

                if not self.graph[node[1]]:
                    self.graph[node[1]] = []

                    
        else:
            for node in nodes:
                if type(node) not in [tuple, list]:
                    raise TypeError("all the list elements must be a tuple or list that contains a pair of integers")
                if len(node) != 2:
                    raise ValueError("tuple must contains exactly 2 integers; 'from' node and 'to' node")
                
                if node[1] not in self.graph[node[0]]:
                    self.graph[node[0]].append(node[1])
                if node[0] not in self.graph[node[1]]:
                    self.graph[node[1]].append(node[0])

        return self.graph
                
        
    def create_adjacency_matrix(self) -> np.ndarray:
        """
        Creates an adjacency matrix of a given graph.
        """
        self.adj_matrix = np.zeros((len(self.graph), len(self.graph)))

        for i in sorted(self.graph.keys()):
            for j in self.graph[i]:
                self.adj_matrix[i][j] += 1
        return self.adj_matrix
    

