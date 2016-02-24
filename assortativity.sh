#!/bin/bash
#PBS -N assortativity
#PBS -q shortmem
#PBS -l nodes=1:ppn=48
#PBS -l walltime=23:59:00

source /Users/kaik7708/env/bin/activate

ls /Users/kaik7708/gmlFiles_batch1/*.gml | parallel python /Users/kaik7708/Network-Comparison/main_assortativity.py
