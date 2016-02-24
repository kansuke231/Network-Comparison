#!/bin/sh
#PBS -N human_brain_motif
#PBS -q shortmem
#PBS -l nodes=1:ppn=1
#PBS -l walltime=23:59:00

HOME_PATH="/Users/kaik7708"
BRAIN_PATH="/Users/eltu0973/Human_brain_gml/Human_brain_BNU_1_0025864_session_1-bg.gml"
EDGE_LIST="/scratch/Users/kaik7708/edge_list.txt"
OUTPUT="/Users/kaik7708/human_brain_test.txt"

source /Users/kaik7708/env/bin/activate

SECONDS=0
# convert a gml file into an edgelist txt file
python ${HOME_PATH}/motif_computing_system/gml_to_edgelist.py ${BRAIN_PATH} rewire ${EDGE_LIST} 

time=$SECONDS
echo $time

SECONDS=0
${HOME_PATH}/pgd-v1/pgd -f ${EDGE_LIST} --macro ${OUTPUT};

time=$SECONDS
echo $time
