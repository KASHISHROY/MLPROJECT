##any execution that happens log all those information,so that we can track if there is any error
import logging
import os
from datetime import datetime

# Create log file name with timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create logs file path->will be inside the cwd insilde logs folder
logs_path = os.path.join(os.getcwd(), "logs",LOG_FILE)
# Create logs directory if not exists
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
)


