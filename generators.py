import random 
from typing import Sequence

def random_graph(vertex_count: int, edge_count: int | None = None, satiation: float =.2) -> Sequence[tuple[int, int]]: 
    if not edge_count: edge_count = vertex_count + 1
    satiations = dict.fromkeys(range(vertex_count), 0)
    edges = []
    while edge_count > 0:
        for i in range(vertex_count): 
            j = list(range(vertex_count))
            j.remove(i)
            j = random.choice(j)
            p = random.random()

            if ((satiations[i] + satiations[j]) / 2) < p and i != j: 
                edges.append((i, j))
                satiations[i] += satiation
                satiations[j] += satiation
                edge_count -= 1

    return edges

def erdos_renyi():
    pass