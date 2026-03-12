"""
The flask application package.
"""
import logging
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session
#from flask import flash, render_template, redirect, request
#from FlaskWebProject import app

app = Flask(__name__)
app.config.from_object(Config)


# Configure logging
#stream_handler = logging.StreamHandler()
#stream_handler.setLevel(logging.WARNING)

#app.logger.setLevel(logging.WARNING)
#app.logger.addHandler(stream_handler)

    

Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

import FlaskWebProject.views
