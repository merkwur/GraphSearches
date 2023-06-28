# !usr/bin/python3.10
# https://www.coursera.org/learn/algorithms-graphs-data-structures/

from graph import Graph
import matplotlib.pyplot as plt

class GraphSearch:

    def __init__(self, graph, matrix):
        self.graph = graph
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

    def distance(self, end_node: int) -> int:
        """
        Calculates the shortest distance from start node to end node. 
        Sort of backtraces from the last node's which if is not the end node of the whole graph.
        """
        
        for i in self.BFSExplored[1:]:
            self.dist += 1            
            if len(self.graph[i]) > 1:
                for j in self.graph[i]:
                    d = self.DFS(j, True)
                    self.dist -= len(d) if d[-1] != end_node else 0

        return self.dist


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

gs = GraphSearch(g.create_graph([(0, 1), (2, 1), (1, 2), (1, 3), (2, 4), (1, 4)], True), g.create_adjacency_matrix())

print(gs.graph)
# print("")
# # print(gs.adjacency_matrix)
# plt.matshow(gs.adjacency_matrix)
# plt.show()
# print("")
# # print("BradthFirstSearch", gs.BFS(0, 7, True))
print("DepthFirstSearch", gs.DFS(0))
