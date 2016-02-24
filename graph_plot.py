import csv
import matplotlib.pyplot as plt
import numpy as np
import math
from sklearn.neighbors import KernelDensity
import sys

def isInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def data_import_dict(filename):
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

def data_import(filename):
    with open(filename,"r") as f:
        reader = csv.reader(f)
        header = next(reader)

        result = []  # a list that stores triplets (type, # of nodes, # of edges)

        for row in reader:
            if row[0]:
                for i,e in enumerate(row):
                    if i == 0:
                        continue
                    if isInt(e):
                        result.append((row[0],int(row[i]),int(row[i+1])))
                        break

    return  result



def node_plotter(data,ylabel="Clustering Coefficient"):

    types = [type for n_of_nodes,Q,type in data]

    colors = ["y","r","c","b","g","k","m"]
    #plt.axes(axisbg="#777777")

    plt.xscale("log")
    plt.yscale("log")
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
    with open(params[1]) as f:
        reader = csv.reader(f)
        for row in reader:
            """
            if row[1].startswith("("): # if it's a complex number
                Q_dict[row[0]] = float(row[1].split("+0j")[0].split("(")[1])
            else:
                Q_dict[row[0]] = float(row[1])
            """
            Q_dict[row[0]] = float(row[1])
    mutual_keys = set(Q_dict.keys()).intersection(set(data.keys()))
    combined = [(data[k][1],Q_dict[k],data[k][0])for k in mutual_keys] # element -> (# of nodes, Q, type)

    node_plotter(combined,ylabel="Spectral Gap")


if __name__ == '__main__':
    main()
