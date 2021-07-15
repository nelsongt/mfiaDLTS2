This is a python port of [mfiaDLTS](https://github.com/nelsongt/mfiaDLTS). Please see the dumentation for mfiaDLTS as it mostly will apply to this project with the obvious exception of MATLAB-specific portions. Currently in early development, at the moment should work ok for acquiring transient data. Transient processing is not yet implemented.

![image](https://raw.githubusercontent.com/nelsongt/mfiaDLTS2/master/screenshot.png)


Hardware Requirements
------------

  -Device to perform DLTS on
  
  -Cryostat with electrical leads for device connection
  
  -Lakeshore 33X temperature controller to control cryostat temperature w/ GPIB interface
  
  -Zurich Instruments MFIA or MFLI with IA module
  
  -PC with python installed to run this code and with GPIB cable and drivers


Installation of mfiaDLTS2
------------

Download the source code and extract it to a folder wherever you want.

mfiaDLTS2 requires a ditribution of python 3 and several python dependencies. As of this writing python 3.9 was used successfully. There are many ways to do this but I can make recommendation for beginners:

### Windows

Install [miniconda](https://docs.conda.io/en/latest/miniconda.html). Open the Anaconda Prompt and install dependencies with the following:

    pip install numpy pandas PyQt5 pyqtgraph PyMeasure zhinst
  
Then from Anaconda Prompt type to start mfiaDLTS2:
  
    python <path to mfiaMain.py>
  
If you want a way to run the program by double clicking a file you have to create a .bat file for this. Using notepad, write this:
    
    @echo off
    <path to python.exe> <path to mfiaMain.py>
    pause
    
and save that as a file named mfiaDLTS2.bat, you may run the program from this bat file or even create a shortcut to this bat file on the desktop and run from there.
  

### \*Ubuntu

Python and most dependencies can be installed using native package manager. Similar idea will work for Fedora, openSUSE, Arch, etc.

    sudo apt install python3 python3-pip python3-numpy python3-pandas python3-pyqt5 python3-pyqtgraph python3-pymeasure
    
The zhinst package will not be in the distro repository so install that from pip:
    
    pip install zhinst
    
Then to run mfiaDLTS2 use the command line, cd into the mfiaDLTS2 folder and type:
    
    python mfiaMain.py
    

### Mac

Sorry, I am unable to help at this time but it will be similar to above.
  


