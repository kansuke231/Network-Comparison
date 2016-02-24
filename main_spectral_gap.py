#!/Users/kaik7708/env/bin/python
import igraph
import os
import operator
import csv
import numpy as np
import sys
from feature_extractors.spectral_gap import spectral_gap

def main(filepath):
    pwd = os.getcwd()
    filename = os.path.split(filepath)[1]
    f = open(pwd+"/spectral_gap/"+filename+".spectral_gap.txt","w")
    writer = csv.writer(f)
    G = igraph.read(filepath)
    G.simplify()
    G.to_undirected()
    largest_c = G.clusters(mode="STRONG").giant()
    result = spectral_gap(largest_c)
    writer.writerow((filename,result))
    f.close()

if __name__ == '__main__':
    param = sys.argv
    main(param[1])
