import random 

def random_graph(v, e, satiation=.2): 
    
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