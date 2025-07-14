from yourdata.logger import get_logger

logger = get_logger()

class Task:
    def __init__(self, config):
        self.config = config

    def run(self):
        raise NotImplementedError("Each task must implement a run() method.")

class ExampleBatchJob(Task):
    def run(self):
        logger.info(f"Running: {self.__class__.__name__}")
        for i in range(3):
            logger.info(f"Step {i + 1}/3 complete.")
        logger.info(f"{self.__class__.__name__} completed.")
