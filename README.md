# SC-LIO-SAM
Für weitere Dokumentation siehe die Bachelorarbeit von Pfannes, Lennard sowie https://github.com/gisbi-kim/SC-LIO-SAM

# Ideen
* Entfernung dynamischer Objekte mit [removert](https://www.youtube.com/watch?v=UiYYrPMcIRU)

# Submodules
* Basierend auf **SC-LIO-SAM** https://github.com/gisbi-kim/SC-LIO-SAM
* **Ouster LiDAR Treiber** https://github.com/ouster-lidar/ouster-ros
* **SBG IMU Treiber** https://github.com/SBG-Systems/sbg_ros_driver

# How to use
```console
git clone https://github.com/baenji456/bachelor_slam_ben.git
cd bachelor_slam_ben
catkin_make
```
Alle folgenden Schritte werden in unterschiedlichen Terminals ausgeführt
## Variante A: Live
1. Ouster Treiber starten
```console
source devel/setup.bash
roslaunch ouster_ros sensor.launch
```
2. SBG IMU Treiber starten
```console
source devel/setup.bash
roslaunch sbg_driver sbg_ellipseD.launch
```
3. SC-LIO-SAM starten
```console
source devel/setup.bash
roslaunch lio_sam run.launch
```
## Variante B: Mit Bagfiles
1. SC-LIO-SAM starten
```console
source devel/setup.bash
roslaunch lio_sam run.launch
```
2. Bagfile abspielen
```console
source devel/setup.bash
rosbag play <path/to/your/bagfile>
```
