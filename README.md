# Lunar Reconnaissance Orbiter (LRO) 

The Lunar Reconnaissance Orbiter ([LRO](https://www.nasa.gov/mission_pages/LRO/main/index.html)) is a robotic mission by NASA that set out to map the moon's surface. These images taken by the instruments of this missions can be found in the following sites:

 - [Planetary Data System (PDS) Image Atlas](https://pds-imaging.jpl.nasa.gov/search/)
 - [LROC PDS Archive](http://lroc.sese.asu.edu/data/)
 
In order to create different databases that will be used as a part of a Super-resolution project on them, I have created some scripts to obtain and calibrate them in a automated way.

## LRO images download (*lro_download.py*)
The LRO images are indexed in a file called [CUMINDEX.TAB](http://lroc.sese.asu.edu/data/LRO-L-LROC-2-EDR-V1.0/LROLRC_0043A/INDEX/CUMINDEX.TAB). This file can be used as a CSV that contain the information related to every image taken by the instruments of the mission, from camera type and environmental conditions to the altitude of the satellite when the image were taken and the part of the moon covered (described by latitude and longitude).

This script process the CUMINDEX.TAB file to find the images that cover the selected part of the lunar surface. The inputs are the coordinates of the area to be extracted [Start latitude, End latitude][Start longitude, End longitude]    
