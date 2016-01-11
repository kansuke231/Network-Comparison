"""
    
For graph object G
spectral_gap(G) returns smallest nonzero Laplacian eigenvalue

"""

import numpy.linalg
from igraph import *
import numpy as np


def spectral_gap(G):
    
    laplacian = numpy.array(list(G.laplacian()))
    spectrum = numpy.linalg.eigvals(laplacian)
    spectrum.sort()
    spectralGap = 0
    
    for eigenvalue in spectrum:
        if eigenvalue > 10e-9:
            spectralGap = eigenvalue
            break
    return spectralGap
