from main import db

#dept table model
class Dept(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    dName = db.Column(db.String(20), unique=True,nullable=False) 

    players = db.relationship('Players', backref = 'dep_player', lazy=True )

    def __repr__(self):
        return f"Dept('{self.dName}')"