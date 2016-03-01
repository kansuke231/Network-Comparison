#!/bin/bash
# This script is for running main.py on your local machine (a.k.a not a super computer).

# Get the path of a current working directory.
CWDPATH=$(cd $(dirname $0) && pwd)

ls ${CWDPATH}/gmlFiles_batch1/*.gml | parallel python main.py {} modularity
