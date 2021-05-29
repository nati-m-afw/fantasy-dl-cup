from main import db

#user table model
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    firebase_id = db.Column(db.String(120),unique=True,nullable=False)
    fname = db.Column(db.String(20),  nullable=False)
    lname = db.Column(db.String(20),  nullable=False)
    teamname = db.Column(db.String(20),  unique=True, nullable=False)
    userPlayers = db.relationship('userPlayers', backref = 'user_user', lazy=True)

    def __repr__(self):
        return f"User('{self.id}','{self.fname}', '{self.lname}', '{self.teamname}')"
