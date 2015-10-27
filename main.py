import igraph
import os
import csv


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

    with open("result.csv","wt") as f:
        writer = csv.writer(f)
        writer.writerow( ('Name', 'Mean Geodesics Path', 'Clustering Coefficient', 'Motif Significance') )
        pwd = os.getcwd()
        for file in os.listdir(pwd+"/gmlFiles"):
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
                    wrappedG = GraphWrapper("gmlFiles/"+file)

                    wrappedG.G.simplify() # simplify the graph so that it does not contain self-loops and multi-edges
                    wrappedG.G.to_undirected() # make G undirected graph.

                    largest_c_vs = wrappedG.G.clusters(mode="STRONG")[0]
                    subgraph = wrappedG.G.subgraph(largest_c_vs)

                    mean_geo = mean_geodesic_distance(subgraph,weighted=False)
                    clustering_coef = clustering_coeeficient(wrappedG.G)
                    motif_sig = motif_significance(wrappedG.G)

                    writer.writerow( (mean_geo, clustering_coef, motif_sig) )


if __name__ == '__main__':
    main()
