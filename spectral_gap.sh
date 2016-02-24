#!/bin/sh
#PBS -N spectral_gap
#PBS -q longmem
#PBS -l nodes=3:ppn=36
#PBS -l walltime=230:00:00

source /Users/kaik7708/env/bin/activate

ls /Users/kaik7708/gmlFiles/*.gml | parallel python /Users/kaik7708/Network-Comparison/main_spectral_gap.py
