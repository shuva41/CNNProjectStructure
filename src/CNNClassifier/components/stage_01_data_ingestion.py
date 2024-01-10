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
        if not os.path.exists(self.config.local_data_file):
            logger.info("Downloading Data")
            filename, header = request.urlretrieve(url=self.config.source_URL, filename=self.config.local_data_file)
        else:
            logger.info("Data already downloaded")

    def get_updated_list_of_files(self, list_of_files):
        return [f for f in list_of_files if f.endswith('.jpg')]

    def preprocess(self, zf: ZipFile, f: str, working_dir: str):
        target_file_path = os.path.join(working_dir, f)
        if not os.path.exists(target_file_path):
            zf.extract(f, working_dir)
            # os.rename(os.path.join(working_dir, f), target_file_path)

    def unzip_and_clean(self):
        with ZipFile(self.config.local_data_file, mode='r') as zipObj:
            list_of_files = zipObj.namelist()
            # Extracting the jpg files
            updated_list_of_file = self.get_updated_list_of_files(list_of_files)
            for f in tqdm(updated_list_of_file):
                # For showing progress of preprocessing.
                self.preprocess(zipObj, f, self.config.unzip_dir)
