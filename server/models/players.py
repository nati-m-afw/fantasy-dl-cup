from dotenv import main
from main import db

# player table model
class Players(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    fname = db.Column(db.String(20),  nullable=False)
    lname = db.Column(db.String(20),  nullable=False)
    position = db.Column(db.String(20), nullable=False)
    # price = db.Column(db.Decimal(5,5), nullable=False)
    dept_id = db.Column(db.Integer, db.ForeignKey('dept.id'), nullable=False)
    userPlayers = db.relationship('userPlayers', backref = 'user_player', lazy=True)
    
    
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
