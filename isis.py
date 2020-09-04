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

