from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config.from_object(os.getenv("APP_SETTINGS", "config.DevConfig"))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/')
def welcome():
    return "A dockerized Flask App"

if __name__ == '__main__':
    # Register your models here
    from models import *

    # run the app
    app.run(host='0.0.0.0')