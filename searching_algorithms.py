# !usr/bin/python3.10
# https://www.coursera.org/learn/algorithms-graphs-data-structures/

import numpy as np
import graph 

class GraphSearch:
    
    # initialize the graph here
    g = graph.Graph(True)
    g.addEdge(0, 1)
    g.addEdge(1, 2)
    g.addEdge(2, 4)
    g.addEdge(3, 0)
    g.addEdge(3, 4)
    g.addEdge(4, 5)
    g.addEdge(4, 6)
    g.addEdge(6, 7)
    g.adjacency_matrix() 

    def __init__(self):
        self.graph = self.g.graph
        self.adjacency_matrix = self.g.adj_matrix
        self.explored = []
        self.d = 0

    def BFS(self, start_node: int, end_node: int=0, is_shortest: bool=False) -> tuple[list[int], int] or list[int]: 
        """
        Breadth-first searching algorithm 
        """
        assert type(start_node) == int, f"Node type({start_node}) must be an integer"
        assert type(end_node) == int, f"Node type({end_node}) must be an integer"
    
        Q = [start_node]
        self.explored.append(start_node)

        while Q:
            if end_node and end_node in self.explored:
                break

            v = Q.pop(0)
            for w in self.graph[v]:                     
                if w not in self.explored: 
                    self.explored.append(w)
                    Q.append(w) 
                    
        if is_shortest:
            distance = self.distance()
            return (self.explored, distance)     
        return self.explored

    def distance(self) -> int:
        return len(self.explored) - 1

    def DFS(self, start_node: int=0) -> list[int]:
        """
        Depth-first search algorithm (recursive)
        """
        assert type(start_node) == int, f"Node type({start_node}) must be an integer"

        if start_node not in self.explored:
            self.explored.append(start_node)

        for i in self.graph[start_node]:
            if i not in self.explored:
                self.explored.append(i)
                self.DFS(i)
        
        return self.explored

gs = GraphSearch()
print(gs.graph)
print("")
print(gs.adjacency_matrix)
print("")
print(gs.BFS(0, 7, True))
