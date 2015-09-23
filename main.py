import igraph

G = igraph.read("gmlFiles/UsAirportstop500.gml")
#G = igraph.read("dummy.gml")

G.simplify() # simplify the graph so that it does not contain self-loops and multi-edges
G.to_undirected() # make G undirected graph.

"""
for e in G.es:
    print(e["weight"])
for v in G.vs:
    print(v["type"])
"""

from feature_extractors.mean_degree import mean_degree
from feature_extractors.mean_geodesic import mean_geodesic_distance
from feature_extractors.clustering_coefficient import clustering_coeeficient
from feature_extractors.motif_counting import motif_census
from feature_extractors.degree_assortativity import degree_assortativity

print("mean degree",mean_degree(G))
print("------------------------------------")
#print(mean_geodesic_distance(G,weighted=True))
#print("------------------------------------")
print("mean geodesic distance",mean_geodesic_distance(G,weighted=False))
print("------------------------------------")
print("clustering coefficient",clustering_coeeficient(G))
print("------------------------------------")
print("motif counting",motif_census(G))
print("------------------------------------")
print("degree assortativity",degree_assortativity(G))
print("------------------------------------")
#print(G.clusters(mode="STRONG"))
