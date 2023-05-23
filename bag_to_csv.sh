#!/bin/bash

# Read the input parameters
filename=$1

source /opt/ros/noetic/setup.bash
source devel/setup.bash

rostopic echo -b $filename.bag -p /pose/odom2base > $filename.csv