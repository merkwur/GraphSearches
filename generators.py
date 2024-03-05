import random 
from typing import Sequence

def random_graph(v: int, e: int | None = None, satiation: float =.2) -> Sequence[tuple[int, int]]: 
    if not e: e = v + 1
    satiations = dict.fromkeys(range(v), 0)
    edges = []
    while e > 0:
        for i in range(v): 
            j = list(range(v))
            j.remove(i)
            j = random.choice(j)
            p = random.random()

            if ((satiations[i] + satiations[j]) / 2) < p and i != j: 
                edges.append((i, j))
                satiations[i] += satiation
                satiations[j] += satiation
                e -= 1

    return edges



def erdos_renyi():
    pass