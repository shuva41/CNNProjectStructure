####################### Automatic Folder Structure ##############################
############################### Creation ########################################


import os
from pathlib import Path
import logging

# Step01: Setting up the structure of the Log messages
logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s] : %(message)s')
package_name = 'CNNClassifier'

# Step02: List of files we want to create
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/components/__init__.py",
    f"src/{package_name}/utils/__init__.py",
    f"src/{package_name}/config/__init__.py",
    f"src/{package_name}/pipeline/__init__.py",
    f"src/{package_name}/entity/__init__.py",
    f"src/{package_name}/constants/__init__.py",
    "tests/__init__.py",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "configs/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "research/trials.ipynb"
]


for filepath in list_of_files:
    filepath = Path(filepath)

    # Split the file path to get folder and file name.
    filedir,filename = os.path.split(filepath)

    # Create the folder.
    if filedir != '':
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file:{filename}")

# Creating a File, once the folder is already there
    if (not os.path.exists(filepath) or (os.path.getsize(filepath) == 0)):
        with open(filepath, 'w') as f:
            logging.info(f"Creating empty file:{filename}")
    else:
        logging.info(f"File:{filename} already exists")