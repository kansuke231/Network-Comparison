import igraph


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
    wrappedG = GraphWrapper("gmlFiles/PoliticalBlogs.gml")
    print(wrappedG.G)
    print(wrappedG.attributes)

    wrappedG.G.simplify() # simplify the graph so that it does not contain self-loops and multi-edges
    wrappedG.G.to_undirected() # make G undirected graph.

    """
    for e in wrappedG.G.es:
        print(e["weight"])


    for v in wrappedG.G.vs:
        print(v)
    """
    from feature_extractors.mean_degree import mean_degree
    from feature_extractors.mean_geodesic import mean_geodesic_distance
    from feature_extractors.clustering_coefficient import clustering_coeeficient
    from feature_extractors.motif_counting import motif_census, motif_significance, random_motif_census
    from feature_extractors.degree_assortativity import degree_assortativity

    """
    print("mean degree",mean_degree(wrappedG.G))
    print("------------------------------------")
    #print(mean_geodesic_distance(wrappedG.G,weighted=True))
    #print("------------------------------------")
    print("mean geodesic distance",mean_geodesic_distance(wrappedG.G,weighted=False))
    print("------------------------------------")
    print("clustering coefficient",clustering_coeeficient(wrappedG.G))
    print("------------------------------------")
    print("motif counting",motif_census(wrappedG.G))
    #print("------------------------------------")
    #print("motif significance",random_motif_census(wrappedG.G))
    print("------------------------------------")
    print("degree assortativity",degree_assortativity(wrappedG.G))
    print("------------------------------------")
    #print(wrappedG.G.clusters(mode="STRONG"))
    """

if __name__ == '__main__':
    main()