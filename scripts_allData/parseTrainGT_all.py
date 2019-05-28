import os;
import time

SKIP_INTERVAL = 1

keyword = 'PixLoc'
imageHeight = 512
imageWidth = 640

outputNum = 0
fileType = ".txt"
outputFile = (str(outputNum)+fileType)
outputDir = "/home/mmendiet/Courses/Spring_2019/Applied_AI/project_data/allData/trainingGT_all/"
agtFile = "/home/mmendiet/Courses/Spring_2019/Applied_AI/project_data/mydata_agt/Train"
metFile = "/home/mmendiet/Courses/Spring_2019/Applied_AI/project_data/mydata_bbox/Train"

stringList = []
print("parseTrainGT.py")
for file in sorted(os.listdir(agtFile)):
	#print(file)
	if(file.endswith(".agt")):
		print(file)
		with open (agtFile +"/" + file, 'rt') as in_file:
			frame = SKIP_INTERVAL
			for line in in_file:
				index = line.find(keyword)
				if(index > 0):
					if(frame%SKIP_INTERVAL==0):
						#fullString = line[(index):];
						splitString = line.split()
						x1y1 = (splitString[1] + " " + splitString[2])
						stringList.append(x1y1)
						#time.sleep(.0005)
						#print("here")
					frame = frame + 1;
					#print(frame)
		
		#print(line) # prints that line
listNum = 0;
for file in sorted(os.listdir(metFile)):
	#print(file)
	outputNum = 0;
	if(file.endswith(".bbox_met")):
		print(file)
		with open (metFile +"/" + file, 'rt') as in_file:
			frame = SKIP_INTERVAL
			for line in in_file:
				if(frame%SKIP_INTERVAL==0):
					splitString = line.split(',')

					leftX = float(splitString[9])
					leftY = float(splitString[10])
					xy = stringList[listNum].split()
					centerX = float(xy[0])
					centerY = float(xy[1])

					bWidth = 2*(centerX-leftX)
					bHeight = 2*(centerY-leftY)
					x = centerX/imageWidth
					y = centerY/imageHeight
					width = bWidth/imageWidth
					height = bHeight/imageHeight


					numLen = len(str(outputNum))
					outputNumString = ""
					for i in range (0,abs(numLen-4)):
						outputNumString += str(0)
					outputNumString+=str(outputNum)
					outputFile = (outputDir + file.split('.')[0] + outputNumString+fileType)
					newfile = open(outputFile,"w")
					newfile.write("0 " + str(x) + " " + str(y) + " " + str(width)+ " " + str(height))
					newfile.close()
					#time.sleep(.0005)
					#print(outputFile)
					outputNum = outputNum+1
					listNum = listNum+1;
					#print("0 " + str(x) + " " + str(y) + " " + str(width)+ " " + str(height))
					#print(file.split('.')[0])
				frame = frame + 1;





