#!/Users/kaik7708/env/bin/python
import igraph
import os
import operator
import csv
import numpy as np



def main():

    from feature_extractors.mean_geodesic import mean_geodesic_distance

    pwd = os.getcwd()

    getall = [ (file, os.path.getsize(pwd+"/gmlFiles/"+file)) for file in os.listdir(pwd+"/gmlFiles")]
    getall_sorted = sorted(getall, key=operator.itemgetter(1))
    f = open(pwd+"mean_geodesic.csv","w")
    writer = csv.writer(f)
    for file,size in getall_sorted:
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
		G = igraph.read(pwd+"/gmlFiles/"+name)
		G.simplify()
		G.to_undirected()
		largest_c_vertices = G.clusters(mode="STRONG")[0]
		largest_c = G.subgraph(largest_c_vertices)
		mean_geo = mean_geodesic_distance(largest_c,weighted=False)
		writer.writerow((name,mean_geo))
    f.close()

if __name__ == '__main__':
    main()
