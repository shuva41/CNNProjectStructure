from CNNClassifier.components.stage_01_data_ingestion import DataIngestion
from CNNClassifier.config.configuration import ConfigurationManager
from CNNClassifier import logger

logger.info("Stage 01: Data Ingestion started.")
# Setting Configuration of Input for dat_ingestion.
config = ConfigurationManager()
data_ingestion_config = config.get_data_ingestion_config()
# This is where we are passing the configuration in config.yaml file to the DataIngestion class in stage_01_data_ingestion.py file.
data_ingestion = DataIngestion(config=data_ingestion_config)

# Download the data from the given url or database.
logger.info("Downloading Data")
data_ingestion.download_file()
logger.info("Downloaded Data Successfully")

# Unzip and clean the data
logger.info("Unzipping and Cleaning Data")
data_ingestion.unzip_and_clean()
logger.info("Unzipped and Cleaned Data Successfully")

logger.info("Stage 01: Data Ingestion completed successfully.")
