#######################################################################
# input: python i-graph Graph object
# output: closeness centrality with respect to whole graph.
# sum differences between maximally closeness-central vertex with all other vertices' c-centrality, and
# normalize with respect to the summed differences on a maximally c-central network (a star).
# see Freeman's "Centrality in Social Networks Conceptual Clarification"
#######################################################################



import igraph

def closeness_centrality(G):
    
    closeness_seq = G.closeness(vertices=None, mode=3, cutoff=None, weights=None, normalized=True)
    max_c = max(closeness_seq)
    cent_diff = 0.0
    
    for score in closeness_seq:
        each_diff = max_c - score
        cent_diff = cent_diff + each_diff
    
    n = len(G.vs())
    denominator = ((n ** 2.0) - (3 * n) + 2) / ((2 * n) - 3)
    d_centrality = cent_diff / denominator

    return d_centrality