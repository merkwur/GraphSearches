# usr/bin/python3.10

from collections import defaultdict
from collections.abc import Sequence
import numpy as np
from functools import lru_cache


class Graph: 
    def __init__(self, is_directed: bool = False):
        self.graph: Sequence[tuple[int, int]] = []
        self.adjacency_view = defaultdict(list)
        self.adjacency_matrix: np.ndarray = None
        self.is_directed: bool = is_directed

    def add_edges(self, edges: Sequence[tuple[int, int]]) -> Sequence[tuple[int, int]]:
        self.update_adjacency_view.cache_clear()
        for edge in edges: 
            if edge not in self.graph:
                self.graph.append(edge)

    def add_edge(self, edge: tuple[int, int]) -> Sequence[tuple[int, int]]:
        if (edge not in self.graph): 
            self.update_adjacency_view.cache_clear()
            self.graph.append(edge)

    @lru_cache
    def update_adjacency_view(self) -> dict: 
        for f, t in self.graph:
            print(f"in the loop {f}, {t}")
            # if is directed add "to" vertex in to "from"s neighs and vice versa
            if (not self.is_directed): 
                if t not in self.adjacency_view[f]: 
                    self.adjacency_view[f].append(t)
                if f not in self.adjacency_view[t]:
                    self.adjacency_view[t].append(f)
            # otherwise add only "to" vertex to "from"s vertex neighs
            else: 
                if t not in self.adjacency_view[f]:
                    self.adjacency_view[f].append(t)
        return self.adjacency_view
    
    def update_adjacency_matrix(self, adjacency_view: dict | None) -> np.ndarray: 
        if adjacency_view:
            adjacency = adjacency_view
        else: 
            adjacency = self.update_adjacency_view()
        n = len(adjacency)
        self.adjacency_matrix = np.zeros((n, n))
        for v in adjacency: 
            for u in adjacency[v]: 
                self.adjacency_matrix[v][u] = 1
        return self.adjacency_matrix
    





            
            



    

