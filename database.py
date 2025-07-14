import psycopg2
from yourdata.logger import get_logger

logger = get_logger()

def get_connection(config):
    conn = psycopg2.connect(
        host=config['database']['host'],
        dbname=config['database']['name'],
        user=config['database']['user'],
        password=config['database']['password'],
        port=config['database']['port']
    )
    logger.info("Database connection established.")
    return conn

def fetch_sample_data(config):
    conn = get_connection(config)
    cur = conn.cursor()
    cur.execute("SELECT NOW();")
    result = cur.fetchone()
    logger.info(f"Fetched sample data: {result}")
    cur.close()
    conn.close()
