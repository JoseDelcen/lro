# Lunar Reconnaissance Orbiter (LRO) 

The Lunar Reconnaissance Orbiter ([LRO](https://www.nasa.gov/mission_pages/LRO/main/index.html)) is a robotic mission by NASA that set out to map the moon's surface. These images taken by the instruments of this missions can be found in the following sites:

 - [Planetary Data System (PDS) Image Atlas](https://pds-imaging.jpl.nasa.gov/search/)
 - [LROC PDS Archive](http://lroc.sese.asu.edu/data/)
 
In order to create different databases that will be used as a part of a Super-resolution project on them, I have created some scripts to obtain and calibrate them in a automated way.

## LRO images download (*lro_download.py*)
The LRO images are indexed in a file called [CUMINDEX.TAB](http://lroc.sese.asu.edu/data/LRO-L-LROC-2-EDR-V1.0/LROLRC_0043A/INDEX/CUMINDEX.TAB). This file can be used as a CSV that contain the information related to every image taken by the instruments of the mission, from camera type and environmental conditions to the altitude of the satellite when the image were taken and the part of the moon covered (described by latitude and longitude).

This script process the CUMINDEX.TAB file to find the images that cover the selected part of the lunar surface. The inputs are the coordinates of the area to be extracted [Start latitude, End latitude][Start longitude, End longitude]. 

Once the list of objects to be downloaded is generated, the files are copied to the target folder. 

## ISIS3 Calibration process (*isis.py & isis.sh*)
Integrated Software for Imagers and Spectrometers v3 ([ISIS3](https://github.com/USGS-Astrogeology/ISIS3)) is a digital image processing software package to manipulate imagery collected by current and past NASA and International planetary missions. 

In order to calibrate de images obtained with the previous script, this software is used. The pipeline to calibrate the images would be:
 1. *lronac2isis*: Converts the .IMG files into the CUBE format (.CUB) that ISIS3 uses to process the images.
 2. *spiceinit*: Adds to the .CUB file all the information needed for the calibration step. It is important to use the web service in order to avoid the download of 500GB+ of calibration kernels related to the LRO database.
 3. *lronaccal*: Calibrates the images.
 4. *lronacecho*: Removes the echo from the images.
 5. *stretch*: Converts the image into a 8-bit image
 
There are several ways to generate standard image files (.png, .jpg):
 1. Use *isis2std*
 2. Use the [GDAL's tool](http://planetarygis.blogspot.com/2014/06/using-isis-23-image-cubes-in-gis.html)
 
As they were not working properly (ending up generating a blank .png image), an alternative process is used for the conversion:
 1. Use *lronac2pds* to convert back the .CUB file into a .IMG
 2. Use the tool [IMG2PNG](http://bjj.mmedia.is/utils/img2png/#howto) to convert the .IMG file into a .PNG
 
