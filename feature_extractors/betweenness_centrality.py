######################################################################
#   input: python i-graph Graph object
#   output: betweenness centrality with respect to whole graph.
#   sum differences between maximally between-central vertex with all other vertices' b-centrality, and
#   normalize with respect to the summed differences on a maximally b-central network.
#    see Freeman's "Centrality in Social Networks Conceptual Clarification"
######################################################################



import igraph

def betweenness_centrality(G):

    betweenness = G.betweenness()
    max_c = max(betweenness)
    cent_diff = 0.0
    for score in betweenness:
        each_diff = max_c - score
        cent_diff = cent_diff + each_diff
    
    n = len(G.vs())


    denominator = ((n ** 3) - (4 * (n ** 2)) + (5 * n) - 2)

    b_centrality = cent_diff / denominator

    return b_centrality

