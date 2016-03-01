import numpy as np

def mean_geodesic_distance(G):
    """
    input: python i-graph Graph object
    output: the mean geodesic distance (shortest path) of graph G
    """

    # a list of distances
    ds = []
    for i,v in enumerate(G.vs):
        path_lengths = G.shortest_paths(v,weights=None)[0]
        # since diagonal element is 0 (the distance of self loop is 0), delete the element
        del path_lengths[i]
        ds += path_lengths

    return np.nanmean(ds)
