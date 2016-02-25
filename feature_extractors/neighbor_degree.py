

def mean_neighbor_degree(G):
	"""
	Calculates the mean neighbor degree for a graph G.
	"""
	result = 0.0
	n = len(G.vs)

	for vi in G.vs:
		ki = G.degree(vi)
		for vj in G.neighbors(vi):
			kj = G.degree(vj)
			result += (float(kj)/float(ki))
	
	return result/n
