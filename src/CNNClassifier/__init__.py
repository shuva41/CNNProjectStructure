# logging.FileHandler(log_filepath) -- We will save the logs in a file
# logging.StreamHandler(sys.stdout) -- Whatever we have saved inside the file, will also be available on Command Prompt
###################################################################################
import os
import sys
import logging

# Directory where the logs will be stored
log_dir = 'logs'

# Format of the log message
logging_str = '[%(asctime)s: %(levelname)s: %(module)s]: %(message)s'

# Create the log directory
log_filepath = os.path.join(log_dir, 'CNNClassifierLogs.log')
os.makedirs(log_dir, exist_ok=True)

# Configure the logging
logging.basicConfig(filename=log_filepath,
                    level=logging.INFO,
                    format=logging_str,
                    handlers=[logging.FileHandler(log_filepath), logging.StreamHandler(sys.stdout)])

logger = logging.getLogger('CNNClassifier')
