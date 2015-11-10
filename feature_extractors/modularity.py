
def modularity(G):
	VertexDendrogram = G.community_fastgreedy()
	VertexClustering = VertexDendrogram.as_clustering()
	return VertexClustering.modularity