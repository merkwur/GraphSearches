# !usr/bin/python3.10
# https://www.coursera.org/learn/algorithms-graphs-data-structures/

import utils
from collections import defaultdict
from draw import draw_graph 
from graph import Graph
import matplotlib.pyplot as plt


class GraphSearch:

    def __init__(self, graph: dict, matrix: bool = False):
        self.graph = graph
        if matrix:
            self.adjacency_matrix = matrix
        self.BFSExplored = []
        self.DFSExplored = []
        self.k_stack = []
        self.reversed_graph = Graph()
        self.SCC = defaultdict(list)
        self.kosaraju_explored = []
        self.strong_comp = 0
        
        
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


    def DFS(self, start_node: int = 0, sccs=False) -> list[int]:
        """
        Depth-first search algorithm (recursive)
        """
        assert type(start_node) == int, f"Node type({start_node}) must be an integer"

        if start_node not in self.DFSExplored:
            self.DFSExplored.append(start_node)

        if not sccs:
            for i in self.graph[start_node]:
                if i not in self.DFSExplored:
                    self.DFSExplored.append(i)
                    self.DFS(i)
                self.reverse_graph(i, start_node)

                # fills the stack for Kosaraju's Algorithm
                if self.DFSExplored[-1] not in self.k_stack:
                    self.k_stack.append(self.DFSExplored[-1])
        
        else: 
            
            for i in self.reversed_graph.graph[start_node]:
                if len(self.reversed_graph.graph[start_node]) == 0:
                    
                    self.SCC[self.strong_comp].append([])
                if i not in self.kosaraju_explored:
                    self.kosaraju_explored.append(i)
                    self.SCC[self.strong_comp].append(i)
                    self.DFS(i, True)
                    self.strong_comp += 1
                    
    
    def kosaraju(self):
        self.DFS(0)
        self.complete_stack()

    def complete_stack(self):
        for i in reversed(self.DFSExplored):
            if i not in self.k_stack:
                self.k_stack.append(i)

    def reverse_graph(self, a, b):
        self.reversed_graph.add_edges([(a, b)], True)
        
    def reverse_traverse(self):
        for i in reversed(self.k_stack):
            if i not in self.kosaraju_explored:
                self.DFS(i, True)
            

        




        


g = Graph()
G = g.add_edges([(0, 1), (1, 2), (2, 3), (3, 0), (2, 4), (4, 5), (5, 6), (6, 4), (6, 7)], True)
gs = GraphSearch(G)
gs.kosaraju()
gs.reverse_traverse()


points = utils.random_layout(G)
print(g.graph)
print(gs.k_stack)
print(gs.DFSExplored)
print(gs.reversed_graph.graph)
print(gs.SCC)


# draw_graph(G, points)





# print("DepthFirstSearch", gs.DFS(0))
