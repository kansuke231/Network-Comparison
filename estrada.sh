#!/bin/sh
#PBS -N estrada
#PBS -q shortmem
#PBS -l nodes=3:ppn=24
#PBS -l walltime=23:59:00

source /Users/kaik7708/env/bin/activate

ls /Users/kaik7708/gml/*.gml | parallel python /Users/kaik7708/Network-Comparison/main_estrada.py
