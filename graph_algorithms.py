from graph import Graph
from typing import Sequence


class GraphAlgorithms(Graph):
    def __init__(self, nodes):
        super().__init__()
        self.is_visited: set[int] = set()
        self.graph: Sequence[tuple] = self.add_edges(nodes)
        self.adjacency_list: dict[list] = self.adjacency_view()
        print(self.adjacency_list)

    # make callable outside the class
    def depth_first(self, starting_node: int) -> set[int]:

        """
        Performs a depth-first search (DFS) starting from the given node in the graph. 
        This method traverses the graph layer-wise and records the order of visited nodes.

        Parameters:
        - starting_node (int): The node from which the BFS should start. This node 
                               should be a valid integer and exist in the graph's adjacency list
        

        Raises:
        - ValueError: If the starting_node is None.
        - TypeError: If the starting_node is not an integer.
        - KeyError: If the starting_node does not exist in the graph's adjacency list.

        Returns:
        - set: A set of nodes which they were visited during the DFS.

        Note:
        The method uses the recursive call for traversing the whole graph.
        """

        if starting_node is None:
            raise ValueError("To perform the DFS, starting node needs to be given.")
        
        if not isinstance(starting_node, int):
            raise TypeError(f"Node type({type(starting_node)}) must be an integer.")

        if starting_node not in self.adjacency_list:
            raise KeyError(f"Node {starting_node} is not in the adjacency list.")

        if starting_node in self.is_visited:
            return

        self.is_visited.add(starting_node)

        for node in self.adjacency_list[starting_node]:            
            self.depth_first(node)

        return self.is_visited
        
    def breadth_first(self, starting_node: int, order: bool = False) -> list[int]:
        """
        Performs a breadth-first search (BFS) starting from the given node in the graph. 
        This method traverses the graph layer-wise and records the order of visited nodes.

        Parameters:
        - starting_node (int): The node from which the BFS should start. This node 
                               should be a valid integer and exist in the graph's adjacency list
        - order (bool): decides to return either "ordered" visited nodes list or visited node list

        Raises:
        - ValueError: If the starting_node is None.
        - TypeError: If the starting_node is not an integer.
        - KeyError: If the starting_node does not exist in the graph's adjacency list.

        Returns:
        - list: A list of nodes which they were visited during the BFS.

        Note:
        The method uses a queue to manage the nodes during traversal and a set to keep track of visited nodes.
        """

        if starting_node is None:
            raise ValueError("To perform the BFS, starting node needs to be given.")
        
        if not isinstance(starting_node, int):
            raise TypeError(f"Node type({type(starting_node)}) must be an integer.")

        if starting_node not in self.adjacency_list:
            raise KeyError(f"Node {starting_node} is not in the adjacency list.")
        
        queue = [starting_node]
        visited = set([starting_node])
        visited_order = []

        while queue:
            v = queue.pop(0)
            visited_order.append(v)
            
            for u in self.adjacency_list[v]:                     
                if u not in visited: 
                    visited.add(u)
                    queue.append(u) 
        
        if order:
            return visited_order
        else: return visited
                    
    def a_star(self):
        pass
        
    def djikstra(self):
        pass
    
    def bellman_ford(self):
        pass

    def hopcroft_karp(self):
        pass








graph = [(0, 1), (1, 2),(0, 2), (2, 3), (1, 3), (1, 4), (4, 5), (5, 3), (2, 6), (6, 7)]
G = Graph(False)
GA = GraphAlgorithms(G.adjacency_view())
G.add_edges(graph)
# print(G.graph)
# print(G.adjacency_view())
# print(G.adjacency_matrix_view())
GA.depth_first(0) 
print(GA.is_visited)

























# bellman ford
# hopcroft karp
# djikstra
# A*