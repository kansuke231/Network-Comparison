#!/bin/bash
#PBS -N geodesic_distance2
#PBS -q longmem
#PBS -l nodes=1:ppn=48
#PBS -l walltime=230:00:00

source /Users/kaik7708/env/bin/activate

HOME="/Users/kaik7708"

diff -rq ${HOME}/gmlFiles ${HOME}/gmlFiles_batch1 | grep "Only in /Users/kaik7708/gmlFiles_batch1:" | sed "s/Only in .Users.kaik7708.gmlFiles_batch1: \(.*\.gml\)/\1/g" | parallel python ${HOME}/Network-Comparison/main_geodesic.py

