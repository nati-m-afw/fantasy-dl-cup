from main import db

#joint user and players table
class userPlayers(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    players_id = db.Column(db.Integer, db.ForeignKey('players.id'), nullable=False)
    gameweek_id = db.Column(db.Integer, db.ForeignKey('gameweek.id'), nullable=False)
    status = db.Column(db.String, nullable=False)
    def __init__(self,user_id,players_id,gameweek_id,status):
        
       
        self.user_id=user_id,
        self.players_id = players_id,
        self.gameweek_id=gameweek_id,
        self.status = status
        
    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'players_id': self.players_id,
            "gameweek_id":self.gameweek_id,
            'status': self.status,
        }

    def __repr__(self):
        return f"userPlayers('{self.user_id}', '{self.players_id}')"
