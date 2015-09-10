import numpy as np

def mean_degree(G,mode="ALL"):
    """
    input: python i-graph Graph object
    output: the mean degree of graph G
    """
    deg_seq = G.degree(G.vs,mode=mode)
    return np.average(deg_seq)

def mean_in_degree(G):
    return mean_degree(G, mode="IN")

def mean_out_degree(G):
    return mean_degree(G, mode="OUT")
