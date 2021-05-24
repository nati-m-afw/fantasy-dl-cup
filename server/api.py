from flask import Flask, session, render_template, request, redirect, url_for, jsonify, json
from dotenv import load_dotenv
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
load_dotenv()



# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# DEMO ARRAY OF PLAYERS LIST
# PLAYERS = [
#     {
#         'name': 'gk',
#         'price': '3.5',
#         'position': 'gk'
#     },
#     {
#         'name': 'Bguy',
#         'price': '4.5',
#         'position': 'mid'
    
#     },
#     {
#         'name': 'Bguy',
#         'price': '4.5',
#         'position': 'stk'
#     }
# ]
# sqllite db uri
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("SQLALCHEMY_DATABASE_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS")
#db instance
db = SQLAlchemy(app)

# player table model
class Players(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    fname = db.Column(db.String(20),  nullable=False)
    lname = db.Column(db.String(20),  nullable=False)
    position = db.Column(db.String(20), nullable=False)
    # price = db.Column(db.Decimal(5,5), nullable=False)
    dept_id = db.Column(db.Integer, db.ForeignKey('dept.id'), nullable=False)

    def __init__(self, fname, lname, position, dept_id):
        self.fname = fname
        self.lname = lname
        self.position = position
        self.dept_id = dept_id
    def serialize(self):
        return {
            'id': self.id,
            'fname': self.fname,
            'lname': self.lname,
            'position': self.position,
        }


    def __repr__(self):
        return f"Players('{self.fname}', '{self.lname}','{self.position}','{self.dept_id}')"

#dept table model
class Dept(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    dName = db.Column(db.String(20), unique=True,nullable=False) 

    players = db.relationship('Players', backref = 'dep_player', lazy=True )

    def __repr__(self):
        return f"Dept('{self.dName}')"

###########################################################################################################################################
@app.route('/getplayers/<pos>')
@cross_origin()
def getPlayers(pos):
    response = { 'status': 'success'}
   
    player =  Players.query.filter_by(position = pos).all()
    response['players'] = list(map(lambda p: p.serialize(), player))
   
    return response
    


if __name__ == '__main__':
    app.run()