# Importing Libs
from flask import Flask, Blueprint,json 
from flask_sqlalchemy import SQLAlchemy

# Library for importing environment variables
from dotenv import load_dotenv

#Library to enable cors
from flask_cors import CORS,cross_origin
import os

# Create App Instance
app = Flask(__name__)

#App configs
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("SQLALCHEMY_DATABASE_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS")

# Creating DB Instance
db = SQLAlchemy(app)

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
from models.players import Players
from models.user_players import userPlayers
from models.users import Users
from models.matches import Match

# Create Tables 
db.create_all()

# Populate with Data
from scripts.populate import populate
# populate()


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