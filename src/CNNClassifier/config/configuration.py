from CNNClassifier.utils.utils import read_yaml, create_directory
from CNNClassifier.entity.config_entity import DataIngestionConfig, PrepareBaseModelConfig
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
        '''
            1. This function stores the data ingestion configuration parameters from config.yaml file into the DataIngestionConfig dataclass.
            2. This function also creates the artifacts/data_ingestion folder.
        '''
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

        def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
            # Load parameters for stage02_prepare_base_model.py component
            config = self.config.prepare_base_model

            # artifacts/prepare_base_model folder created
            create_directory([config.root_dir])

            # Assign values from config.yaml file to PrepareBaseModelConfig dataclass in config_entity.
            prepare_base_model_config = PrepareBaseModelConfig(
                root_dir=Path(config.root_dir),
                base_model_path=Path(config.base_model_path),
                updated_base_model_path=Path(config.updated_base_model_path),
                params_image_size=self.params.IMAGE_SIZE,
                params_learning_rate=self.params.LEARNING_RATE,
                params_include_top=self.params.INCLUDE_TOP,
                params_weights=self.params.WEIGHTS,
                params_classes=self.params.CLASSES
            )

            return prepare_base_model_config
