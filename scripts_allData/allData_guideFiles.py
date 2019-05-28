import os;
import time
from shutil import copyfile

SKIP_INTERVAL = 1

keyword = 'PixLoc'
imageHeight = 512
imageWidth = 640

outputNum = 0
fileTypeJ = ".jpg"
fileType = ".txt"


#read jpg files
#trainDir = "/home/mmendiet/Courses/Spring_2019/Applied_AI/project_data/allData/jpegTraining/"
#testDir = "/home/mmendiet/Courses/Spring_2019/Applied_AI/project_data/allData/jpegTest/"
#writeDir = "/home/mmendiet/Courses/Spring_2019/Applied_AI/darknet_server/data/allData"


#trainFolders = ['2S3jpeg','BMP2jpeg','BRDM2jpeg','BTR70jpeg','Pickupjpeg','T72jpeg']
#testFolders = ['SUVjpeg','ZSU23-4jpeg']

#copy jpg file names to train.txt and test.txt with jpegDir
outputTrainFile = "/home/mmendiet/Courses/Spring_2019/Applied_AI/darknet_server/data/allData_info/trainAll.txt"
outputTestFile = "/home/mmendiet/Courses/Spring_2019/Applied_AI/darknet_server/data/allData_info/testAll.txt"
jpegDir = "data/allData_info/allData/"

#copy GT file with that name to output folder with all GT txt files
copyTestDir = "/home/mmendiet/Courses/Spring_2019/Applied_AI/project_data/allData/testGT_all"
copyTrainDir = "/home/mmendiet/Courses/Spring_2019/Applied_AI/project_data/allData/trainingGT_all"
#outputGTDir = "/home/mmendiet/Courses/Spring_2019/Applied_AI/darknet_server/data/allData_info/allData/"
outputGTDir = "/home/mmendiet/Courses/Spring_2019/Applied_AI/project_data/allData/allData/"


print("allData_guideFiles.py")
trainTXT = open(outputTrainFile,"a")
for file in sorted(os.listdir(copyTrainDir)):
	#print(file)
	if(file.endswith(".txt")):
		splitString = file.split('.')
		trainTXT.write(jpegDir+splitString[0]+fileTypeJ+"\n")
		copyFile = splitString[0] + fileType
		copyfile(copyTrainDir +'/'+ copyFile, outputGTDir + copyFile)
		print(splitString[0])
trainTXT.close()


print("allData_guideFiles.py\n\n")
testTXT = open(outputTestFile,"a")
for file in sorted(os.listdir(copyTestDir)):
	#print(file)
	if(file.endswith(".txt")):
		splitString = file.split('.')
		testTXT.write(jpegDir+splitString[0]+fileTypeJ+"\n")
		copyFile = splitString[0] + fileType
		copyfile(copyTestDir +'/'+ copyFile, outputGTDir + copyFile)
		print(splitString[0])
testTXT.close()


