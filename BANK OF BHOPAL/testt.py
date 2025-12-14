import os
from dotenv import load_dotenv
load_dotenv()
host=os.getenv("DB_HOST")
user=os.getenv("DB_USER")
passwd=os.getenv("DB_PASSWORD")
database=os.getenv("DB_NAME")
print(type(host) , user , passwd , database)