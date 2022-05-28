from flask import Flask
from hashids import Hashids
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)  # подключаю конфигурационный файл к сайту
db = SQLAlchemy(app)  # "дружу" базу данных с сайтом
hashid = Hashids(min_length=4, salt=app.config['SECRET_KEY'])

from routes import *

if __name__ == '__main__':
    app.run(adress='0.0.0.0')
