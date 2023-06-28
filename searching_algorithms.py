# !usr/bin/python3.10
# https://www.coursera.org/learn/algorithms-graphs-data-structures/

import utils
from draw import draw_network 
from graph import Graph
import matplotlib.pyplot as plt

class GraphSearch:

    def __init__(self, graph: dict, matrix: bool = False):
        self.graph = graph
        if matrix:
            self.adjacency_matrix = matrix
        self.BFSExplored = []
        self.DFSExplored = []
        
    def BFS(self, start_node: int, end_node: int=0, is_shortest: bool=False) -> tuple[list[int], int] or list[int]: 
        """
        Breadth-first searching algorithm 
        """
        assert type(start_node) == int, f"Node type({start_node}) must be an integer"
        assert type(end_node) == int, f"Node type({end_node}) must be an integer"
    
        Q = [start_node]
        self.BFSExplored.append(start_node)

        while Q:
            if end_node and end_node in self.BFSExplored:
                break
            
            v = Q.pop(0)
            
            for w in self.graph[v]:                     
                if w not in self.BFSExplored: 
                    self.BFSExplored.append(w)
                    Q.append(w) 


        if is_shortest:       
            return (self.BFSExplored, self.distance(end_node))     
        return self.BFSExplored


    def DFS(self, start_node: int=3, is_distance: bool=False) -> list[int]:
        """
        Depth-first search algorithm (recursive)
        """
        assert type(start_node) == int, f"Node type({start_node}) must be an integer"
        
        if is_distance:
            self.DFSExplored = []

        if start_node not in self.DFSExplored:
            self.DFSExplored.append(start_node)

        # print(self.DFSExplored)

        for i in self.graph[start_node]:
            if i not in self.DFSExplored:
                self.DFSExplored.append(i)
                self.DFS(i)
        
        return self.DFSExplored



g = Graph()
G = g.create_graph([(0, 1), (2, 0), (1, 2), (2, 3), (2, 4), (2, 7), 
                    (3, 4), (4, 5), (5, 6), (6, 3), (4, 6), (4, 8), 
                    (4, 5), (7, 10), (8, 10), (10, 9), (9, 8)
                    ], True)
gs = GraphSearch(G)


points = utils.random_layout(G)
draw_network(G, points)






# print("DepthFirstSearch", gs.DFS(0))
