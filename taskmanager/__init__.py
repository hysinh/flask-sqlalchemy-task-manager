import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
if os.path.exists("env.py"):  #in order to use any of the hidden environment variables, import "env" package
    import env  # noqa


app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")

db = SQLAlchemy(app) 

#imported last bc "routes" file will rely on using both the "app" and "db" variables definted about
from taskmanager import routes  # noqa