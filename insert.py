"""
	insert.py updates a file containing feature vectors with new feature values you want to add
	
	insert.py takes three argument when it's executed:
		1. the name of a file which contains feature vectors for each network data
		2. the name of a feature you are trying to populate with values in a table
		3. the name of a file containing feature values for networks

	For example: python insert.py features.csv MeanGeodesicPaths mean_geodesic.csv 

	features.csv should look like:
		.gmlFile,NetworkType,SubType,NumberNodes,.....
		Malaria_HVR_1.gml,Biological,Genetic,308,.....

	mean_geodesic.csv should look like:
		AutonomousInternetSystems733.gml,3.641745571764424
		BinaryInteractomeArabidopsisThaliana_binary_hq.gml,6.6352033852033854
		......

"""
import csv
import sys
import copy
from operator import itemgetter
import os

# csv heading
dict_order = [".gmlFile","NetworkType","SubType","NumberNodes","NumberEdges","MeanDegree",\
			  "MeanGeodesicPath","ClusteringCoefficient","Modularity","NaturalEigenvalue",\
			  "m3_1","m3_2","m3_3","m3_4","m4_1","m4_2","m4_3","m4_4","m4_5","m4_6","m4_7","m4_8","m4_9","m4_10","m4_11"]





feature_csv = "old_features.csv"
feature_kind = "NaturalEigenvalue"
valueFiles = os.listdir(/Users/eltu0973/natural_eigenvalue)



def main():
	"""
	-- inputs --
	input_file: a csv file containing values of a specific feature of networks.
	"""

	feature_dict = {}
    gml_name = ""

	# reading feature vectors, and store them in a dictionary
	with open(feature_csv, 'rb') as file1:
		reader = csv.DictReader(file1)
		for row in reader:
			gml_name = row[".gmlFile"]
			feature_dict[gml_name] = copy.copy(row)

	# reading an input file containing values of a specific feature for networks

    for input_file in valueFiles:
        with open(input_file, 'rb') as file2:
            reader = csv.reader(file2)
            for row in reader:
                gml_name = row[0]
                value = row[1]
                feature_dict[gml_name]["NaturalEigenvalue"] = value

	
	# writing the updated feature vectors
    with open("features.csv", 'wb') as file3:
        writer = csv.DictWriter(file3,fieldnames=dict_order)
        writer.writeheader()
        for rowdict in sorted(feature_dict.values(), key=itemgetter('.gmlFile')):
            writer.writerow(rowdict)



	

if __name__ == "__main__":
	main()


