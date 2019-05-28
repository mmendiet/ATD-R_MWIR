input = "/media/matias/Seagate Expansion Drive/ATR Database/mydata/arf2/Testing/ZSU23-4/arf/";
output = "/home/matias/Desktop/jpegTest/ZSU23-4jpeg/";

function action(input, output, filename) {
        print(input+filename);
        run("ARF ", "arf=[" + input + filename + "] frames=1800 start=1");
        splitName = split(filename, '.');
        print(splitName[0]);
        run("Image Sequence... ", "format=JPEG name=" + splitName[0] +" start=0 digits=4 use save="+ output);
        close();
}


setBatchMode(true); 
list = getFileList(input);
for (i = 0; i < list.length; i++)
        action(input, output, list[i]);
setBatchMode(false);
