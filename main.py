from yourdata.config import load_config
from yourdata.db import fetch_sample_data
from yourdata.batch_runner import run_all_tasks
from yourdata.logger import get_logger

logger = get_logger()

def main():
    logger.info("Application started.")
    config = load_config()
    fetch_sample_data(config)
    run_all_tasks(config)
    logger.info("Application finished.")

if __name__ == "__main__":
    main()
