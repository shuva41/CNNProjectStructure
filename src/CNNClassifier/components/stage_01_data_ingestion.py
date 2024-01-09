import os                            # To interact with the OS
import urllib.request as request     # To make request to a server
from zipfile import ZipFile          # To unzip the downloaded file
from CNNClassifier import logger     # The first file that will be executed is   __init__.py
from pathlib import Path
from tqdm import tqdm           # To showcase the Progressbar
from CNNClassifier.entity import DataIngestionConfig  # Import the config for input
from CNNClassifier.utils import utils


class DataIngestion:
    # This is where we are passing the configuration in config.yaml file to the DataIngestion class in stage_01_data_ingestion.py file. The type of the configuration is DataIngestionConfig dataclass from src\CNNClassifier\entity\entity.py file.
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        pass

    def get_updated_list_of_files(self):
        pass

    def preprocess(self):
        pass

    def unzip_and_clean(self):
        pass
