"""
    
For graph object G
estrada_index(G) returns (sum e^(eig_i)) for all eigenvalues eig_i)

"""

import numpy.linalg
from igraph import *
import numpy as np

def estrada_index(G):
    
    adjacencyMatrix = numpy.array(list(G.get_adjacency()))
    spectrum = numpy.linalg.eigvals(adjacencyMatrix)
    estradaIndex = 0
    for eigenvalue in spectrum:
        estradaIndex += np.exp(eigenvalue)
    return estradaIndex