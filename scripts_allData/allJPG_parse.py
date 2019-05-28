import os;

import cv2
import numpy as np

from shutil import copyfile



trainDir = "/home/mmendiet/Courses/Spring_2019/Applied_AI/project_data/allData/jpegTraining/"
testDir = "/home/mmendiet/Courses/Spring_2019/Applied_AI/project_data/allData/jpegTest/"
writeDir = "/home/mmendiet/Courses/Spring_2019/Applied_AI/darknet_server/data/allData_info/allData"
#writeDir = "/media/work1/Seagate Expansion Drive/darknet_folders/allData_info/allData"


trainFolders = ['2S3jpeg','BMP2jpeg','BRDM2jpeg','BTR70jpeg','Pickupjpeg','T72jpeg']
testFolders = ['SUVjpeg','ZSU23-4jpeg']

for folder in trainFolders:
    currDir = trainDir+folder
    print(currDir)
    for file in sorted(os.listdir(currDir)):
        #print(file)
        copyfile(currDir+'/'+file, writeDir+'/'+file)
    
for folder in testFolders:
    currDir = testDir+folder
    print(currDir)
    for file in sorted(os.listdir(currDir)):
        #print(file)
        copyfile(currDir+'/'+file, writeDir+'/'+file)
