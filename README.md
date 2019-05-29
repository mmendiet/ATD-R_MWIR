# ATD-R_MWIR
Automatic Target Detection and Recognition for MWIR Imagery

## Folder - ATD_MWIR:
### Folder - configuration4:
    configuration4.cfg: Configuration file for this network as explained in the report.
    configuration4_4000.weights: Weights of trained network after 4000 iterations (Needs to be downloaded, see instructions at the bottom of the page)

### Folder: scripts_allData
    parseTestGT_all.py: Parsing Script for all testing data ground truth
    parseTrainGT_all.py: Parsing Script for all training data ground truth
    allData_guideFiles.py: Parsing script to write guiding text documents for training and testing in Darknet
    testAll.txt: Darknet guide file for testing
    trainAll.txt Darknet guide file for training
    allJPG_parse.py: Python script to combine all jpg testing and training images into allData folder for Darknet
    allTXT_parse.py: Python script to combine all gourng truth label txt files for testing and training images into allData folder for Darknet
    Macro3.jim: ImageJ script used to convert arf image sequence format of database images into jpg images for use in Darknet

### Folder - testImage:
Contains three test jpg images

### Top Level
allData.data: Setup file needed to run Darknet model. Specifies the number of classes and where to find class names
alldata.names: Contains class names

ATD_image_demo.sh: Bash script for running trained model on testImage set

ATD_video_demo.sh: Bash script for running trained model on demo.mp4 video

demo.mp4: Video with segments of all test set senarios (Needs to be downloaded, see instructions at the bottom of the page) 

testImage.txt: Contains image paths for runing ATD_image_demo.sh

demonstration.mp4: Screen capture showing the steps to run the provided network, as well as shows the network running on the test images and demo video. (Needs to be downloaded, see instructions at the bottom of the page)

## Steps to complete first
    First, clone this repository, and rename it to ATD_MWIR.
    Next, download the network weights here: https://drive.google.com/open?id=1w1_NocNTNXofW-BT_mZLheRRXpNM2R3X
        Place this .weights file inside the "configuration 4" folder.
    Then, download the demo video here: https://drive.google.com/open?id=1CGVT3MYePIYaGVQ2szsiaQw2rb9RRf4x
        Place this video in the top level.
    Next, download this instruction video: https://drive.google.com/open?id=1XScnhttBi5f4Glitnhp77OYNcDhm8ZBQ
        This video shows the steps for running the detection network on images and videos. The steps are explained below.

## Steps completed in the video:
1. git clone https://github.com/AlexeyAB/darknet.git
    NOTE: Ensure that all depadancies for this repository (https://github.com/AlexeyAB/darknet) are installed and functioning
2. Open the darknet folder, and edit the MakeFile
3. In the MakeFile, make GPU=1, CUDNN=1, CUDNN_HALF=1, and OPENCV=1
4. Type make into the terminal inside the darnet folder
5. Copy the ATD_MWIR folder into the darknet folder
6. Enter the ATD_MWIR folder
7. Copy the ATD_image_demo.sh and ATD_image_demo.sh to the root darknet folder
8. In the terminal (in the root darknet folder) enter bash ATD_image_demo.sh
    The image demo should begin. Press any key to cycle through the images
9. In the terminal (in the root darknet folder) enter bash ATD_video_demo.sh
    The video demo should begin.

