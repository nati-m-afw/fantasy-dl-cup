from flask import Flask, session, render_template, request, redirect, url_for, jsonify
from dotenv import load_dotenv
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
load_dotenv()



# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


PLAYERS = [
    {
        'name': 'Sportsguy',
        'price': '3.5'
    },
    {
        'name': 'Bguy',
        'price': '4.5'
    }
]
# sqllite db uri
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:6549@localhost/FantasyDL'
#db instance
db = SQLAlchemy(app)
# marshmallow app created
# ma = Marshmallow(app)

# player table model
class Players(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    fname = db.Column(db.String(20),  nullable=False)
    lname = db.Column(db.String(20),  nullable=False)
    position = db.Column(db.String(20), nullable=False)
    # price = db.Column(db.Decimal(5,5), nullable=False)
    dept_id = db.Column(db.Integer, db.ForeignKey('dept.id'), nullable=False)


    def __repr__(self):
        return f"Players('{self.fname}', '{self.lname}','{self.position}','{self.dept_id}')"

#dept table model
class Dept(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    dName = db.Column(db.String(20), unique=True,nullable=False) 

    players = db.relationship('Players', backref = 'dep_player', lazy=True )

    def __repr__(self):
        return f"Dept('{self.dName}')"



#marshmallow output schema
# class playerSchema(ma.Schema):
#     class Meta:
#         model = Players
#         #if foreign key
#         # include_fk=True 

# #schema to dump and load ORM objects

# player_schema = playerSchema()


@app.route('/getplayers/<pos>')
def getPlayers(pos):
    # response = { 'status': 'success'}
    # response['players'] = PLAYERS
    
    player =  Players.query.filter_by(position = pos).first()
    return str(player)
    


if __name__ == '__main__':
    app.run()