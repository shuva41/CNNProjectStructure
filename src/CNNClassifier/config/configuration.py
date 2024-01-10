from CNNClassifier.utils.utils import read_yaml, create_directory
from CNNClassifier.entity.config_entity import DataIngestionConfig
from CNNClassifier.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from pathlib import Path
import os


class ConfigurationManager:
    # Class to map config_entity.py with config.yaml file
    def __init__(self, config_file_path=CONFIG_FILE_PATH, params_file_path=PARAMS_FILE_PATH):
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)

        # artifacts directory created
        create_directory([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        # artifacts/data_ingestion folder created
        create_directory([config.root_dir])
        # Assign values from config.yaml file to DataIngestionConfig dataclass in config_entity.
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        return data_ingestion_config
