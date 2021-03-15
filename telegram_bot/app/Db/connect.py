import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

conn = psycopg2.connect(host=os.getenv("db_host"),
                        port=os.getenv("db_port"),
                        database=os.getenv("db_name"),
                        user=os.getenv("db_user"),
                        password=os.getenv("db_user_password"))
print("Database opened successfully")