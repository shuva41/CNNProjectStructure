## CNN Classifier Project with proper folder structure and AIOPS

- **Step 01:** Create the 'template.py' to automatically create the folder structure.
  
  - The Path library is used to avoid the notation conflict of paths in Windows and Linux.
    1. **Windows path:** F:\Machine_Learning\full_stack_data_science-ineuron\Computer Vision\CNNProjectStructure>
    2. **Linux path:** /home/ubuntu/full_stack_data_science-ineuron/Computer Vision/CNNProjectStructure>
       ```python
       from pathlib import Path  
       print(Path('x/y/z.txt'))
       ```
    3. **Output:** x\y\z.txt  
       Since, we are using Windows machine. It will become x/y/z.txt if we were using a linux machine. Path library adjusts the path according to the OS.

- **Step 02:** Create setup.py file, for configuring local environment, converting folders into packages, e.t.c

- **Step 03:** Create setup.cfg file. To show the left side description incase the project is published in PYPI

- **Step 04:** Create requirements.txt and requrements_dev.txt. The 2nd file will have some more number of libraries, that are not required in production environment.

- **Step 05:** Create the pyproject.toml file. It contains the information regarding building the project and create a wheel file which will be available to download at PYPI package page.
  
  1. Setup.py will build the package from the local packages that we have created using the configuration mentioned in this file and setup.cfg file.

- **Step 06:** Create tox.ini file for testing purposes in local environment. tox.ini file initiates the test environment.
  
  1. Tox is a tool for automating and standardizing testing in Python. It is a generic virtualenv management and test command line tool that creates a local environment, in which you can test your packages using pytest

- **Step 07:** Automate the environment creation and package installation process by init_setup.sh: shell scripting. All commnads to be written in a linux command prompt.
  
  ```bash
      bash init_setup.sh
  ```

- **Step 08:** Here we are creating the logger configuration inside the `init.py` file of CNNClassifier/components folder.
  
  1. Whenever, we would import CNNClassifier module, the first thing that will automatically imported and executed will be the `__init__.py` file. Thus logger object will be creted and we will be able to import it.

- **Step 09:** Create the config_entity.py file in the entity folder. It will contain the datatype for input of each component of the project.
  
  1. Create the DataIngestionConfig immutable dataclass, that configures the datatype of the input to the data ingestion component.

- **Step 10:** Create the config.yaml file in the CNNProjectStructure/configs folder. It will contain the values for input to each component of the project.
  
  1. Create the data_ingestion configuration. The values should match the datatype of the DataIngestionConfig dataclass.

- **Step 11:** Create components/utils/utils.py that contains the common functionalities.
  
  1. Create read_yaml function that will read any yaml file and return the content as an object.
  2. Create create_directory function, that creates a folder depending upon the path given in the argument.
  - Understand ensure-annotations decorator from trials.ipynb file

- **Step 12:** Create the following files:
  
  - Create the universal constants in CNNClassifier/constants/`__init__.py` file.
  - Create the configuration.py file in the CNNClassifier/config folder. It will contain all the functions for mapping config_entity.py with config.yaml file.
    1. _get_data_ingestion_config_: This function will map the data_ingestion section of the config.yaml file with the DataIngestionConfig dataclass.

- **Step 13:** Create stage_01_data_ingestion.py file in the components folder. It will create all the codes for the functionalities like downloading data, cleaning data, splitting data, etc.
  
  - _Step 01_ : Function to download file
  - _Step 02_ : Function to extract the list of jpg files
  - _Step 03_ : Function containing the code to Unzip the file
  - _Step 01_ : Function to execute the Unzip operation and then call the function to extract the list of jpg files.

- **Step 14:** Create the data_ingestion_pipeline.py file in the pipeline folder.
  
  1. It will contain the code for connecting CNNProjectStructure/configs/config.yaml, CNNClassifier/entity/config_entity.py and components/data_ingestion.py files.
  2. This is where we are performing the data ingestion step by step, by calling the functions from components/stage_01_data_ingestion.py file.

### Workflow

1. Create trials in research/trials.ipynb
2. Create config.yaml file
3. entity file
4. Create codes in the components
5. Create pipelines for training and prediction
6. Test your packages
7. DVC to reproducing the pipeline
