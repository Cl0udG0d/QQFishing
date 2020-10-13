from flask import Flask
from exts import db
import os



# DEBUG = True
DEBUG = False
SECRET_KEY = os.urandom(24)

HOSTNAME='mysql'
# HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'QQFishing'
USERNAME = 'root'
PASSWORD = 'root'
# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1/tushare?charset=utf8'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT,
                                                                               DATABASE)

SQLALCHEMY_TRACK_MODIFICATIONS = False


app = Flask(__name__)
db.init_app(app)
