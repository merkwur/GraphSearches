# !usr/bin/python3.10

# https://www.coursera.org/learn/algorithms-graphs-data-structures/
# https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/


import numpy as np
import graph 

class GraphSearch:
    
    # initialize the graph here

    g = graph.Graph()
    g.addEdge(0, 1)
    g.addEdge(1, 2)
    g.addEdge(2, 4)
    g.addEdge(3, 0)
    g.addEdge(3, 4)
    g.addEdge(4, 5)
    g.adjecency_matrix() # for the backtracing algorithm, it is necessary

    def __init__(self):
        self.graph = self.g.graph
        self.adjecency_matrix = self.g.adj_matrix
        self.explored = []

    def BFS(self, start_node: int, end_node: int=0, is_shortest: bool=False) -> tuple[list[int], int]: 
        """
        Breadth first searching algorithm 
        """
        try:
            assert type(start_node) == int
        except AssertionError:
            print(f"Node type ({start_node}) must be an integer")

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

        distance = self.back_tracing(start_node, end_node)
        return (self.explored, distance )     

    def back_tracing(self, start_node, end_node):
        """
        Finds the shortest path between two nodes using adjecency matrix.
        """
        distance = 0
        for i in range(end_node, 0, -1):
            back = self.adjecency_matrix[i] 
            distance += 1
            for j in np.where(back>0)[0]:
                if j == start_node:
                    return distance
        return distance

    def DFS(self, start_node: int=0) -> list[int]:
        """
        Depth first search algorithm (recursive)
        """
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
print(gs.adjecency_matrix)
print("")
print(gs.DFS())
