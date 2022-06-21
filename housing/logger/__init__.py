import logging
from datetime import datetime
import os
from re import L

LOG_DIR="housing_logs"

current_time=f"{datetime.now().strftime('%Y-%M-%d-%H-%M-%S')}"
LOG_FILE_NAME="log-{current_time}.log"

os.makedirs(LOG_FILE_NAME,exist_ok=True)

LOG_FILE_PATH=os.path.join(LOG_DIR,LOG_FILE_NAME)

logging.basicConfig(filename=LOG_FILE_PATH,filemode='w',
format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
level=logging.INFO
)