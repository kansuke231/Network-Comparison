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
    #filename = os.path.split(filepath)[1]
    f = open(pwd+"/geodesic/"+filepath+".geo.txt","w")
    writer = csv.writer(f)
    G = igraph.read("/Users/kaik7708/gmlFiles_batch1/"+filepath)
    G.simplify()
    G.to_undirected()
    largest_c = G.clusters(mode="STRONG").giant()
    mean_geo = mean_geodesic_distance(largest_c)
    writer.writerow((filepath,mean_geo))
    f.close()

if __name__ == '__main__':
    param = sys.argv
    main(param[1])
