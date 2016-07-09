import random

def diameter(G):

	N = len(G.vs)

	if N < 10000:
		return G.diameter(directed=False)
		
	else:
		ds = []
		for i,v in enumerate(random.sample(G.vs, int(N*0.01))):
			path_lengths = G.shortest_paths(v,weights=None)[0]
			ds+=path_lengths
		return max(ds)