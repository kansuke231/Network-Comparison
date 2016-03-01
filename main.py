#!/Users/kaik7708/env/bin/python

"""
This main.py serves as a basis for computing a network's feature.

The 1st command line argument is a filepath for .gml file.
The 2nd one is the name of a feature extracting function.
Note that the name of a script it (I mean the function) lives in has to be the same
as the function's name.
"""

import igraph
import os
import csv
import sys

def main(filepath,feature):
    pwd = os.getcwd()
    filename = os.path.split(filepath)[1]
    f = open(pwd + "/%s/"%feature + filename + ".%s.txt"%feature,"w")
    writer = csv.writer(f)
    G = igraph.read(filepath)
    G.simplify()
    G.to_undirected()
    largest_c = G.clusters(mode="STRONG").giant()
    exec("f_value = %s(largest_c)"%feature)
    writer.writerow((filepath,f_value))
    f.close()

if __name__ == '__main__':
    param = sys.argv
    filepath = param[1]
    feature = param[2]
    exec("from feature_extractors.%s import %s"%(feature,feature))
    main(filepath,feature)
