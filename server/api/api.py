# Importing
from flask import Blueprint
from models.players import Players
from flask_cors import cross_origin

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
#     "user_id" : 1, 
#     "myTeam":{
#         "goalkeeper":[
#             {
#                 "fname":"Manu",
#                 "id":1,
#                 "lname":"GK"

#             }
#         ]
#     }
# }

# Route to save user selected team
# @app.route('/saveteam', methods=['POST'])
# def save_team():
#     if request.method=='POST':
#         requestbody = request.get_json()
        # 