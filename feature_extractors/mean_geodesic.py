import numpy as np

def mean_geodesic_distance(G,weighted=True):
    """
    input: python i-graph Graph object
    output: the mean geodesic distance (shortest path) of graph G
    """
    if weighted:
        weights = "weight" # an attribute for edge weight. You may change this depending on the gml file
    else:
        weights = None

    # a list of distances
    ds = []
    for i,v in enumerate(G.vs):
        path_lengths = G.shortest_paths(v,weights=weights)[0]
        # since diagonal element is 0 (the distance of self loop is 0), delete the element
        del path_lengths[i]
        ds += path_lengths

    return np.average(ds)
