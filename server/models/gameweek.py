from main import db

class Gameweek(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    status = db.Column(db.String, nullable=False) 
    event = db.relationship('Event', backref='gw_event', lazy=True)

    def __repr__(self):
        return f"Gameweek('{self.id}', '{self.status}'"
    