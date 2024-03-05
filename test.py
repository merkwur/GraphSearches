from graph import Graph
from generators import random_graph

G = Graph(False)
G.add_edges(random_graph(5, 12))
adj = G.update_adjacency_view()
print(adj)



