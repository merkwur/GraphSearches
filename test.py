from graph import Graph
from generators import random_graph, fast_random_graph

G = Graph(False)
G.add_edges(fast_random_graph(5, .8))
adj = G.update_adjacency_view()
print(adj)



