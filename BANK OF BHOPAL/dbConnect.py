import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()
host=os.getenv("DB_HOST")
user=os.getenv("DB_USER")
passwd=os.getenv("DB_PASSWORD")
database=os.getenv("DB_NAME")
def mysql_connection():
    conn = mysql.connector.connect(
        host=host,
        user=user,
        passwd=passwd,
        database=database,
        auth_plugin="mysql_native_password"
          )
    return conn
