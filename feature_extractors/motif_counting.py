"""
The algorithm is based on a paper "Fast Parallel Graphlet Counting for Large
Networks" by Ahmed et al. http://arxiv.org/abs/1506.04322
"""

import igraph
import numpy as np
import scipy.misc as scm
import copy
import matplotlib.pyplot as plt
import multiprocessing as mp


NUM_PROCESSES = 100

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

def parallel(G,V,E,e):
    """
    This function is used for replacing the for loop in the motif census
    function with multiprocessing.
    """

    """
    In order to use Pool, an object being passed to target function must
    be "picklable".
    """
    # Initialize numpy array X
    X = np.zeros(len(G.vs))

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

    g3_1 = len(Tri_e)
    g3_2 = len(Star_u) + len(Star_v)
    g3_3 = V - len(N_u.union(N_v))

    # get counts of 4-cliques & 4-cycles
    g4_1 = clique_count(G,X,Tri_e)
    g4_4 = cycle_count(G,X,Star_u)

    # get unrestricted counts for 4-node connected motifs
    N_T_T = scm.comb(len(Tri_e),2,1)
    N_Su_Sv = len(Star_u)*len(Star_v)
    N_T_SuVSv = len(Tri_e)*(len(Star_u)+len(Star_v))
    N_S_S = scm.comb(len(Star_u),2,1) + scm.comb(len(Star_v),2,1)

    # get unrestricted counts for 4-node disconnected motifs
    N_T_I = len(Tri_e)*(V - len(N_u.union(N_v)))
    N_Su_I = len(Star_u)*(V - len(N_u.union(N_v)))
    N_Sv_I = len(Star_v)*(V - len(N_u.union(N_v)))
    N_SuVSv_I = N_Su_I + N_Sv_I
    N_I_I = scm.comb((V - len(N_u.union(N_v))),2,1)
    N_I_I_1 = E - len(N_u.difference([v])) - len(N_v.difference([u])) - 1

    for w in N_v:
        X[w] = 0

    output.put([g3_1, g3_2, g3_3, g4_1, g4_4, N_T_T, N_Su_Sv, N_T_SuVSv,\
            N_S_S, N_T_I, N_SuVSv_I, N_I_I, N_I_I_1])

def motif_census_parallel(G):
    # frequencies for k = 3 motifs
    for i in range(1,4):
        exec("g3_%d = 0"%i)

    # frequencies for k = 4 motifs
    for i in range(1,12):
        exec("g4_%d = 0"%i)

    V = len(G.vs)  # number of vertices
    E = len(G.es)  # number of edges
    pool = mp.Pool(processes=4)
    results = [pool.apply(parallel,args=(G,V,E,e)) for e in G.es]
    """
    processes = [mp.Process(target=parallel, args=(G,V,E,e)) for e in G.es]
    # Run processes
    for p in processes:
        p.start()

    for p in processes:
        p.join()

    results = [output.get() for p in processes]
    """
    g3_1 = reduce(lambda x,L: L[0]+x, results, 0)
    g3_2 = reduce(lambda x,L: L[1]+x, results, 0)
    g3_3 = reduce(lambda x,L: L[2]+x, results, 0)
    g4_1 = reduce(lambda x,L: L[3]+x, results, 0)
    g4_4 = reduce(lambda x,L: L[4]+x, results, 0)

    N_T_T = reduce(lambda x,L: L[5]+x, results, 0)
    N_Su_Sv = reduce(lambda x,L: L[6]+x, results, 0)
    N_T_SuVSv = reduce(lambda x,L: L[7]+x, results, 0)
    N_S_S = reduce(lambda x,L: L[8]+x, results, 0)
    N_T_I = reduce(lambda x,L: L[9]+x, results, 0)
    N_SuVSv_I = reduce(lambda x,L: L[10]+x, results, 0)
    N_I_I = reduce(lambda x,L: L[11]+x, results, 0)
    N_I_I_1 = reduce(lambda x,L: L[12]+x, results, 0)

    g3_1 = g3_1/3.0
    g3_2 = g3_2/2.0
    g3_4 = scm.comb(V,3,1) - g3_1 - g3_2 -g3_3

    g4_1 = g4_1/6.0
    g4_2 = N_T_T - 6*g4_1
    g4_3 = ((N_T_SuVSv) - 4*g4_2)/2.0
    g4_4 = g4_4/4.0
    g4_5 = ((N_S_S) - g4_3)/3.0
    g4_6 = N_Su_Sv - 4*g4_4
    g4_7 = (N_T_I - g4_3)/3.0
    g4_8 = (N_SuVSv_I - 2*g4_6)/2.0
    g4_9 = (N_I_I_1 - (6*g4_1 + 4*g4_2 + 2*g4_3) - (4*g4_4 + 2*g4_6))/2.0
    g4_10 = N_I_I - 2*g4_9
    g4_11 = scm.comb(V,4,1) - sum([eval("g4_%d"%i) for i in range(1,11)])

    return [eval("g3_%d"%i) for i in range(1,5)] + [eval("g4_%d"%i) for i in range(1,12)]


def motif_census(G_filepath,rewire=False):
    G = igraph.read(G_filepath)
    if rewire:
        G.rewire()
    G.simplify()
    G.to_undirected()
    # frequencies for k = 3 motifs
    for i in range(1,4):
        exec("g3_%d = 0"%i)

    # frequencies for k = 4 motifs
    for i in range(1,12):
        exec("g4_%d = 0"%i)

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

    g4_1 = g4_1/6.0
    g4_2 = N_T_T - 6*g4_1
    g4_3 = ((N_T_SuVSv) - 4*g4_2)/2.0
    g4_4 = g4_4/4.0
    g4_5 = ((N_S_S) - g4_3)/3.0
    g4_6 = N_Su_Sv - 4*g4_4
    g4_7 = (N_T_I - g4_3)/3.0
    g4_8 = (N_SuVSv_I - 2*g4_6)/2.0
    g4_9 = (N_I_I_1 - (6*g4_1 + 4*g4_2 + 2*g4_3) - (4*g4_4 + 2*g4_6))/2.0
    g4_10 = N_I_I - 2*g4_9
    g4_11 = scm.comb(V,4,1) - sum([eval("g4_%d"%i) for i in range(1,11)])

    return [eval("g3_%d"%i) for i in range(1,5)] + [eval("g4_%d"%i) for i in range(1,12)]


def random_motif_census(G_filepath):

    pool = mp.Pool(processes=NUM_PROCESSES)
    matrix = [pool.apply(motif_census, args=(G_filepath,True)) for i in xrange(1000)]

    matrix = np.array(matrix)
    filename = G_filepath.split("/")[-1]
    np.savetxt("motif_distribution/"+filename+".txt",matrix,fmt="%d",delimiter=',')
    matrix_T = matrix.T

    #for motif in matrix_T:
        #distribution_plot(motif)

    mean = np.mean(matrix, axis=0)
    std = np.std(matrix,axis=0)

    pool.close()
    pool.join()

    return (mean,std)

def distribution_plot(motif):
    plt.hist(motif,bins=50,normed = False)
    plt.xlabel("Counting")
    plt.ylabel("Frequency")
    plt.show()

def motif_significance(G_filepath):

    G_motif = motif_census(G_filepath)
    filename = G_filepath.split("/")[-1]
    np.savetxt("motif_counts/"+filename+".txt",G_motif,fmt="%d",delimiter=',')
    new_G_motif_mean, new_G_motif_std = random_motif_census(G_filepath)
    diff = map(lambda (x,y): x-y ,zip(G_motif,new_G_motif_mean))
    Z_score = map(lambda (x,y): round(x/float(y),2) if y > 0 else x ,zip(diff,new_G_motif_std))

    return Z_score
