# usr/bin/python3.10

from collections import defaultdict
from typing import Sequence, Any
import numpy as np

class Graph: 
    def __init__(self, is_directed: bool = True):
        self.graph: Sequence[tuple] = []
        self.adjacency_list: defaultdict = defaultdict(list[int])
        self.adjacency_matrix: np.ndarray = None
        self.incidence_matrix: np.ndarray = None
        self.is_directed: bool = is_directed
        self.graph_length: int | Any = None

    def add_edges(self, nodes: Sequence[tuple | list]) -> Sequence[tuple]:
        """
        Adds a sequence of edges to the graph. Each edge is represented as a tuple or a list of two elements, 
        indicating a connection between two nodes.

        Parameters:
        - nodes (Sequence[tuple | list]): A sequence of tuples or lists where each tuple/list represents an edge 
                                        in the graph. Each tuple/list should contain exactly two elements.

        Returns:
        - Sequence[tuple]: The updated list of all edges in the graph after adding the new edges.

        Note:
        This method updates the graph's internal representation of edges but does not immediately update 
        the adjacency list or matrix views.
        """
        for node in nodes:
            if node not in self.graph:
                self.graph.append(node)
        return self.graph
    
    def adjacency_view(self) -> defaultdict[int, list[int]]:
        """
        Generates and returns the adjacency list representation of the graph. The adjacency list is created 
        based on the current set of edges in the graph and reflects whether the graph is directed or undirected.

        Returns:
        - defaultdict[int, list[int]]: A dictionary where each key is a node and its value is a list of 
                                    all adjacent nodes. The keys include all nodes present in the graph's edges.

        Note:
        This method updates the graph's `graph_length` property based on the number of unique nodes in the 
        adjacency list. The adjacency list is created each time this method is called, reflecting the latest 
        state of the graph's edges.
        """

        if self.is_directed:
            for node in self.graph:
                if node[1] not in self.adjacency_list[node[0]]:
                    self.adjacency_list[node[0]].append(node[1])
                if not self.adjacency_list.get(node[1]):
                    self.adjacency_list[node[1]] = []
                    
        else: 
            for node in self.graph:
                self.adjacency_list[node[0]].append(node[1])
                self.adjacency_list[node[1]].append(node[0])
        self.graph_length = len(self.adjacency_list)
        return self.adjacency_list
    

    def adjacency_matrix_view(self) -> np.ndarray:
        """
        Generates and returns the adjacency matrix representation of the graph. This method first ensures 
        that the adjacency list is up-to-date and then constructs a matrix where each element (i, j) is 1 if 
        there is an edge from node i to node j, and 0 otherwise.

        Returns:
        - np.ndarray: A 2D NumPy array representing the adjacency matrix of the graph. The size of the matrix 
                    is determined by the number of unique nodes in the graph.

        Note:
        If the adjacency list is not current, this method will first call `adjacency_view` to update it. 
        The method updates the graph's `graph_length` property based on the number of unique nodes.
        """
        if len(self.adjacency_list) > 0:
            self.graph_length = len(self.adjacency_list)
            self.adjacency_matrix = np.zeros((self.graph_length, self.graph_length))
        else:
            self.adjacency_list = self.adjacency_view()
            self.graph_length = len(self.adjacency_list)
            self.adjacency_matrix = np.zeros((self.graph_length, self.graph_length))

        for u in self.adjacency_list.keys():
            for v in self.adjacency_list[u]:
                self.adjacency_matrix[u][v] = 1
        return self.adjacency_matrix

        
    def incidence_matrix_view(self) -> np.ndarray:

        edges_length = len(self.graph)
        if not self.graph_length:
            self.adjacency_view()
        vertex_length = self.graph_length
        self.incidence_matrix = np.zeros((vertex_length, edges_length))

        if not self.is_directed:
            for e, edge in enumerate(self.graph):
                self.incidence_matrix[edge[0]][e] = 1
                self.incidence_matrix[edge[1]][e] = 1
        else: 
            for e, edge in enumerate(self.graph):
                self.incidence_matrix[edge[0]][e] = -1
                self.incidence_matrix[edge[1]][e] = 1
                
        return self.incidence_matrix
            

    def get_edges(self):
        return self.graph
    
    def get_vertices(self):
        if self.graph_length:
            return self.adjacency_view().keys()
        else:
            return self.adjacency_list.keys()
    
    # TO-DO
    





            
            



    

