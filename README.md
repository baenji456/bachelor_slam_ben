# SC-LIO-SAM
Für weitere Dokumentation siehe die Bachelorarbeit von Pfannes, Lennard sowie https://github.com/gisbi-kim/SC-LIO-SAM

# Ideen
* Entfernung dynamischer Objekte mit [removert](https://www.youtube.com/watch?v=UiYYrPMcIRU)

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

# Parameter
Die Paramter des SC-LIO-SAM Packages sind in der Datei params_liosam.yaml zu finden. (LINK EINFÜGEN)
Es gibt zwei Arten von Parametern, diese werden im Folgenden Einrichtungsparameter und Anpassungsparameter genannt. Einrichtungparameter sind Parameter, die für einen bestimmten Aufbau oder ein bestimmtes Projekt nur einmal angepasst werden müssen. Um einen Aufbau für verschiedene Anwendungen zu optimieren können Anpassungsparameter verändert werden.
## Einrichtungsparameter
1. **Topics**: Namen bestimmter Topics, die von LiDAR und IMU gesendet und von SC_LIO_SAM verwendet werden
2. **Frames**: Benennung der verschiedenen Frames 
3. **GPS Settings**: Aktivierung von useImuHeadingInitialization, wenn GPS genutzt werden soll
4. **Export Settings**: Speicherort für PCD Dateien
5. **Sensor Settings**: Angaben zu genutzten LiDAR Sensor Typ
6. **IMU Settings**: Angaben zu Noise und Bias der IMU, müssen vorherbestimmt werden
7. **Extrinsics**: Abstände zwischen LiDAR und IMU
8. **CPU Params**: Anzahl der Cores
## Anpassungsparameter
