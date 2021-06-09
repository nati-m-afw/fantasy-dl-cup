# Importing
from flask import Blueprint, request, jsonify
from models.players import Players
from models.users import Users
from models.user_players import userPlayers
from models.department import Dept
from models.gameweek import Gameweek
from flask_cors import cross_origin
from main import db

#Creating Blueprint for api
api_app = Blueprint("api",__name__)


# DEMO ARRAY OF PLAYERS LIST
# PLAYERS = [
#     {
#      "dept_id": 1, 
#      "fname": "Manu", 
#      "id": 1, 
#      "lname": "GK", 
#      "position": "goalkeeper"
#    }, 
#    {
#      "dept_id": 2, 
#      "fname": "Fanny", 
#      "id": 2, 
#      "lname": "Gk", 
#      "position": "goalkeeper"
#    }, 
#    {
#      "dept_id": 4, 
#      "fname": "Ranjit", 
#      "id": 12, 
#      "lname": "GK", 
#      "position": "goalkeeper"
#    }
# ]


###############################################################

#Route to get players by position
@api_app.route('/getplayers/<pos>')
@cross_origin()
def getPlayers(pos):
    response = { 'status': 'success'}
   
    player =  db.session.query(Players, Dept.dName).filter_by(position = pos).join(Dept).all()
    response['players'] = list(map(lambda p: addDNameToResponse(p[0].serialize(), p[1]), player))
   
    return response
    

# Helper Function
# Add status to player data in get_team response
def addDNameToResponse(player, department):
    result = player
    result.update( {'department': department} )
    return result


# MOCK_DATA = {
#     "userId" : 1, 
#     "team": [1,10,2,3,4,5,6,7,8,9],
#     "gameweekId": 1
# }

# Route to update user_players table
@api_app.route('/updateuserplayers', methods=['POST'])
def update_team():
    if request.method=='POST':
        requestBody = request.get_json()
        
        # Delete old team
        db.session.query(userPlayers).filter(userPlayers.user_id == requestBody['userId'], userPlayers.gameweek_id == requestBody['gameweekId']).delete()
        # print(a)
        for gameweek in range(requestBody['gameweekId'], 6):
            for player in requestBody['team']:
                ### Add GAMEWEEK column
                up = userPlayers(user_id=requestBody['userId'], players_id=player['playerId'], gameweek_id=gameweek, status=player['status'])
                db.session.add(up)
        db.session.commit()
        return "201"


# Get users team
### Add GAMEWEEK parameter
@api_app.route('/getteam/<userId>/<gameweekId>')
def get_team(userId, gameweekId):
    response = { 'status': 'success' }

    team = (db.session.query(userPlayers, Players, Users, Dept, Gameweek).with_entities(Players, userPlayers.status, Dept.dName)
    .join(Users)
    # .join(userPlayers)
    .join(Players)
    .join(Dept)
    .join(Gameweek)
    .filter(Users.id==userId, Gameweek.id==gameweekId)).all()
    
    response['team'] = list(map(lambda p: addStatusToResponse(p[0].serialize(), p[1], p[2]), team))
    response['gameweekId'] = gameweekId
    return response


# Get Acitve Gameweek
@api_app.route('/getactivegw')
def get_active_gameweek():
    response = { 'status': 'success' }

    gw = Gameweek.query.filter_by(status='ACTIVE').first()

    if gw is None:
        response['activeGW'] = 0
    else:
        response['activeGW'] = gw.id

    return response

# Helper Function
# Add status to player data in get_team response
def addStatusToResponse(player, status, department):
    result = player
    result.update( {'status': status } )
    result.update( {'department': department} )
    return result