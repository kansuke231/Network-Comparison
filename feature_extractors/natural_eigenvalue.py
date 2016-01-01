"""
    
For graph object G
natural_eigenvalue(G) returns (log(Estrada's Index / #vertices))

"""

import numpy.linalg
from igraph import *
import numpy as np

def natural_eigenvalue(G):
    
    adjacencyMatrix = numpy.array(list(G.get_adjacency()))
    spectrum = numpy.linalg.eigvals(adjacencyMatrix)
    estradaIndex = 0
    for eigenvalue in spectrum:
        estradaIndex += np.exp(eigenvalue)
    
    dim = adjacencyMatrix.shape[0]
    naturalEigenvalue = np.log(estradaIndex / dim)
    return naturalEigenvalue

