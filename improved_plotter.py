import csv
import matplotlib.pyplot as plt
import sys

def isInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def data_import_dict(filename):
    """
    This function is used for importing necessary data from GML_Conversion_Data.csv,
    namely the name of .gml file and the number of nodes.
    """
    with open(filename,"rU") as f:
        reader = csv.reader(f)
        header = next(reader)

        result = {}
        flag = False
        for row in reader:

            if row[0]:
                for i,e in enumerate(row):
                    if e.endswith(".gml"):
                        key = e.strip()
                        flag = True
                    if isInt(e) and flag:
                        print("------------>",key,row[0],int(e))
                        result[key] = (row[0],int(e))
                        flag = False
                        break
            flag = False # just in case

    return  result



def node_plotter(data,ylabel="Clustering Coefficient"):

    types = [type for n_of_nodes,Q,type in data]

    colors = ["y","r","c","b","g","k","m"]
    #plt.axes(axisbg="#777777")

    # uncomment out these lines below if you want a log scale
    plt.xscale("log")
    #plt.yscale("log")

    # specify the range of a plot
    plt.ylim(0,1)

    plt.xlabel("Number of Nodes")
    plt.ylabel(ylabel)
    handles = []
    for t,c in zip(set(types),colors):
        x = [n_of_nodes for n_of_nodes,Q,type in data if type == t]
        y = [Q for n_of_nodes,Q,type in data if type == t]
        handles.append(plt.scatter(x,y,color=c))

    legend = plt.legend(handles,set(types),loc=1)
    frame = legend.get_frame()
    #frame.set_facecolor("#777777")
    plt.show()




def main():
    params = sys.argv
    data = data_import_dict("GML_Conversion_Data.csv")
    
    Q_dict = {}

    # Getting data from whatever_feature.csv. 
    # The first column should be the name of .gml file and the second is a feature value
    with open(params[1]) as f:
        reader = csv.reader(f)
        for row in reader:
            Q_dict[row[0]] = float(row[1])

    mutual_keys = set(Q_dict.keys()).intersection(set(data.keys()))
    combined = [(data[k][1],Q_dict[k],data[k][0])for k in mutual_keys] # element -> (# of nodes, Q, type)

    node_plotter(combined,ylabel="Centrality")


if __name__ == '__main__':
    main()
