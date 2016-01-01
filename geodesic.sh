#!/bin/sh

CWDPATH=$(cd $(dirname $0) && pwd)

ls ${CWDPATH}/test_gml/*.gml | parallel python main_geodesic.py
