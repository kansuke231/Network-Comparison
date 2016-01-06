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

# csv heading
dict_order = [".gmlFile","NetworkType","SubType","NumberNodes","NumberEdges","MeanDegree",\
			  "MeanGeodesicPath","ClusteringCoefficient","Modularity"]

def main(feature_csv,feature_kind,input_file):
	"""
	-- inputs --
	feature_csv: a file path to a csv file containing all the information of feature vectors.
	feature_kind: the name of a feature you are trying to populate with values.
	input_file: a csv file containing values of a specific feature of networks. 
	"""

	feature_dict = {}

	# reading feature vectors, and store them in a dictionary
	with open(feature_csv, 'rb') as file1:
		reader = csv.DictReader(file1)
		for row in reader:
			gml_name = row[".gmlFile"]
			feature_dict[gml_name] = copy.copy(row)

	# reading an input file containing values of a specific feature for networks
	with open(input_file, 'rb') as file2:
		reader = csv.reader(file2)
		for row in reader:
			gml_name = row[0]
			value = row[1]
			try:
				feature_dict[gml_name][feature_kind] = value
			except:
				print "Unregisted gml file:",gml_name

	# writing the updated feature vectors
	with open(feature_csv, 'wb') as file3:
		writer = csv.DictWriter(file3,fieldnames=dict_order)
		writer.writeheader()
		for rowdict in sorted(feature_dict.values(), key=itemgetter('.gmlFile')):
			writer.writerow(rowdict)


	

if __name__ == "__main__":
	params = sys.argv
	feature_csv = params[1]
	feature_kind = params[2]
	input_file = params[3]

	if not feature_kind in dict_order[1:]:
		print "Invalid feature name:", feature_kind
		exit(1)

	main(feature_csv,feature_kind,input_file)


