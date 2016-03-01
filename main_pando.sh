#!/bin/bash
#PBS -N feature_name
#PBS -q longmem
#PBS -l nodes=3:ppn=36
#PBS -l walltime=230:00:00

# Modify HOME_PATH below for your setting.
HOME_PATH="/Users/kaik7708"
source ${HOME_PATH}/env/bin/activate

# Modify the last segment of the line below in order to change the network feature you want to calculate.
ls ${HOME_PATH}/gmlFiles/*.gml | parallel python ${HOME_PATH}/Network-Comparison/main.py {} modularity
