
def modularity(G):
	VertexClustering = G.community_multilevel()
	return VertexClustering.modularity
