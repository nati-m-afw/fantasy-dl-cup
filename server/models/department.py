from main import db

#dept table model
class Dept(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    dName = db.Column(db.String(20), unique=True,nullable=False) 
    players = db.relationship('Players', backref = 'dep_player', lazy=True )

    def __init__(self,id ,dName ):
        self.id = id,
        self.dName = dName,
        
    
    
    def serialize(self):
        return {
            'id': self.id,
            'team_name': self.dName, 
        }
    
    
    def __repr__(self):
        return f"Dept('{self.dName}')"