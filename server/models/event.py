from main import db
class Event(db.Model):
    id =db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    players_id =db.Column(db.Integer, db.ForeignKey('players.id'), nullable=False)
    match_id =db.Column(db.Integer, db.ForeignKey('match.id'), nullable=False)
    gameweek_id =db.Column(db.Integer, db.ForeignKey('gameweek.id'), nullable=False)
    goals_scored = db.Column(db.Integer,nullable=False)
    goals_conceded = db.Column(db.Integer, nullable=False)
    assists_provided = db.Column(db.Integer,nullable=False)
    minutes_played = db.Column(db.Integer,nullable=False)
    yellow_cards = db.Column(db.Integer,nullable=False)
    red_cards = db.Column(db.Integer,nullable=False)
    
    
    def __init__(self,id , players_id,match_id,gameweek_id,goals_scored,goals_conceded,assists_provided,minutes_played,yellow_cards,red_cards, ):
        self.id = id,
        self.players_id=players_id,
        self.match_id=match_id,
        self.gameweek_id=gameweek_id,
        self.goals_scored=goals_scored,
        self.goals_conceded = goals_conceded,
        self.assists_provided=assists_provided,
        self.minutes_played = minutes_played,
        self.yellow_cards = yellow_cards,
        self.red_cards = red_cards,
    
    
    def serialize(self):
        return {
            'id': self.id,
            'player_id': self.players_id,
            'match_id': self.match_id,
            'gameweek_id':self.gameweek_id,
            "goals_scored":self.goals_scored,
            "goals_conceded":self.goals_conceded,
            "assists_provided":self.assists_provided,
            'minutes_played': self.minutes_played,
            "yellow_cards":self.yellow_cards,
            'red_cards':self.red_cards   
        }
    
    def __repr__(self):
        return f"Event('{self.id}')"
    
    