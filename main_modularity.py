#!/Users/kaik7708/env/bin/python
import igraph
import os
import operator
import csv
import numpy as np
import sys
from feature_extractors.modularity import modularity

def main(filepath):
    pwd = os.getcwd()
    filename = os.path.split(filepath)[1]
    f = open(pwd+"/modularity/"+filename+".modularity.txt","w")
    writer = csv.writer(f)
    G = igraph.read(filepath)
    G.simplify()
    G.to_undirected()
    largest_c = G.clusters(mode="STRONG").giant()
    Q = modularity(largest_c)
    writer.writerow((filename,Q))
    f.close()

if __name__ == '__main__':
    param = sys.argv
    main(param[1])
