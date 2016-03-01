"""
    
For graph object G
fiedler_eigenvalue(G) returns second smallest Laplacian eigenvalue

"""

import numpy.linalg

def fiedler_eigenvalue(G):
    
    laplacian = numpy.array(list(G.laplacian()))
    spectrum = numpy.linalg.eigvals(laplacian)
    spectrum.sort()
    fiedler = spectrum[1]
    return fiedler
