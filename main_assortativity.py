#!/Users/kaik7708/env/bin/python
import igraph
import os
import operator
import csv
import numpy as np
import sys
from feature_extractors.degree_assortativity import degree_assortativity

def main(filepath):
    pwd = os.getcwd()
    filename = os.path.split(filepath)[1]
    f = open(pwd+"/assortativity/"+filename+".assortativity.txt","w")
    writer = csv.writer(f)
    G = igraph.read(filepath)
    G.simplify()
    G.to_undirected()
    largest_c = G.clusters(mode="STRONG").giant()
    A = degree_assortativity(largest_c)
    writer.writerow((filename,A))
    f.close()

if __name__ == '__main__':
    param = sys.argv
    main(param[1])
