This is a python port of [mfiaDLTS](https://github.com/nelsongt/mfiaDLTS). Please see the dumentation for mfiaDLTS as it mostly will apply to this project with the obvious exception of MATLAB-specific portions. Currently in early development, at the moment should work ok for acquiring transient data. Transient processing is not yet implemented.

![image](https://raw.githubusercontent.com/nelsongt/mfiaDLTS2/master/screenshot.png)
  
  
Hardware Requirements
------------

  -Device to perform DLTS on
  
  -Cryostat with electrical leads for device connection
  
  -Lakeshore 33X temperature controller to control cryostat temperature w/ GPIB interface
  
  -Zurich Instruments MFIA or MFLI with IA module
  
  -PC with python installed to run this code and with GPIB cable and drivers
  
  
Software Dependencies
------------

LabOne: https://www.zhinst.com/downloads
  
Python 3.7 or higher  
-numpy  
-pandas  
-PyQt5  
-pyqtgraph  
-PyMeasure  
-zhinst
  
  
Installation of mfiaDLTS2
------------

Download the source code and extract it to a folder wherever you want.

mfiaDLTS2 requires a ditribution of python 3 and several python dependencies. As of this writing python 3.10 was used successfully. There are many ways to do this but I can make recommendation for beginners:

### Windows

Install [miniconda](https://docs.conda.io/en/latest/miniconda.html). Open the Anaconda Prompt and create a new environment:

    conda create --name mfiaEnv
    
Activate the environment:

    conda activate mfiaEnv

Install as many dependencies with conda as possible using the following:

    conda install numpy pandas PyQt5 pyqtgraph PyMeasure zhinst
  
Then from Anaconda Prompt type to start mfiaDLTS2:
  
    python "path to mfiaMain.py"
  
If you want a way to run the program by double clicking a file you have to edit the mfiaMain.bat file for this. Right click on mfiaMain.bat and hit edit. You will need to replace the path placeholders with the actual paths, eg. "Path where your Python exe is stored\python.exe" will become "C:\Users\myUser\Miniconda3\envs\mfiadlts\python.exe" but of course you will replace myUser with whatever your windows username is. After you are done, save the file. You may now run the program by double clicking this bat file or even create a shortcut to this bat file on the desktop and run from there.
  

### \*Ubuntu

Python and most dependencies can be installed using native package manager. Similar idea will work for Fedora, openSUSE, Arch, etc.

    sudo apt install python3 python3-pip python3-numpy python3-pandas python3-pyqt5 python3-pyqtgraph python3-pymeasure
    
The zhinst package will not be in the distro repository so install that from pip:
    
    pip install zhinst
    
Then to run mfiaDLTS2 use the command line, cd into the mfiaDLTS2 folder and type:
    
    python mfiaMain.py
    
You may use double-click the bash script mfiaMain.sh to run the script without typing anything, but you will probably have to chmod+x the script to get it to run the first time.

### Mac

I am unable to help at this time but it will be similar to above. Instructions can be submitted through the issues or by email.
  


