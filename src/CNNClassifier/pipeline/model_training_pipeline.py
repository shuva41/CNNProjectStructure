from CNNClassifier.config.configuration import ConfigurationManager
from CNNClassifier.components.intermediate_prepare_callbacks import PrepareCallback
from CNNClassifier.components.stage_03_train import Training
from CNNClassifier import logger
 

config = ConfigurationManager()

prepare_callbacks_config = config.get_prepare_callback_config()
prepare_callbacks = PrepareCallback(config=prepare_callbacks_config)
callback_list = prepare_callbacks.get_tb_ckpt_callbacks()
    
training_config = config.get_training_config()
training = Training(config=training_config)
training.get_base_model()
training.train_valid_generator()
training.train(
        callback_list=callback_list
    )
