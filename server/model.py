from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# app = Flask(__name__)
# app.config['SECRET_KEY']='6d2f21b7e684870fa1b497af3d8f0a4f'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///players.db'
# db = SQLAlchemy(app) 

# class Players(db.Model):
#     id = db.Column(db.Integer, primary_key=True, nullable=False)
#     fname = db.Column(db.String(20),  nullable=False)
#     lname = db.Column(db.String(20),  nullable=False)
#     position = db.Column(db.String(20), nullable=False)
#     # price = db.Column(db.Decimal(5,5), nullable=False)
#     # depId = db.column(db.Integer), nullable=False) 

#     def __repr__(self):
#         return f"Players('{self.fname}', '{self.position}')"
