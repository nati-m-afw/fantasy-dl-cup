from main import db

#joint user and players table
class userPlayers(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    players_id = db.Column(db.Integer, db.ForeignKey('players.id'), nullable=False)

    def __repr__(self):
        return f"userPlayers('{self.user_id}', '{self.players_id}')"
