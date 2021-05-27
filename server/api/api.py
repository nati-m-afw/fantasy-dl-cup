# Importing
from flask import Blueprint, request, jsonify
from models.players import Players
from models.users import Users
from models.user_players import userPlayers
from flask_cors import cross_origin
from main import db

#Creating Blueprint for api
api_app = Blueprint("api",__name__)


# DEMO ARRAY OF PLAYERS LIST
# PLAYERS = [
#     {
#         'name': 'gk',
#         'price': '3.5',
#         'position': 'gk'
#     },
#     {
#         'name': 'Bguy',
#         'price': '4.5',
#         'position': 'mid'
    
#     },
#     {
#         'name': 'Bguy',
#         'price': '4.5',
#         'position': 'stk'
#     }
# ]


###############################################################

#Route to get players by position
@api_app.route('/getplayers/<pos>')
@cross_origin()
def getPlayers(pos):
    response = { 'status': 'success'}
   
    player =  Players.query.filter_by(position = pos).all()
    response['players'] = list(map(lambda p: p.serialize(), player))
   
    return response
    


# MOCK_DATA = {
#     "userId" : 1, 
#     "team": [1,10,2,3,4,5,6,7,8,9],
#     "gameweekId": 1
# }

# Route to update user_players table
@api_app.route('/updateuserplayers', methods=['POST'])
def save_team():
    if request.method=='POST':
        requestBody = request.get_json()
        for playerId in requestBody['team']:
            up = userPlayers(user_id=1, players_id=playerId)
            db.session.add(up)
        db.session.commit()
        return "201"


# Get users team
@api_app.route('/getteam/<userId>')
def get_team(userId):
    response = { 'status': 'success'}

    team = (db.session.query(userPlayers, Players, Users)
    .join(Users)
    # .join(userPlayers)
    .join(Players)
    .filter(Users.id==userId)).all()
    
    response['team'] = list(map(lambda p: p[1].serialize(), team))
    return response