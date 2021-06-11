
from main import db

# player table model
class Scores(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    players_id =db.Column(db.Integer, db.ForeignKey('players.id'), nullable=False)
    match_id =db.Column(db.Integer, db.ForeignKey('match.id'), nullable=False)
    gameweek_id =db.Column(db.Integer, db.ForeignKey('gameweek.id'), nullable=False)
    score = db.Column(db.Integer,nullable=False)
    
    def __init__(self, players_id, match_id, gameweek_id,score):
        
        self.players_id = players_id,
        self.match_id = match_id,
        self.gameweek_id = gameweek_id
        self.score = score
    
    
    
    def serialize(self):
        return {
           
            'players_id': self.players_id,
            'match_id': self.match_id,
            'gameweek_id': self.gameweek_id,
            "score":self.score
            
        }



