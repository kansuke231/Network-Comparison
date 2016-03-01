#
#   For graph object G
#   pagerank_centrality(G) returns sum of differences of pagerank centrality from maximally central vertex
#   with all others, divided by this sum of differences on a N-star with in_degree N-1 for center vertex.
#
#   See 'Centrality in Social Networks Conceptual Clarification' (Freeman '78) for centrality measure extensions to whole networks.
#   Implimented for pagerank centrality by E. Tucker
#

import igraph

def pagerank_centrality(G):

    rankings = G.pagerank(vertices=None, directed=True, damping=0.85, weights=None, arpack_options=None, implementation='prpack', niter=1000, eps=0.001)
    max_c = max(rankings)
    sum_diff = 0.0
    for score in rankings:
        difference = max_c - score
        sum_diff = sum_diff + difference

############################################################
#CREATE DIRECTED N-STAR WITH CENTER HAVING IN_DEGREE OF N-1#
############################################################

    N = len(G.vs())

    N_Star = igraph.Graph.Star(N, mode="in", center=0)
    star_rankings = N_Star.pagerank(vertices=None, directed=True, damping=0.85, weights=None, arpack_options=None, implementation='prpack', niter=1000, eps=0.001)
    max_c_star = max(star_rankings)
    star_diff = 0.0
    for score in star_rankings:
        difference = max_c_star - score
        star_diff = star_diff + difference


    pagerankCentrality = sum_diff / star_diff

    return pagerankCentrality