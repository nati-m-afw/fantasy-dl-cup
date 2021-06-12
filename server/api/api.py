# Importing
from flask import Blueprint, request, jsonify
from models.players import Players
from models.users import Users
from models.user_players import userPlayers
from models.department import Dept
from models.gameweek import Gameweek
from models.matches import Match
from models.score import Scores
from models.statistics import StatInfo

from flask_cors import cross_origin
from main import db
from flask_restx import Resource , Api

#Creating Blueprint for api
api_app = Blueprint("api",__name__)
api = Api(api_app)

###############################################################


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


#mock data 
# team1 = 1
# score = 
# mckdata[team1]['points'] =

# #MOCK_DATA={
# # "1" : {
# #   "teamName":"IT",
# #   "teamId":1,
# #   "points": 15,
# #   "last5": ["W","w","W","w","W"]
# #   "played":,
# #   "won":0,
# #   "drawn":5,
# #   "lost":0,
# #   "GF":
# # },
# # "2": {
# # }
# # }

#get table route
@api_app.route('/gettable')
def get_table():
    response={'status':'success'}
    table = {
        # IT
        "1":{
            "teamName":"IT",
            "teamId": 1,
            "points": 0,
            "last5": [],
            "played": 0,
            "won": 0,
            "drawn": 0,
            "lost": 0,
            "GF":0,
            "GA":0
        },
        "2": {
            "teamName":"Mech",
            "teamId": 2,
            "points": 0,
            "last5": [],
            "played": 0,
            "won": 0,
            "drawn": 0,
            "lost": 0,
            "GF":0,
            "GA":0
        },
        "3": {
            "teamName":"Elec",
            "teamId": 3,
            "points": 0,
            "last5": [],
            "played": 0,
            "won": 0,
            "drawn": 0,
            "lost": 0,
            "GF":0,
            "GA":0
        },
        "4":{
            "teamName":"SE",
            "teamId": 4,
            "points": 0,
            "last5": [],
            "played": 0,
            "won": 0,
            "drawn": 0,
            "lost": 0,
            "GF":0,
            "GA":0
        },
        "5":{
            "teamName":"Chemical",
            "teamId": 5,
            "points": 0,
            "last5": [],
            "played": 0,
            "won": 0,
            "drawn": 0,
            "lost": 0,
            "GF":0,
            "GA":0
        },
        "6":{
            "teamName":"BioMed",
            "teamId": 6,
            "points": 0,
            "last5": [],
            "played": 0,
            "won": 0,
            "drawn": 0,
            "lost": 0,
            "GF":0,
            "GA":0
        },
        
    }
    matches = Match.query.all()
    for match in matches:
        # check if match has been played
        if(match.state == 1):
            # table[str(match.team)] = match

            # Check if team has won the match
            if(match.score[0] > match.score[2]):
                # Add win to home team
                table[str(match.team)]['won'] += 1
                # Add win point
                table[str(match.team)]['points']+=3
                # Add play count
                table[str(match.team)]['played'] += 1
                # Add GF to home team
                table[str(match.team)]['GF'] += int(match.score[0])
                # Add GA to home team
                table[str(match.team)]['GA'] += int(match.score[2])
                # Add to Last 5
                if len(table[str(match.team)]['last5']) < 5:
                    table[str(match.team)]['last5'].append("W")
                else:
                    table[str(match.team)]['last5'].pop(0)
                    table[str(match.team)]['last5'].append("W")
                
                
                # Add loss to away team
                table[str(match.opponent)]['lost'] += 1
                # Add play count
                table[str(match.opponent)]['played'] += 1
                # Add GF to away team
                table[str(match.opponent)]['GF'] += int(match.score[2])
                # Add GA to away team
                table[str(match.opponent)]['GA'] += int(match.score[0])
                # Add to Last 5
                if len(table[str(match.opponent)]['last5']) < 5:
                    table[str(match.opponent)]['last5'].append("L")
                else:
                    table[str(match.opponent)]['last5'].pop(0)
                    table[str(match.opponent)]['last5'].append("L")

            
            # Check if team has lost the match
            elif(match.score[0] < match.score[2]):
                # Add loss to home team
                table[str(match.team)]['lost'] += 1
                # Add play count
                table[str(match.team)]['played'] += 1
                # Add GF to home team
                table[str(match.team)]['GF'] += int(match.score[0])
                # Add GA to home team
                table[str(match.team)]['GA'] += int(match.score[2])
                # Add to Last 5
                if len(table[str(match.team)]['last5']) < 5:
                    table[str(match.team)]['last5'].append("L")
                else:
                    table[str(match.team)]['last5'].pop(0)
                    table[str(match.team)]['last5'].append("L")

                
                
                # Add win to away team
                table[str(match.opponent)]['won'] += 1
                # Add win point
                table[str(match.opponent)]['points'] += 3
                #Add play count
                table[str(match.opponent)]['played'] += 1
                 # Add GF to away team
                table[str(match.opponent)]['GF'] += int(match.score[2])
                # Add GA to away team
                table[str(match.opponent)]['GA'] += int(match.score[0])
                # Add to Last 5
                if len(table[str(match.opponent)]['last5']) < 5:
                    table[str(match.opponent)]['last5'].append("W")
                else:
                    table[str(match.opponent)]['last5'].pop(0)
                    table[str(match.opponent)]['last5'].append("W")


            #Check if team has drawn the match
            elif(match.score[0] == match.score[2]):
                # Add draw to home team
                table[str(match.team)]['drawn'] += 1
                # Add play count
                table[str(match.team)]['played'] += 1
                #Add draw point
                table[str(match.team)]['points'] +=1
                # Add GF to home team
                table[str(match.team)]['GF'] += int(match.score[0])
                # Add GA to home team
                table[str(match.team)]['GA'] += int(match.score[2])
                # Add to Last 5
                if len(table[str(match.team)]['last5']) < 5:
                    table[str(match.team)]['last5'].append("D")
                else:
                    table[str(match.team)]['last5'].pop(0)
                    table[str(match.team)]['last5'].append("D")

                
                # Add draw to away team
                table[str(match.opponent)]['drawn'] += 1
                # Add play count
                table[str(match.opponent)]['played'] += 1
                # Add draw point
                table[str(match.opponent)]['points'] +=1
                # Add GF to away team
                table[str(match.opponent)]['GF'] += int(match.score[2])
                # Add GA to away team
                table[str(match.opponent)]['GA'] += int(match.score[0])
                # Add to Last 5
                if len(table[str(match.opponent)]['last5']) < 5:
                    table[str(match.opponent)]['last5'].append("D")
                else:
                    table[str(match.opponent)]['last5'].pop(0)
                    table[str(match.opponent)]['last5'].append("D")
   
    ## print(table)
    return table
    
@api.route("/score/<player_id>/<gameweek_id>")
class Score(Resource):
    def get(self,player_id,gameweek_id):
        current_score = Scores.query.filter_by(players_id=player_id,gameweek_id=gameweek_id)
        current_score =  list(map(lambda p: p.serialize(), current_score))
        return current_score[0]


@api.route("/statistics")
class Stat(Resource):
    def get(self):
        most_goals = StatInfo.query.filter_by().order_by(StatInfo.goals_scored.desc()).limit(5)
        most_assists = StatInfo.query.filter_by().order_by(StatInfo.assists_provided.desc()).limit(5)
        most_red_cards = StatInfo.query.filter_by().order_by(StatInfo.red_cards.desc()).limit(5)
        most_yellow_cards = StatInfo.query.filter_by().order_by(StatInfo.yellow_cards.desc()).limit(5)
        most_clean_sheets = StatInfo.query.filter_by().order_by(StatInfo.clean_sheets.desc()).limit(5)
        most_goals =  list(map(lambda p: p.serialize(), most_goals))
        most_assists =  list(map(lambda p: p.serialize(), most_assists))
        most_red_cards =  list(map(lambda p: p.serialize(), most_red_cards))
        most_yellow_cards =  list(map(lambda p: p.serialize(), most_yellow_cards))
        most_clean_sheets =  list(map(lambda p: p.serialize(), most_clean_sheets))
        
        def get_player_info(player_id):
            current_player_info = Players.query.filter_by(id=player_id).first()
            current_team_id = current_player_info.dept_id
            current_player_name = current_player_info.fname + " " + current_player_info.lname
            current_team_name = Dept.query.filter_by(id=current_team_id).first().dName
            return {"team_id":current_team_id,"player_name":current_player_name,"team_name":current_team_name}
            
        all_data = {
            "goals_scored":[],
            "assists_provided":[],
            "yellow_cards":[],
            "red_cards":[],
            "clean_sheets":[],
        }
        def get_stat_data(type,data):
            all_goals_info = []
            for i in range(len(data)):
                extra_info = get_player_info(data[i]['id'])
                current_goal_info = {
                "player_id":data[i]['id'],
                "player_name":extra_info['player_name'],
                type:data[i][type],
                "team_name":extra_info['team_name']
                }
                
                all_goals_info.append(current_goal_info)
            all_data[type] = all_goals_info
            
            
                
        
                
                
                
        get_stat_data("goals_scored",most_goals)
        get_stat_data("assists_provided",most_goals)
        get_stat_data("yellow_cards",most_yellow_cards)
        get_stat_data("red_cards",most_red_cards)
        get_stat_data("clean_sheets",most_clean_sheets)
        
        
        return all_data , 200
        