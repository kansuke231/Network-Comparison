import igraph

G = igraph.read("dummy.gml")
for e in G.es:
    print(e["weight"])
for v in G.vs:
    print(v["type"])

from feature_extractors.mean_degree import mean_degree
from feature_extractors.mean_geodesic import mean_geodesic_distance

print(mean_degree(G))
print(mean_geodesic_distance(G,weighted=True))
print(mean_geodesic_distance(G,weighted=False))