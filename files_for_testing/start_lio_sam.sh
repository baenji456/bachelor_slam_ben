#!/bin/bash

# Read the input parameters
bagfile=$1
filename=$2

echo "RUNNING BAGFILE $bagfile WITH SETUP $filename"

source /opt/ros/noetic/setup.bash
source devel/setup.bash

roslaunch lio_sam run_tests.launch bagfile:=$bagfile filename:=$filename