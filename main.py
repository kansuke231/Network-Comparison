import igraph
import os
import operator
import csv
import numpy as np


class GraphWrapper:
    """
    This class is a wrapper class for igraph's graph object.
    self.G is an attribute for igraph's graph object
    self.attributes is a dictionary of the graph attributes
    """
    def __init__(self,filepath):
        self.G = igraph.read(filepath)
        self.attributes = self.type_extractor(filepath)

    def type_extractor(self,filepath):
        """
        This method takes a string of a file path and returns
        a dictionary of graph attributes: e.g. d["type"] -> Social, d["subtype"] -> Sports
        """
        d = {}
        with open(filepath,"r") as f:
            flag = False
            for e in f.readlines():
                words = e.split()

                if "graph" in words:
                    flag = True
                    continue

                if "node" in words:
                    break

                if flag and (len(words) == 2):  #words could be like ['['] after seeing ['graph'], thus len()
                    d[words[0]] = words[1]


        return d


def main():

    from feature_extractors.mean_geodesic import mean_geodesic_distance
    from feature_extractors.clustering_coefficient import clustering_coeeficient
    from feature_extractors.motif_counting import motif_census, motif_significance, random_motif_census
    from feature_extractors.degree_assortativity import degree_assortativity

    pwd = os.getcwd()

    getall = [ (file, os.path.getsize(pwd+"/gmlFiles/"+file)) for file in os.listdir(pwd+"/gmlFiles")]
    for file,size in sorted(getall, key=operator.itemgetter(1)):
        if file.endswith(".gml"):
            # files below have some bugs, causing this script to stop.
            if not(file == "911_Hijacker_Associations.gml")\
            and not(file == "Corporate_Ownership.gml")\
            and not(file == "Faculty_Hiring_Business.gml")\
            and not(file == "Faculty_Hiring_Computer_Science.gml")\
            and not(file == "Faculty_Hiring_History.gml")\
            and not(file == "High_School_Dynamic_Contact_2011.gml")\
            and not(file == "MidievalRussiaTrade.gml"):
                name = file
                print name
                motif_sig = motif_significance("gmlFiles/"+name)
                np.savetxt("z_score/"+file+".txt",motif_sig,fmt="%.4f")


if __name__ == '__main__':
    main()
