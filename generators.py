import random, math 
from typing import Sequence


def random_graph(vertex_count: int, edge_count: int | None = None, satiation: float =.2) -> Sequence[tuple[int, int]]: 
    if not edge_count: edge_count = vertex_count + 1
    satiations = dict.fromkeys(range(vertex_count), 0)
    edges = []
    max_counter = 0
    while edge_count > 0 and max_counter < vertex_count * 5:
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
        max_counter += 1
    return edges


def fast_random_graph(n, p):
    """
    from networkx fast_gnp_random_graph() function copy.

    References from Networkx
    ----------
    .. [1] Vladimir Batagelj and Ulrik Brandes,
        "Efficient generation of large random networks",
        Phys. Rev. E, 71, 036113, 2005.
    """

    lp = math.log(1. - p)
    edges = []
    v = 1
    w = -1
    while v < n:
        lr = math.log(1.0 - random.random())
        w = w + 1 + int(lr / lp)
        while w >= v and v < n:
            w = w - v
            v = v + 1
        if v < n:
            edges.append((v, w))
    return edges