import inspect
from yourdata import tasks
from yourdata.logger import get_logger

logger = get_logger()

def run_all_tasks(config):
    logger.info("Detecting available tasks...")

    task_classes = [
        cls for name, cls in inspect.getmembers(tasks, inspect.isclass)
        if issubclass(cls, tasks.Task) and cls is not tasks.Task
    ]

    for task_cls in task_classes:
        try:
            logger.info(f"Executing task: {task_cls.__name__}")
            task_instance = task_cls(config)
            task_instance.run()
        except Exception as e:
            logger.error(f"Task {task_cls.__name__} failed with error: {e}")
