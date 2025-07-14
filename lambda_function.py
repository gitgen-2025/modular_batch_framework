from yourdata.config import load_config
from yourdata.batch_runner import run_all_tasks
from yourdata.logger import get_logger

logger = get_logger()

def lambda_handler(event, context):
    logger.info("Lambda function invoked.")
    config = load_config()
    run_all_tasks(config)
    logger.info("Lambda function completed.")
    return {"statusCode": 200, "body": "Success"}
