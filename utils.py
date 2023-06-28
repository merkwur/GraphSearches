# influenced from networkz drawing.
import numpy.random as npr

def random_layout(G: dict, center: tuple[float or int] = None, dim: int = 2, min_dist: float = 10.) -> list[list, list]:
    points = [[], []]
    for i in G.keys():
        points[0].append(int(npr.uniform(max(G.keys()) - max(G.keys())/4, max(G.keys()) + max(G.keys())/4, dim)[0] * min_dist))
        points[1].append(int(npr.uniform(max(G.keys()) - max(G.keys())/4, max(G.keys()) + max(G.keys())/4, dim)[1] * min_dist))
    return points


