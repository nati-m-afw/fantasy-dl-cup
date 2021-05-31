from main import db

# player table model
class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    team = db.Column(db.Integer,  nullable=False)
    opponent = db.Column(db.Integer,  nullable=False)
    game_week = db.Column(db.Integer,nullable=False)
    time = db.Column(db.String(20),nullable=False)
    date = db.Column(db.String(20),nullable=False)
    state = db.Column(db.Integer,nullable=False)
    score = db.Column(db.String(20),nullable=True)
    
    
    def __init__(self, team,opponent,game_week,time,date,state,score):
        self.team= team
        self.opponent = opponent
        self.game_week = game_week
        self.time = time
        self.date = date
        self.state = state
        self.score = score
        
    def serialize(self):
        return {
            'id': self.id,
            'team': self.team,
            'opponent': self.opponent,
            "game_week":self.game_week,
            'time': self.time,
            'date':self.date,
            'state':self.state,
            "score":self.score
        }