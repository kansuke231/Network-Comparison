#!/bin/sh
#PBS -N time_rewire
#PBS -q shortmem
#PBS -l nodes=1:ppn=1
#PBS -l walltime=23:59:00

HOME_PATH="/Users/kaik7708"
GML_PATH="/Users/kaik7708/gmlFiles/software_linux.gml"
EDGE_LIST="/scratch/Users/kaik7708/edge_list_linux.txt"
OUTPUT="/Users/kaik7708/time_rewire.txt"

source /Users/kaik7708/env/bin/activate

SECONDS=0
# convert a gml file into an edgelist txt file
python ${HOME_PATH}/motif_computing_system/gml_to_edgelist.py ${GML_PATH} rewire ${EDGE_LIST} 

time=$SECONDS
echo $time

SECONDS=0
${HOME_PATH}/pgd-v1/pgd -f ${EDGE_LIST} --macro ${OUTPUT};

time=$SECONDS
echo $time
