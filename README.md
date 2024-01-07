## CNN Classifier Project with proper folder structure and AIOPS

- **Step 01:** Create the 'template.py' to automatically create the folder structure.
  - The Path library is used to avoid the notation conflict of paths in Windows and Linux.
    1.  **Windows path:** F:\Machine_Learning\full_stack_data_science-ineuron\Computer Vision\CNNProjectStructure>
    2.  **Linux path:** /home/ubuntu/full_stack_data_science-ineuron/Computer Vision/CNNProjectStructure>
        > from pathlib import Path  
        > print(Path('x/y/z.txt'))
    3.  **Output:** x\y\z.txt  
        Since, we are using Windows machine. It will become x/y/z.txt if we were using a linux machine. Path library adjusts the path according to the OS.
- **Step 02:** Create setup.py file, for configuring local environment, converting folders into packages, e.t.c
- **Step 03:** Create setup.cfg file. To show the left side description incase the project is published in PYPI
- **Step 04:** Create requirements.txt and requrements_dev.txt. The 2nd file will have some more number of libraries, that are not required in production environment.
- **Step 05:** Create the pyproject,toml file. It contains the information regarding building the project and create a wheel file which will be available to download at PYPI package page.
  1. Setup.py will build the package from the local packages that we have created using the configuration mentioned in this file and setup.cfg file.
- **Step 06:** Create tox.ini file for testing purposes in local environment.
  1. Tox is a tool for automating and standardizing testing in Python. It is a generic virtualenv management and test command line tool you can
- **Step 07:** Automate the environment creation process by init_setup.sh: shell scripting. All commnads to be written in a linux command prompt.
  > bash init_setup.sh
