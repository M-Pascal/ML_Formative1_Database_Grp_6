import os
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import logging

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s")

def get_connection():
    """Establish a database connection."""
    try:
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST", "n8oow.h.filess.io"),
            user=os.getenv("DB_USER", "CancerDiagnosisDB_givensoon"),
            password=os.getenv("DB_PASSWORD", "c54ce40e7a2d93bccf7f0c9095035c2f86d9bc36"),
            database=os.getenv("DB_NAME", "CancerDiagnosisDB_givensoon"),
            port=int(os.getenv("DB_PORT", 3307)),
            autocommit=False
        )
        return conn
    except Error as e:
        logging.error(f"Database Connection Error: {e}")
        return None