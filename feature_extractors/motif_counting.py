"""
The algorithm is based on a paper "Fast Parallel Graphlet Counting for Large
Networks" by Ahmed et al. http://arxiv.org/abs/1506.04322
"""

import numpy as np
import scipy.misc as scm


def motif_census(G):

    # frequencies for k = 3 motifs
    for i in range(1,4):
        exec("g3_%d = 0"%i)

    # just for explicitness
    g3_1 = 0
    g3_2 = 0
    g3_3 = 0

    # frequencies for k = 4 motifs
    for i in range(1,12):
        exec("g4_%d = 0"%i)

    #Initialize numpy array X
    X = np.zeros(len(G.vs))

    num_of_vertices = len(G.vs)
    num_of_edges = len(G.es)

    N_T_T = np.zeros(num_of_edges);      N_Su_Sv = np.zeros(num_of_edges)
    N_T_SuVSv = np.zeros(num_of_edges);  N_S_S = np.zeros(num_of_edges)
    N_T_I = np.zeros(num_of_edges);      N_SuVSv_I =np.zeros(num_of_edges)
    N_I_I = np.zeros(num_of_edges);      N_I_I_1 = np.zeros(num_of_edges)

    # This for loop can be paralleled according to the authors
    for e in G.es:
        u,v = e.tuple
        Star_u = set(); Star_v = set(); Tri_e = set()
        
        N_u = set(G.neighbors(u))
        N_v = set(G.neighbors(v))
        
        for w in N_u:
            if w == v: continue
            Star_u.add(w); X[w] = 1

        for w in N_v:
            if w == u: continue
            if X[w] == 1:
                Tri_e.add(w); X[w] = 2
                Star_u.remove(w)
            else:
                Star_v.add(w); X[w] = 3

        g3_1 += len(Tri_e)
        g3_2 += len(Star_u) + len(Star_v)
        g3_3 += num_of_vertices - len(N_u.union(N_v))



    g3_1 = g3_1/3.0
    g3_2 = g3_2/2.0
    g3_4 = scm.comb(num_of_vertices,3,1) - g3_1 - g3_2 -g3_3

    return [g3_1,g3_2,g3_3,g3_4]