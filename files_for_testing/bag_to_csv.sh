#!/bin/bash

# Read the input parameters
filename=$1

source /opt/ros/noetic/setup.bash
source devel/setup.bash

rostopic echo -b $filename.bag -p /pose/odom2axis > 0_TRAJS/axis_$filename.csv

rostopic echo -b $filename.bag -p /lio_sam/mapping/path> 0_PATHS/path_$filename.csv