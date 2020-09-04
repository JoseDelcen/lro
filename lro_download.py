#!/usr/bin/env python3
import pandas as pd
import requests
import shutil
import os.path

# Coordinates to extract

print("Introduce the coordinates of the area to be processed")

START_LAT = input("Starting Latitude: ")
END_LAT = input("Ending Latitude: ")
START_LON = input("Starting Longitude: ")
END_LON = input("Ending Longitude: ")

# URL
urlString = 'http://lroc.sese.asu.edu/data/'


# Columns from the database CUMINDEX
#columns = {1  :  "VOLUME_ID",
#           2  :  "FILE_SPECIFICATION_ID",
#           3  :  "INSTRUMENT_HOST_ID",
#           4  :  "INSTRUMENT_ID",
#           5  :  "ORIGINAL_PRODUCT_ID",
#           6  :  "PRODUCT_ID",
#           7  :  "PRODUCT_VERSION_ID",
#           8  :  "TARGET_NAME",
#           9  :  "ORBIT_NUMBER",
#           10 : "SLEW_ANGLE",
#           11 : "MISSION_PHASE_NAME",
#           12 : "RATIONALE_DESC",
#           13 : "DATA_QUALITY_ID",
#           14 : "NAC_PREROLL_START_TIME",
#           15 : "START_TIME",
#           16 : "STOP_TIME",
#           17 : "SPACECRAFT_CLOCK_PARTITION",
#           18 : "NAC_SPACECRAFT_CLOCK_PREROLL_COUNT",
#           19 : "SPACECRAFT_CLOCK_START_COUNT",
#           20 : "SPACECRAFT_CLOCK_STOP_COUNT",
#           21 : "START_SCLK_SECONDS",
#           22 : "START_SCLK_TICKS",
#           23 : "STOP_SLCK_SECONDS",
#           24 : "STOP_SLCK_TICKS",
#           25 : "NAC_LINE_EXPOSURE_DURATION",
#           26 : "WAC_EXPOSURE_DURATION",
#           27 : "NAC_FRAME_ID",
#           28 : "NAC_DAC_RESET",
#           29 : "NAC_CHANNEL_A_OFFSET",
#           30 : "NAC_CHANNEL_B_OFFSET",
#           31 : "INSTRUMENT_MODE_CODE",
#           32 : "WAC_INSTRUMENT_MODE_ID",
#           33 : "WAC_BAND_CODE",
#           34 : "WAC_BACKGROUND_OFFSET",
#           35 : "WAC_FILTER_NAME",
#           36 : "WAC_NUMBER_OF_FRAMES",
#           37 : "WAC_INTERFRAME_TIME",
#           38 : "WAC_INTERFRAME_CODE",
#           39 : "WAC_MODE_POLAR",
#           40 : "COMPAND_SELECT_CODE",
#           41 : "MODE_COMPRESSION",
#           42 : "MODE_TEST",
#           43 : "NAC_TEMPERATURE_SCS",
#           44 : "NAC_TEMPERATURE_FPA",
#           45 : "NAC_TEMPERATURE_FPGA",
#           46 : "NAC_TEMPERATURE_TELESCOPE",
#           47 : "WAC_BEGIN_TEMPERATURE_SCS",
#           48 : "WAC_MIDDLE_TEMPERATURE_SCS",
#           49 : "WAC_END_TEMPERATURE_SCS",
#           50 : "WAC_BEGIN_TEMPERATURE_FPA",
#           51 : "WAC_MIDDLE_TEMPERATURE_FPA",
#           52 : "WAC_END_TEMPERATURE_FPA",
#           53 : "IMAGE_LINES",
#           54 : "LINE_SAMPLES",
#           55 : "SAMPLE_BITS",
#           56 : "SCALED_PIXEL_WIDTH",
#           57 : "SCALED_PIXEL_HEIGHT",
#           58 : "RESOLUTION",
#           59 : "EMISSION_ANGLE",
#           60 : "INCIDENCE_ANGLE",
#           61 : "PHASE_ANGLE",
#           62 : "NORTH_AZIMUTH",
#           63 : "SUB_SOLAR_AZIMUTH",
#           64 : "SUB_SOLAR_LATITUDE",
#           65 : "SUB_SOLAR_LONGITUDE",
#           66 : "SUB_SPACECRAFT_LATITUDE",
#           67 : "SUB_SPACECRAFT_LONGITUDE",
#           68 : "SOLAR_DISTANCE",
#           69 : "SOLAR_LONGITUDE",
#           70 : "CENTER_LATITUDE",
#           71 : "CENTER_LONGITUDE",
#           72 : "UPPER_RIGHT_LATITUDE",
#           73 : "UPPER_RIGHT_LONGITUDE",
#           74 : "LOWER_RIGHT_LATITUDE",
#           75 : "LOWER_RIGHT_LONGITUDE",
#           76 : "LOWER_LEFT_LATITUDE",
#           77 : "LOWER_LEFT_LONGITUDE",
#           78 : "UPPER_LEFT_LATITUDE",
#           79 : "UPPER_LEFT_LONGITUDE",
#           80 : "SPACECRAFT_ALTITUDE",
#           81 : "TARGET_CENTER_DISTANCE",
#           82 : "ORBIT_NODE",
#           83 : "LRO_FLIGHT_DIRECTION"}

# Convert Original CSV into a reduced version

#data = pd.read_csv("CUMINDEX.csv")
#print("Head of CSV: ")
#print("Shape of CSV:")
#print(data.shape)
#print("Dropping useless columns...")
#data.drop(['DATA_QUALITY_ID','NAC_PREROLL_START_TIME','START_TIME','STOP_TIME','SPACECRAFT_CLOCK_PARTITION','NAC_SPACECRAFT_CLOCK_PREROLL_COUNT','SPACECRAFT_CLOCK_START_COUNT','SPACECRAFT_CLOCK_STOP_COUNT','START_SCLK_SECONDS','STOP_SLCK_SECONDS','START_SCLK_TICKS','NAC_LINE_EXPOSURE_DURATION','WAC_EXPOSURE_DURATION','NAC_FRAME_ID','NAC_DAC_RESET','NAC_CHANNEL_A_OFFSET','NAC_CHANNEL_B_OFFSET','INSTRUMENT_MODE_CODE','WAC_INSTRUMENT_MODE_ID','WAC_BAND_CODE','WAC_BACKGROUND_OFFSET','WAC_NUMBER_OF_FRAMES','WAC_FILTER_NAME','WAC_INTERFRAME_TIME','WAC_INTERFRAME_CODE','WAC_MODE_POLAR','COMPAND_SELECT_CODE','MODE_COMPRESSION','MODE_TEST','NAC_TEMPERATURE_SCS', 'NAC_TEMPERATURE_FPA', 'NAC_TEMPERATURE_FPGA', 'NAC_TEMPERATURE_TELESCOPE', 'WAC_BEGIN_TEMPERATURE_SCS', 'WAC_MIDDLE_TEMPERATURE_SCS', 'WAC_END_TEMPERATURE_SCS', 'WAC_BEGIN_TEMPERATURE_FPA', 'WAC_MIDDLE_TEMPERATURE_FPA', 'WAC_END_TEMPERATURE_FPA'], axis = 1, inplace=True)
#print(data.columns)
#print("Shape of CSV after drop:")
#print(data.shape)
#print(data.head())
#data.to_csv('CUMINDEX_2.csv',index = False)

# Read CSV
data = pd.read_csv("CUMINDEX_2.csv")
print("Number of total images currently in the DB: ", len(data))
print("Extracted Location Coordinates")
print("Latitude: (", START_LAT, ",", END_LAT,")")
print("Longitude: (", START_LON, ",", END_LON , ")")

# Extract file names for images in range (START_LAT, END_LAT)(START_LON, END_LON)
fileNames = data.loc[(data.CENTER_LATITUDE > START_LAT) & (data.CENTER_LATITUDE < END_LAT) & (data.CENTER_LATITUDE > START_LON) & (data.CENTER_LATITUDE < END_LON), "FILE_SPECIFICATION_ID"]
cameraType = data.loc[(data.CENTER_LATITUDE > START_LAT) & (data.CENTER_LATITUDE < END_LAT) & (data.CENTER_LATITUDE > START_LON) & (data.CENTER_LATITUDE < END_LON), "ORIGINAL_PRODUCT_ID"]
#fileNames = data.loc[(data.CENTER_LATITUDE > START_LAT) & (data.CENTER_LATITUDE < END_LAT) & (data.CENTER_LATITUDE > START_LON) & (data.CENTER_LATITUDE < END_LON), "FILE_SPECIFICATION_ID"]

print("Number of selected images: ", len(fileNames))

for index, value in fileNames.items():
    urlStringToDownload = urlString + value[4:]
    print(urlStringToDownload)
    print(cameraType.get(index)[:-8])

    if (cameraType.get(index)[:-8] == 'nacl' or cameraType.get(index)[:-8] == 'nacr' ):
        fileToSave = 'Selected_images/NAC/'

    else:
        fileToSave = 'Selected_images/WAC/'
    fileToSave += value[59:]

    if (os.path.isfile(fileToSave)):
        continue

    imageToDownload = requests.get(urlStringToDownload, stream = True)

    if imageToDownload.status_code == 200:

        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        imageToDownload.raw.decode_content = True

        # Open a local file with wb ( write binary ) permission.
        with open(fileToSave,'wb') as f:
            shutil.copyfileobj(imageToDownload.raw, f)
        print('Image sucessfully Downloaded: ',fileToSave)

    else:
        print('Image Couldn\'t be retreived')
     

# Generates file with the list of the downloaded images
fileNames.to_csv('downloaded_image_list.csv', index = False)

# Downloading Image

#urlString += 'LRO-L-LROC-2-EDR-V1.0/LROLRC_0001/DATA/COM/2009181/WAC/M101016050CE.IMG'
#image = requests.get(string, stream = True )
#filename = 'M101016050CE.IMG'
# Check if the image was retrieved successfully
#if image.status_code == 200:
    # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
    #image.raw.decode_content = True
    
    # Open a local file with wb ( write binary ) permission.
    #with open(filename,'wb') as f:
    #    shutil.copyfileobj(image.raw, f)
    #print('Image sucessfully Downloaded: ',filename)
#else:
    #print('Image Couldn\'t be retreived')