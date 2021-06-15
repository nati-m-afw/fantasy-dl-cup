# Importing Flask , Blueprint and SQL Alchemy
from flask import Flask, Blueprint,json 
from flask_sqlalchemy import SQLAlchemy

from datetime import timedelta

# Library for importing environment variables
from dotenv import load_dotenv


# Importing JWT
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

#Library to enable cors
from flask_cors import CORS,cross_origin
import os

# Create App Instance
app = Flask(__name__)
jwt = JWTManager(app)

#App configs
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("SQLALCHEMY_DATABASE_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS")
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=20000)

# Creating DB Instance
db = SQLAlchemy(app)

# Creating JWT Instance
jwt = JWTManager(app)

# Import - to avoid circular Import
from api.api import api_app
from auth.auth import auth_app
from admin.admin import admin_app


# Enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# Load .env variables
load_dotenv()


#Import Database Models
from models.department import Dept
from models.event import Event
from models.gameweek import Gameweek
from models.matches import Match
from models.players import Players
from models.score import Scores
from models.statistics import StatInfo
from models.user_players import userPlayers
from models.users import Users


# Create Tables 
db.create_all()

# Populate with Data
from scripts.populate import populate
# populate()


# Test Route
@app.route("/")
def test():
    return "AAA"


#Registering Blueprints
app.register_blueprint(api_app,url_prefix="")
app.register_blueprint(auth_app,url_prefix="/auth")
app.register_blueprint(admin_app,url_prefix="/admin")
# Run From Main only
if __name__ == '__main__':
    app.run()