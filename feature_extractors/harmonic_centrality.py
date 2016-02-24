#
#   For graph object G
#   harmonic_centrality(G) returns sum of differences of harmonic centrality from maximally central vertex
#   with all others, divided by this sum of differences on a N-star, which will be (N - 2) / 2
#
#   See Freeman's centrality measure extensions to whole networks.
#   Implimented for harmonic centrality by E. Tucker
#

import igraph
import os
import sys


def harmonic_centrality(G):
    V_set = G.vs()
    N = len(V_set)

#################################
#CALCULATE HARMONIC CENTRALITIES#
#################################

    centralityList= []
    for i in range(0, N):
        centralityList.append(0.0)
    for u in (V_set):
        u_index = u.index
        distances = G.shortest_paths(u,weights=None)[0]
        inverseDist = []
        sum_uw = 0.0
        for i in range(0, N):
            d_inv = 0.0         # inverse of distances.  will be zero for self, and for nonconnected vertices.
            if i != u_index:
                d_inv = (1.0 / distances[i])
            inverseDist.append(d_inv)
        for dist in inverseDist:
            sum_uw = sum_uw + dist
        centralityList[u_index] = (1.0 / (N - 1)) * sum_uw

############################################################################
#CALCULATE SUM OF DIFFERENCES BETWEEN MAXIMALLY CENTRAL ELEMENT WITH OTHERS#
############################################################################

    max_c = max(centralityList)
    sum_diff = 0.0
    for centrality in centralityList:
        difference = max_c - centrality
        sum_diff = sum_diff + difference

##################################################################
#DIVIDE BY SUM_DIFF ON STAR WITH N VERTICES. THIS VALUE COMES TO:#
##################################################################

    denominator = (N - 2) / 2.0

    harmonic_centrality = sum_diff / denominator

    return harmonic_centrality

