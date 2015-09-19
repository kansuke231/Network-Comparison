"""
The algorithm is based on a paper "Fast Parallel Graphlet Counting for Large
Networks" by Ahmed et al. http://arxiv.org/abs/1506.04322
"""

import numpy as np
import scipy.misc as scm

def clique_count(G,X,Tri_e):
    cliq_e = 0
    for w in Tri_e:
        for r in G.neighbors(w):
            if X[r] == 2:
                cliq_e += 1
        X[w] = 0
    return cliq_e

def cycle_count(G,X,Star_u):
    cyc_e = 0
    for w in Star_u:
        for r in G.neighbors(w):
            if X[r] == 3:
                cyc_e += 1
        X[w] = 0
    return cyc_e


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
    g4_1 = 0
    g4_4 = 0

    # Initialize numpy array X
    X = np.zeros(len(G.vs))

    V = len(G.vs)  # number of vertices
    E = len(G.es)  # number of edges

    N_T_T = 0;      N_Su_Sv = 0
    N_T_SuVSv = 0;  N_S_S = 0
    N_T_I = 0;      N_SuVSv_I =0
    N_I_I = 0;      N_I_I_1 = 0

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
        g3_3 += V - len(N_u.union(N_v))

        # get counts of 4-cliques & 4-cycles
        g4_1 += clique_count(G,X,Tri_e)
        g4_4 += cycle_count(G,X,Star_u)

        # get unrestricted counts for 4-node connected motifs
        N_T_T += scm.comb(len(Tri_e),2,1)
        N_Su_Sv += len(Star_u)*len(Star_v)
        N_T_SuVSv += len(Tri_e)*(len(Star_u)+len(Star_v))
        N_S_S += scm.comb(len(Star_u),2,1) + scm.comb(len(Star_v),2,1)
        
        # get unrestricted counts for 4-node disconnected motifs
        N_T_I += len(Tri_e)*(V - len(N_u.union(N_v)))
        N_Su_I = len(Star_u)*(V - len(N_u.union(N_v)))
        N_Sv_I = len(Star_v)*(V - len(N_u.union(N_v)))
        N_SuVSv_I += N_Su_I + N_Sv_I
        N_I_I += scm.comb((V - len(N_u.union(N_v))),2,1)
        N_I_I_1 += E - len(N_u.difference([v])) - len(N_v.difference([u])) - 1

        for w in N_v:
            X[w] = 0


    g3_1 = g3_1/3.0
    g3_2 = g3_2/2.0
    g3_4 = scm.comb(V,3,1) - g3_1 - g3_2 -g3_3

    g4_2 = N_T_T - 6*g4_1
    g4_3 = (N_T_SuVSv)/2.0 - 2*g4_2
    g4_5 = (N_S_S)/3.0 - g4_3/3.0
    g4_6 = N_Su_Sv - 4*g4_4
    g4_7 = N_T_I/3.0 - g4_3/3.0
    g4_8 = N_SuVSv_I/2.0 - g4_6
    g4_9 = (N_I_I_1 - (6*g4_1 + 4*g4_2 + 2*g4_3) - (4*g4_4 + 2*g4_6))/2

    g4_10 = N_I_I - 2*g4_9 # Something is wrong here.
    g4_11 = scm.comb(V,4,1) - sum([eval("g4_%d"%i) for i in range(1,11)])

    return [g3_1,g3_2,g3_3,g3_4] + [eval("g4_%d"%i) for i in range(1,12)]