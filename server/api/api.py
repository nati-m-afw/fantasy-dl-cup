# Importing Essentials
from flask import Blueprint, request, jsonify

# Importing DB and JWT Instance
from main import db,jwt

# Importing Flask Restx
from flask_restx import Resource , Api

# Importing JWT Helpers
from flask_jwt_extended import jwt_required


# Importing DB Models
from models.users import Users
from models.user_players import userPlayers
from models.department import Dept
from models.gameweek import Gameweek
from models.matches import Match
from models.score import Scores
from models.players import Players
from models.statistics import StatInfo

#Creating Blueprint for api
api_app = Blueprint("api",__name__)
api = Api(api_app)


# Helper Function
# Add status to player data in get_team response
def addDNameToResponse(player, department):
    result = player
    result.update( {'department': department} )
    return result

# Route to Get Players by Position
@api.route('/getplayers/<pos>')
class GetPlayers(Resource):
    @jwt_required()
    def get(self,pos):
        response = { 'status': 'success'}
        player =  db.session.query(Players, Dept.dName).filter_by(position = pos).join(Dept).all()
        response['players'] = list(map(lambda p: addDNameToResponse(p[0].serialize(), p[1]), player))
    
        return response , 200
    
# Get users team
# Add GAMEWEEK parameter
#JWT MISSING
@api.route('/getteam/<userId>/<gameweekId>')
class GetTeam(Resource):
    # @jwt_required()
    def get(self,userId,gameweekId):
        # response = { 'status': 'success' }
        # team = (db.session.query(userPlayers, Players, Users, Dept, Gameweek).with_entities(Players, userPlayers.status, Dept.dName)
        # .join(Users)
        # # .join(userPlayers)
        # .join(Players)
        # .join(Dept)
        # .join(Gameweek)
        # .filter(Users.id==userId, Gameweek.id==gameweekId)).all()
        
        # response['team'] = list(map(lambda p: addStatusToResponse(p[0].serialize(), p[1], p[2]), team))
        # response['gameweekId'] = gameweekId
        # Get Active gameweek
        
        # Alternative Code to fetch Team
        active_gameweek_id = 0
        active_gameweek = Gameweek.query.filter_by(status='ACTIVE').first()
        if(active_gameweek):
            active_gameweek_id = active_gameweek.id
        team = []
        response = { 'status': 'success',"gameweekId":active_gameweek_id}
        selected_players = userPlayers.query.filter_by(user_id=userId,gameweek_id=gameweekId)
        selected_players =  list(map(lambda p: p.serialize(), selected_players))
        for player in selected_players:
            # Get Players Info
            current_player = Players.query.filter_by(id=player['players_id']).first()
            # current_player =  list(map(lambda p: p.serialize(), current_player))
            current_dept = Dept.query.filter_by(id=current_player.dept_id).first()
            # current_dept =  list(map(lambda p: p.serialize(), current_dept))
            current_info = {
                "department":current_dept.dName,
                "dept_id":current_dept.id,
                "fname":current_player.fname,
                "lname":current_player.lname,
                "position":current_player.position,
                "id":current_player.id,
                "status":player['status']          
            }
            team.append(current_info)
        response['team'] = team
         # Alternative Code to fetch Team
        
        
        return response , 200


# Get Active Gameweek
@api.route('/getactivegw')
class ActiveGameweek(Resource):
    @jwt_required()
    def get(self):
        response = { 'status': 'success' }
        gw = Gameweek.query.filter_by(status='ACTIVE').first()
        #  If gameweek active exists
        if gw is not None:
            response['activeGW'] = gw.id
        # If GW active does not exists
        else:
            gw = Gameweek.query.filter_by(status='PAST').first()
            # If Past GW Exists
            if gw is not None:
                response['activeGW'] = gw.id
            # If Past GW does not Exist
            else:
                response['activeGW'] = 0
        return response , 200

# Route to update user_players table
@api.route('/updateuserplayers', methods=['POST'])
class UpdateUserPlayers(Resource):
    @jwt_required()
    def post(self):
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
            return {"message":"Success"}, 201

# Helper Function
# Add status to player data in get_team response
def addStatusToResponse(player, status, department):
    result = player
    result.update( {'status': status } )
    result.update( {'department': department} )
    return result

#get table route
@api.route('/gettable')
class Table(Resource):
    @jwt_required()
    def get(self):
        response={'status':'success'}
        table = {
            "1":{
                "teamName": "BioMed",
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
            "2":{
                "teamName": "Chemical",
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
                "teamName": "Elec",
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
                "teamName": "IT",
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
            "5": {
                "teamName": "Mech",
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
                "teamName": "SE",
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
        try:
            return current_score[0]
        except:
            return 0

@api.route("/statistics")
class Stat(Resource):
    @jwt_required()
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

        # print(most_goals[0]['player_id'])
        # current_player = Players.query.filter_by(id=most_goals[0]['player_id']).first()
        # current_stat = StatInfo.query.filter_by(players_id= most_goals[0]['player_id']).first()
        goals_scored = []
        assists_provided = []
        yellow_cards = []
        red_cards = []
        clean_sheets = []


        def get_goals(player_id):
            current_player = Players.query.filter_by(id=player_id).first()
            current_stat = StatInfo.query.filter_by(players_id= player_id).first()
            current_team = Dept.query.filter_by(id=current_player.dept_id).first()
            current_info = {
                "player_name":current_player.fname,
                "player_id":player_id,
                "goals_scored":current_stat.goals_scored,
                "team_name":current_team.dName,
                "position":current_player.position
            }
            goals_scored.append(current_info)

        def get_assist(player_id):
            current_player = Players.query.filter_by(id=player_id).first()
            current_stat = StatInfo.query.filter_by(players_id= player_id).first()
            current_team = Dept.query.filter_by(id=current_player.dept_id).first()
            current_info = {
                "player_name":current_player.fname,

                "player_id":player_id,
                "assists_provided":current_stat.assists_provided,
                "team_name":current_team.dName,
                "position":current_player.position
            }
            assists_provided.append(current_info)
            
        def goals_conceded(player_id):
            current_player = Players.query.filter_by(id=player_id).first()
            current_stat = StatInfo.query.filter_by(players_id= player_id).first()
            current_team = Dept.query.filter_by(id=current_player.dept_id).first()
            current_info = {
                "player_name":current_player.fname,

                "player_id":player_id,
                "clean_sheets":current_stat.clean_sheets,
                "team_name":current_team.dName,
                "position":current_player.position
            }
            clean_sheets.append(current_info)
            
        def yellow_card(player_id):
            current_player = Players.query.filter_by(id=player_id).first()
            current_stat = StatInfo.query.filter_by(players_id= player_id).first()
            current_team = Dept.query.filter_by(id=current_player.dept_id).first()
            current_info = {
                "player_name":current_player.fname,

                "player_id":player_id,
                "yellow_cards":current_stat.yellow_cards,
                "team_name":current_team.dName,
                "position":current_player.position
            }
            yellow_cards.append(current_info)
            
        def red_card(player_id):
            current_player = Players.query.filter_by(id=player_id).first()
            current_stat = StatInfo.query.filter_by(players_id= player_id).first()
            current_team = Dept.query.filter_by(id=current_player.dept_id).first()
            current_info = {
                "player_name":current_player.fname,

                "player_id":player_id,
                "red_cards":current_stat.red_cards,
                "team_name":current_team.dName,
                "position":current_player.position
            }
            red_cards.append(current_info)

        for i in most_goals:
             get_goals(i['player_id'])
        for i in most_assists:
             get_assist(i['player_id'])   
        for i in most_clean_sheets:
             goals_conceded(i['player_id']) 
        for i in most_red_cards:
             red_card(i['player_id']) 
        for i in most_yellow_cards:
             yellow_card(i['player_id']) 
        
            
        # get_goals(most_goals[0]['player_id'])
        # get_assist(most_assists[0]['player_id'])
        # goals_conceded(most_clean_sheets[0]['player_id'])
        # print(current_player.fname)
        # print(current_stat.goals_scored)
        # print(most_goals[2].players_id)
        # print(most_goals[3].players_id)
        # print(most_goals[4].players_id)
        # print(most_goals[5].players_id)
        

        # def get_player_info(player_id):
        #     current_player_info = Players.query.filter_by(id=player_id).first()
        #     current_team_id = current_player_info.dept_id
        #     current_player_name = current_player_info.fname + " " + current_player_info.lname
        #     current_team_name = Dept.query.filter_by(id=current_team_id).first().dName
        #     print(current_player_named)
        #     return {"team_id":current_team_id,"player_name":current_player_name,"team_name":current_team_name}
        
        all_data = {
            "goals_scored":goals_scored,
            "assists_provided":assists_provided,
            "yellow_cards":yellow_cards,
            "red_cards":red_cards,
            "clean_sheets":clean_sheets,
        }
        print(all_data)
        # def get_stat_data(type,data):
        #     all_goals_info = []
        #     for i in range(len(data)):
        #         extra_info = get_player_info(data[i]['id'])
        #         current_goal_info = {
        #         "player_id":data[i]['id'],
        #         "player_name":extra_info['player_name'],
        #         type:data[i][type],
        #         "team_name":extra_info['team_name']
        #         }
                
            #     all_goals_info.append(current_goal_info)
            # all_data[type] = all_goals_info
            
            
                
        
                
                
                
        # get_stat_data("goals_scored",most_goals)
        # get_stat_data("assists_provided",most_goals)
        # get_stat_data("yellow_cards",most_yellow_cards)
        # get_stat_data("red_cards",most_red_cards)
        # get_stat_data("clean_sheets",most_clean_sheets)
        
        
        return all_data , 200
        

@api.route("/globalleague")
class GlobalLeague(Resource):

    def get(self):
        response = { 'status': 'success' }
        teams = {}

        activeGW = 0

        gw = Gameweek.query.filter_by(status='ACTIVE').first()

        if gw is not None :
            activeGW = gw.id
        else:
            gw = Gameweek.query.filter_by(status='PAST').first()
            if gw is not None:
                activeGW = gw.id


        # Get all user_players
        users = db.session.query(Users).all()
        user_players =  db.session.query(userPlayers).filter(userPlayers.gameweek_id < activeGW + 1).all()
        
        # Create data structure containing all users
        for user in users:
            teams[user.id] = {
                'id': user.id,
                'teamName': user.teamname,
                'score': [0,0,0,0,0]
            }
            # team.push(userScore)

        # Iterate over every row in user_players
        # Store score in data structure if player status is active
        for player in user_players:
            playerScore = Scores.query.filter_by(players_id=player.players_id,gameweek_id=player.gameweek_id).first()
            # print(playerScore)
            # print("UID", player.user_id, "GW", player.gameweek_id, "STATUS", player.status)
             
            try:
                if player.status == 'active':
                    teams[player.user_id]['score'][player.gameweek_id - 1] += playerScore.score
            except:
                teams[player.user_id]['score'][player.gameweek_id - 1] += 0

        response['teams'] = teams
        return response



# Route to get match schedule of a gameweek
@api.route("/schedule/<id>")
class Schedule(Resource):
    # Get Schedule by GAMEWEEK ID
    @jwt_required()
    def get(self,id):
        schedule = Match.query.filter_by(game_week=id).order_by(Match.state.asc(),Match.time.asc())
        schedule =list(map(lambda p: p.serialize(), schedule))
        return {"response_data":schedule} , 200



# Route to get teams info
@api.route("/teams")
class Team(Resource):
    # Get All teams
    @jwt_required()
    def get(self):
        all_teams = Dept.query.all()
        all_teams =  list(map(lambda p: p.serialize(), all_teams))
        return all_teams , 200
    
    
@api.route("/stat/<player_id>")
class PlayerStat(Resource):
    def get(self,player_id):
        score_info = Scores.query.filter_by(players_id=player_id).first()
        player_stats = StatInfo.query.filter_by(players_id=player_id).first()
        player_info = {
            "total_points":score_info.score,
            "total_goals":player_stats.goals_scored,
            "total_assists":player_stats.assists_provided,
            "clean_sheets":player_stats.clean_sheets,
            "yellow_cards":player_stats.yellow_cards,
            "red_cards":player_stats.red_cards,
        }
        return player_info