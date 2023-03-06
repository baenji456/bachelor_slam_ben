# SC-LIO-SAM
Für weitere Dokumentation siehe die Bachelorarbeit von Pfannes, Lennard sowie https://github.com/gisbi-kim/SC-LIO-SAM

# Submodules
* Basierend auf **SC-LIO-SAM** https://github.com/gisbi-kim/SC-LIO-SAM
* **Ouster LiDAR Treiber** https://github.com/ouster-lidar/ouster-ros
* **SBG IMU Treiber** https://github.com/SBG-Systems/sbg_ros_driver

# How to use
Die Schritte werden jeweils in unterschiedlichen Terminals ausgeführt
1. Ouster Treiber starten
```console
source devel/setup.bash
roslaunch ouster_ros sensor.launch
```
2. SBG IMU Treiber starten
```console
source devel/setup.bash
roslaunch sbg_driver sbg_device.launch
```
3. SC-LIO-SAM starten
```console
source devel/setup.bash
roslaunch lio_sam run.launch
```
