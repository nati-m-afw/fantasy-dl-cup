from main import db
class Event(db.Model):
    id =db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    players_id =db.Column(db.Integer, db.ForeignKey('players.id'), nullable=False)
    match_id =db.Column(db.Integer, db.ForeignKey('match.id'), nullable=False)
    gameweek_id =db.Column(db.Integer, db.ForeignKey('gameweek.id'), nullable=False)
    

    def __repr__(self):
        return f"Event('{self.id}')"
    
    