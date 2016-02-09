#/Users/kaik7708/env/bin/python
import igraph
import os
import operator
import csv
import numpy as np
import sys
from feature_extractors.mean_geodesic import mean_geodesic_distance

def main(filepath):
    pwd = os.getcwd()
    filename = os.path.split(filepath)[1]
    f = open(pwd+"/geodesic/"+filename+"geo.txt","w")
    writer = csv.writer(f)
    G = igraph.read(filepath)
    G.simplify()
    G.to_undirected()
    largest_c = G.clusters(mode="STRONG").giant()
    #largest_c = G.subgraph(largest_c_vertices)
    mean_geo = mean_geodesic_distance(largest_c)
    writer.writerow((filename,mean_geo))
    f.close()

if __name__ == '__main__':
    param = sys.argv
    main(param[1])
