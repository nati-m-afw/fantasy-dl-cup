from main import db
class StatInfo(db.Model):
    id =db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    players_id =db.Column(db.Integer, db.ForeignKey('players.id'), nullable=False)
    goals_scored = db.Column(db.Integer,nullable=False)
    clean_sheets = db.Column(db.Integer, nullable=False)
    assists_provided = db.Column(db.Integer,nullable=False)
    yellow_cards = db.Column(db.Integer,nullable=False)
    red_cards = db.Column(db.Integer,nullable=False)
    
    
    def __init__(self , players_id,goals_scored,clean_sheets,assists_provided,yellow_cards,red_cards):
        self.players_id=players_id,
        self.goals_scored=goals_scored,
        self.clean_sheets = clean_sheets,
        self.assists_provided=assists_provided,
        self.yellow_cards = yellow_cards,
        self.red_cards = red_cards,
    
    
    def serialize(self):
        return {
            'id': self.id,
            'player_id': self.players_id,
            "goals_scored":self.goals_scored,
            "clean_sheets":self.clean_sheets,
            "assists_provided":self.assists_provided,
            "yellow_cards":self.yellow_cards,
            'red_cards':self.red_cards   
        }
    
    def __repr__(self):
        return f"Event('{self.id}')"
    
    