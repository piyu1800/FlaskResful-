import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
username = os.getenv("DB_USERNAME", "root")
password = os.getenv("DB_PASSWORD","PK_123456")
host = os.getenv("DB_HOST", "localhost")
database = os.getenv("DB_NAME", "flask_restful")

DATABASE_URI = "mysql+pymysql://{}:{}@{}/{}".format(username, password,host, database)

print(DATABASE_URI)