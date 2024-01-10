from CNNClassifier.config.configuration import ConfigurationManager
from CNNClassifier.components.stage_02_prepare_base_model import PrepareBaseModel
from CNNClassifier import logger

config = ConfigurationManager()

# Load prepare_base_model parameter values from config.yaml to PrepareBaseModelConfig dataclass.
prepare_base_model_config = config.get_prepare_base_model_config()

logger.info("Stage 02: Prepare Base Model started.")

# Loading input parameters from PrepareBaseModelConfig dataclass to stage_02_prepare_base_model.py file.
prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
prepare_base_model.get_base_model()
logger.info("Stage 02: Base VGG16 model created successfully. Base model is saved.")
prepare_base_model.update_base_model()
logger.info("Stage 02: Base VGG16 model updated successfully. Final model is saved.")
logger.info("Stage 02: Prepare Base Model completed successfully.")
