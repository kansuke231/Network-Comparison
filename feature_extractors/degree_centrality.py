#######################################################################
# input: python i-graph Graph object
# output: degree centrality with respect to whole graph.
# sum differences between maximally degree-central vertex with all other vertices' d-centrality, and
# normalize with respect to the summed differences on a maximally d-central network (a star).
# see Freeman's "Centrality in Social Networks Conceptual Clarification"
#######################################################################


def degree_centrality(G):
    
    degrees = G.degree(G.vs())
    
    max_c = max(degrees)
    cent_diff = 0.0
    
    for score in degrees:
        each_diff = max_c - score
        cent_diff = cent_diff + each_diff
    
    n = len(G.vs())

    denominator = ((n ** 2) - (3 * n) + 2)

    d_centrality = cent_diff / denominator

    return d_centrality
