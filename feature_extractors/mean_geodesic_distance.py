import numpy as np
import random

def mean_geodesic_distance(G):
    """
    input: python i-graph Graph object
    output: the mean geodesic distance (shortest path) of graph G
    """

    # a list of distances
    ds = []
    N = len(G.vs)
    # if a network is small enough
    if N < 10000:
        for i,v in enumerate(G.vs):
            path_lengths = G.shortest_paths(v,weights=None)[0]
            # since diagonal element is 0 (the distance of self loop is 0), delete the element
            del path_lengths[i]
            ds.append(np.nanmean(path_lengths))
    
    # if it's really big
    else:
        for i,v in enumerate(random.sample(G.vs, int(N*0.01))):
            path_lengths = G.shortest_paths(v,weights=None)[0]
            # since diagonal element is 0 (the distance of self loop is 0), delete the element
            del path_lengths[i]
            ds.append(np.nanmean(path_lengths))

    return np.nanmean(ds)

