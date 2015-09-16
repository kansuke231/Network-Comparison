import igraph

G = igraph.read("dummy.gml")
for e in G.es:
    print(e["weight"])
for v in G.vs:
    print(v["type"])

from feature_extractors.mean_degree import mean_degree
from feature_extractors.mean_geodesic import mean_geodesic_distance
from feature_extractors.clustering_coefficient import clustering_coeeficient
from feature_extractors.motif_counting import motif_census

print(mean_degree(G))
print("------------------------------------")
print(mean_geodesic_distance(G,weighted=True))
print("------------------------------------")
print(mean_geodesic_distance(G,weighted=False))
print("------------------------------------")
print(clustering_coeeficient(G))
print("------------------------------------")
print(motif_census(G))