#!/usr/bin/env python3

import os
from os import listdir
from os.path import isfile, join

# .IMG -> .CUB
mypath = "/home/jota/Documents/LROC_DB/LRO_0001/NAC/"
base_from = "lronac2isis from=/home/jota/Documents/LROC_DB/LRO_0001/NAC/"
base_to = " to=/home/jota/Documents/LROC_DB/LRO_0001/CUBE/"
output_file = open("commands.txt", "w")


# Listing all the files in folder
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for f in onlyfiles:
    from_string = base_from + f
    to_string = base_to + f[:-4]
    res_string = from_string + to_string + "\n"
    output_file.write(res_string)

# 
output_file.close()

# Calibration data attach
mypath = "/home/jota/Documents/LROC_DB/LRO_0001/NAC/"
spice_from = "spiceinit from=/home/jota/Documents/LROC_DB/LRO_0001/CUBE/"
spice_to = " web=yes"
output_file = open("commands.txt", "w")


# Listing all the files in folder
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for f in onlyfiles:
    from_string = spice_from + f
    to_string = spice_to
    res_string = from_string + to_string + "\n"
    output_file.write(res_string)

# 
output_file.close()


# Image Calibration
mypath = "/home/jota/Documents/LROC_DB/LRO_0001/NAC/"
base_from = "lronaccal from=/home/jota/Documents/LROC_DB/LRO_0001/CUBE/"
base_to = " to=/home/jota/Documents/LROC_DB/LRO_0001/CAL/"
output_file = open("commands.txt", "w")


# Listing all the files in folder
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for f in onlyfiles:
    from_string = base_from + f
    to_string = base_to + f[:-4]
    res_string = from_string + to_string + "\n"
    output_file.write(res_string)

# 
output_file.close()

# Image Echo Removal
mypath = "/home/jota/Documents/LROC_DB/LRO_0001/NAC/"
base_from = "lronacecho from=/home/jota/Documents/LROC_DB/LRO_0001/CAL/"
base_to = " to=/home/jota/Documents/LROC_DB/LRO_0001/ECHO/"
output_file = open("commands.txt", "w")


# Listing all the files in folder
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for f in onlyfiles:
    from_string = base_from + f
    to_string = base_to + f[:-4]
    res_string = from_string + to_string + "\n"
    output_file.write(res_string)

# 
output_file.close()

# Image Stretch to 8-bit
#mypath = "/home/jota/Documents/LROC_DB/LRO_0001/NAC/"
#base_from = "lronac2isis from=/home/jota/Documents/LROC_DB/LRO_0001/ECHO/"
#base_to = " to=/home/jota/Documents/LROC_DB/LRO_0001/STR/"
#output_file = open("commands.txt", "w")


# Listing all the files in folder
#onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

#for f in onlyfiles:
#    from_string = base_from + f
#    to_string = base_to + f[:-4]
#    res_string = from_string + to_string + "\n"
#    output_file.write(res_string)

# 
#output_file.close()

# .CUB -> .IMG
mypath = "/home/jota/Documents/LROC_DB/LRO_0001/NAC/"
base_from = "lronac2pds from=/home/jota/Documents/LROC_DB/LRO_0001/ECHO/"
base_to = " to=/home/jota/Documents/LROC_DB/LRO_0001/IMG/"
output_file = open("commands.txt", "w")


# Listing all the files in folder
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for f in onlyfiles:
    from_string = base_from + f
    to_string = base_to + f[:-4]
    res_string = from_string + to_string + "\n"
    output_file.write(res_string)

# 
output_file.close()
