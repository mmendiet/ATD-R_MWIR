import os;

import cv2
import numpy as np

from shutil import copyfile



trainDir = "/home/mmendiet/Courses/Spring_2019/Applied_AI/project_data/allData/trainingGT_all/"
testDir = "/home/mmendiet/Courses/Spring_2019/Applied_AI/project_data/allData/testGT_all/"
writeDir = "/home/mmendiet/Courses/Spring_2019/Applied_AI/darknet_server/data/allData"
#directory = "/home/mmendiet/Courses/Spring_2019/Applied_AI/project_data/allData/test"


i = 0;
print("Train TXT files")
for file in sorted(os.listdir(trainDir)):
    copyfile(trainDir+'/'+file, writeDir+'/'+file)
    if(1%1000):
        print("Number of files: " + str(i))

i = 0;
print("Test TXT files")
for file in sorted(os.listdir(testDir)):
    copyfile(testDir+'/'+file, writeDir+'/'+file)
    if(1%1000):
        print("Number of files: " + str(i))
