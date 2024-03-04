
import numpy as np

def random_layout(G: dict, center: tuple[float | int] = None, dim: int = 2, min_dist: float = 20.) -> list[list, list]:
    points = [[], []]
    M = max(G.keys())
    for i in G.keys():
        points[0].append(int(i + np.random.uniform(M - M/4, i + M + M /4, dim)[0] * min_dist))
        points[1].append(int(i + np.random.uniform(M - M/4, i + M + M /4, dim)[1] * min_dist))
    return points

def grid_layout(G):
    l = len(G.keys())
    p = np.random.binomial(1, .72, (l, l))
    return [(np.sum(p, axis=0) + np.random.randint(0, l//2, l)).tolist(), (np.sum(p, axis=1)+ np.random.randint(0, l//2, l)).tolist()]



