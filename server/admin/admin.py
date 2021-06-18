# Importing Essentials
from operator import pos
import re
from flask import Blueprint, request,json,jsonify

#  Importing Restx
from flask_restx import Resource, Api

# Importing DB and JWT Instance from main
from main import db

#Creating Blueprint for Admin
admin_app = Blueprint("admin",__name__)
admin = Api(admin_app)

# Importing JWT Helpers
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

# Importing Models
from models.department import Dept
from models.event import Event
from models.gameweek import Gameweek
from models.matches import Match
from models.players import Players
from models.score import Scores
from models.statistics import StatInfo
from models.user_players import userPlayers

# ####################
# Endpoints for admin
######################
def check_admin():
    if(get_jwt_identity() == 1):
       return "Admin"
    else:
        "Non-Admin"
       
# Route to Handle Teams
@admin.route("/teams")
class Team(Resource):
    # Get All teams
    @jwt_required()
    def get(self):
        if(check_admin() == "Admin"):
            all_teams = Dept.query.all()
            all_teams =  list(map(lambda p: p.serialize(), all_teams))
            return all_teams , 200
        else:
            return {"message":"Forbidden Access"}, 403

# Route to Handle Schedule
@admin.route("/schedule/<id>")
class Schedule(Resource):
    # Get Schedule by GAMEWEEK ID
    @jwt_required()
    def get(self,id):
        if(check_admin() == "Admin"):
            schedule = Match.query.filter_by(game_week=id).order_by(Match.state.asc(),Match.time.asc())
            schedule =list(map(lambda p: p.serialize(), schedule))
            return schedule , 200
        else:
             return {"message":"Forbidden Access"}, 403
     
    # Update Schedule By GAMEWEEK ID  
    @jwt_required()
    def patch(self,id):
        if(check_admin() == "Admin"):
            response_data = request.get_json()['match_schedules']
            for match in response_data:
                current_match = Match.query.filter_by(id=match['id']).first()
                current_match.time = match['time']
                current_match.date = match['date']
                db.session.add(current_match)
                db.session.commit()
            
            return {"message":"Update Successful"} , 204
        else:
             return {"message":"Forbidden Access"}, 403

# Route to Generate Matches at start of season
@admin.route("/matches")
class GenerateMatch(Resource):
    @jwt_required()
    def get(self):
        if(check_admin()=="Admin"):
            if(not Match.query.first()):
            #GW1
                m1 =Match(team=4,opponent=5,game_week=1,time="16:00",date="2021-03-03",state=0,score="")
                m2 =Match(team=6,opponent=2,game_week=1,time="16:00",date="2021-03-03",state=0,score="")
                m3 =Match(team=1,opponent=3,game_week=1,time="16:00",date="2021-03-03",state=0,score="")

                #GW2
                m4 =Match(team=2,opponent=4,game_week=2,time="16:00",date="2021-10-03",state=0,score="")
                m5 =Match(team=1,opponent=5,game_week=2,time="16:00",date="2021-10-03",state=0,score="")
                m6 =Match(team=6,opponent=3,game_week=2,time="16:00",date="2021-10-03",state=0,score="")

                #GW3
                m7 =Match(team=4,opponent=1,game_week=3,time="16:00",date="2021-17-03",state=0,score="")
                m8 =Match(team=2,opponent=3,game_week=3,time="16:00",date="2021-17-03",state=0,score="")
                m9 =Match(team=5,opponent=6,game_week=3,time="16:00",date="2021-17-03",state=0,score="")

                #GW4
                m10=Match(team=3,opponent=4,game_week=4,time="16:00",date="2021-24-03",state=0,score="")
                m11=Match(team=6,opponent=1,game_week=4,time="16:00",date="2021-24-03",state=0,score="")
                m12=Match(team=5,opponent=2,game_week=4,time="16:00",date="2021-24-03",state=0,score="")

                #GW5
                m13 =Match(team=4,opponent=6,game_week=5,time="16:00",date="2021-31-03",state=0,score="")
                m14 =Match(team=3,opponent=5,game_week=5,time="16:00",date="2021-31-03",state=0,score="")
                m15 =Match(team=1,opponent=2,game_week=5,time="16:00",date="2021-31-03",state=0,score="")
                            
                db.session.add_all([m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,m13,m14,m15])
                db.session.commit()
                return {"message":"Match Generated Successfully"}, 200
            else:
                return {"message":"Forbidden Access"}, 403
# Route to Handle Players   
@admin.route("/players/<id>")      
class Player(Resource):
    # Get Players by Department ID
    @jwt_required()
    def get(self,id):
        if(check_admin() == "Admin"):
            curr_players = Players.query.filter_by(dept_id=id).all()
            curr_players = list(map(lambda p: p.serialize(), curr_players))
        
            return {"response_data":curr_players} , 200
        else:
            return {"message":"Forbidden Access"}, 403
    
    # Update Player Info
    @jwt_required()
    def patch(self,id):
        if(check_admin() == "Admin"):
            response_data = request.get_json()['updated_player_data']
            current_player = Players.query.filter_by(id=id).all()
            current_player[0].fname = response_data['fname']
            current_player[0].lname = response_data['lname']
            current_player[0].position = response_data['position']
            db.session.commit()
            current_player =  list(map(lambda p: p.serialize(), current_player))
            return {"message":"Update Successful"} , 204
        
        else:
            return {"message":"Forbidden Access"}, 403
        
        
    # Add New Player
    @jwt_required()
    def post(self,id):
        if(check_admin() == "Admin"):
            response_data = request.get_json()['new_player']
            check_player = Players.query.filter_by(fname=response_data['fname'],lname=response_data['lname']).first()
            # If Duplicate Data
            if(check_player):
                return {"message":"Player '{} {}' Exsists".format(check_player.fname,check_player.lname)} , 409
            
            new_player = Players(fname=response_data['fname'],lname=response_data['lname'],position=response_data['position'],dept_id=response_data['team'])
            db.session.add(new_player)
            db.session.commit()
        
            return {"message":"Player '{} {}' added Successfully".format(new_player.fname,new_player.lname)} , 201

        else:
            return {"message":"Forbidden Access"}, 403
        

    # Delete Player
    @jwt_required()
    def delete(self,id):
        if(check_admin() == "Admin"):
    
            # Players.query.filter_by(id=id).delete()
            # db.session.commit()
            return {"message":"Player Successfully Deleted"} , 204
        else:
            return {"message":"Forbidden Access"}, 403
     
# Route to Handle Events   
@admin.route("/events/<id>")       
class Events(Resource):
    # Get Player Info From Event Table
    @jwt_required()
    def get(self,id):
        if(check_admin() == "Admin"):
            curr_data = Event.query.filter_by(players_id=id).all()
            curr_data =  list(map(lambda p: p.serialize(), curr_data))
            return {"response_data":curr_data} , 200
        else:
            return {"message":"Forbidden Access"}, 403
        
    # Update Player info on Events Table
    @jwt_required()
    def patch(self,id):
        if(check_admin() == "Admin"):
            response_data = request.get_json()['updated_stats']            
            curr_match = Event.query.filter_by(gameweek_id=id,players_id=response_data['player_id']).first()
            if curr_match:
                curr_match.goals_scored = response_data['goals_scored'],
                curr_match.goals_conceded=response_data['goals_conceded'],
                curr_match.assists_provided=response_data['assists_provided'], 
                curr_match.minutes_played=response_data['minutes_played'], 
                curr_match.yellow_cards=response_data['yellow_cards'],  
                curr_match.red_cards=response_data['red_cards'], 
                db.session.commit()
            else:
                new_match = Event(players_id=response_data['player_id'],match_id=1,gameweek_id=id,goals_scored=response_data['goals_scored'],goals_conceded=response_data['goals_conceded'],
                                  assists_provided=response_data['assists_provided'],minutes_played=response_data['minutes_played'], 
                                  yellow_cards=response_data['yellow_cards'], red_cards=response_data['red_cards'])
                db.session.add(new_match)
                db.session.commit()
     
# Route Get Active
@admin.route("/activegameweek")
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

# Route to Handle Scores 
@admin.route("/score/<gameweek_id>")
class Score(Resource):
    def post(self,gameweek_id):
        curr_data = request.get_json()['update_info']
        player_id = curr_data['player_id']
        gameweek_id = curr_data['gameweek_id']
       
        
        score_db = Scores.query.filter_by(players_id=player_id,gameweek_id=gameweek_id).first()
        player_position = Players.query.filter_by(id=player_id).first().position
        # If Score already Exists
        if score_db:
            final_score = calculate_score(player_position,curr_data['goals_scored'],curr_data['goals_conceded'],curr_data['assists_provided'],curr_data['minutes_played'],curr_data['yellow_cards'],curr_data['red_cards'],score_db.score)
            score_db.score = final_score
            db.session.commit()
            
        # If new Score
        else:
            final_score = calculate_score(player_position,curr_data['goals_scored'],curr_data['goals_conceded'],curr_data['assists_provided'],curr_data['minutes_played'],curr_data['yellow_cards'],curr_data['red_cards'])
            new_score = Scores(players_id=player_id,match_id=1,gameweek_id=gameweek_id,score=final_score)
            db.session.add(new_score)
            db.session.commit()
            

# Helper To Calculate Scores   
def calculate_score(player_position,goals_scored,goals_conceded,assists_provided,minutes_played,yellow_cards,red_cards,score=0):
    # Non Variables
    goals_conceded = int(goals_conceded)
    goals_scored = int(goals_scored)
    assists_provided = int(assists_provided)
    minutes_played = int(minutes_played)
    yellow_cards = int(yellow_cards)
    red_cards = int(red_cards)

    score = int(score)
    # Yellow and Red Cards
    if(yellow_cards==1):
        score = score - 1
    if(red_cards == 1):
        score = score - 3
    if(minutes_played >= 45 and minutes_played > 0):
        score = score + 1
    if(minutes_played > 45):
         score = score + 1
    
    if(assists_provided > 0):
        if(player_position == "goalkeeper"):
            score = score + (5 * assists_provided)
        elif player_position == "defender":
             score = score + (4 * assists_provided)
        elif player_position == "midfielder":
            score = score + (3 * assists_provided)
        else:
            score = score + (3 * assists_provided)
    
    if(goals_scored > 0):
        if(player_position == "goalkeeper"):
            score = score + (6 * goals_scored)
        elif player_position == "defender":
             score = score + (5 * goals_scored)
        elif player_position == "midfielder":
            score = score + (4 * goals_scored)
        else:
            score = score + (3 * goals_scored)
            
    if(goals_conceded > 0):
        if(player_position == "goalkeeper"):
            score = score - (3 * goals_conceded)
        elif player_position == "defender":
             score = score - (3 * goals_conceded)
        elif player_position == "midfielder":
            score = score - (2 * goals_conceded)
        else:
            score = score - (1 * goals_conceded)
            
    return score
            
# Set Zero to all scores               
@admin.route("/reset")
class Reset(Resource):
    @jwt_required()
    def delete(self):
        if(check_admin()=="Admin"):
          
            # Delete Stats
            db.session.query(StatInfo).delete()
            db.session.commit()
            
            # Delete Scores  
            db.session.query(Scores).delete()
            db.session.commit()    
            
            # Delete User Players   
            db.session.query(userPlayers).delete()
            db.session.commit()
            
            # Delete Events
            db.session.query(Event).delete()
            db.session.commit()
            
            # Delete Matches
            db.session.query(Match).delete()
            db.session.commit()
            
            # Delete Gameweek
            db.session.query(Gameweek).delete()
            db.session.commit()
            
            
            return {"message":"Reset Successfully"} , 204
        else:
            return {"message":"Unauthorized Access"} , 403
        
# End and Start Gameweek
@admin.route("/gameweek")
class gameweeks(Resource):
    # Activate gameweek
    def put(self):
        # Active a gameweek
        upcoming_gw = Gameweek.query.filter_by(status="ALL_UPCOMING").first()
        upcoming_gw.status = "ACTIVE"
        db.session.add(upcoming_gw)
        db.session.commit()
        
           
    #    ENDS ACTIVE GW
    def patch(self):
        active_gw = Gameweek.query.filter_by(status="ACTIVE").first()
        active_gw.status = "PAST"
        db.session.add(active_gw)
        db.session.commit()
       
        ## Add score to match
        gw = Gameweek.query.filter_by(status="ALL_UPCOMING").first()
        gw = gw.id - 1
        matches = Match.query.filter_by(game_week=gw).all()
        # Loop every match in GW
        for match in matches:
            homeScore = 0
            awayScore = 0
            
            # Get players of team
            homeTeamPlayers = Players.query.filter_by(dept_id=match.team).all()
            awayTeamPlayers = Players.query.filter_by(dept_id=match.opponent).all()

            # Loop every player of home team
            for player in homeTeamPlayers:
                # Get goals for player
                goals = Event.query.filter_by(players_id=player.id).first()
                # Add goal to home team
                homeScore += goals.goals_scored

            # Loop every player of away team
            for player in awayTeamPlayers:
                # Get goals for player
                goals = Event.query.filter_by(players_id=player.id).first()
                # Add goal to away team
                awayScore += goals.goals_scored

            score = str(homeScore) + "v" + str(awayScore)
            match.state = 1
            match.score = score
            db.session.add(match)
            db.session.commit()

            
            
        # Add score

            
            
        # # If Active Gameweek 
        # upcoming_gameweek = Gameweek.query.filter_by(status="ALL_UPCOMING").first()
        # upcoming_gameweek.status = "ACTIVE"
        # db.session.add(upcoming_gameweek)
        # db.session.commit()

@admin.route("/statistics/<int:player_id>")
class statUpdate(Resource):
    def put(self,player_id):
        request_stat = request.get_json()['update_info']
        stat = StatInfo.query.filter_by(players_id=player_id).first()
       
        if(stat):
            stat.goals_scored=stat.goals_scored + int(request_stat['goals_scored'])
            stat.assists_provided = stat.assists_provided + int(request_stat['assists_provided'])
            if(int(request_stat['goals_conceded']) == 0):
                stat.clean_sheets= stat.clean_sheets + 1
            if(int(request_stat['yellow_cards'])==1):
           
                stat.yellow_cards= stat.yellow_cards + 1
            if(int(request_stat['red_cards']) == 1):
                stat.red_cards= stat.red_cards + 1
            db.session.add(stat)
            db.session.commit()
        else:
            clean_sheets_current=0
            yellow_card_current=0
            red_card_current=0

            if(int(request_stat['goals_conceded']) == 0):
                clean_sheets_current=1
            if(int(request_stat['yellow_cards'])==1):
                yellow_card_current=1
            if(int(request_stat['yellow_cards'])==1):
                red_card_current=1
            
            stat_new = StatInfo(players_id=player_id, goals_scored=request_stat['goals_scored'],clean_sheets=clean_sheets_current,assists_provided=request_stat['assists_provided'], yellow_cards=yellow_card_current, red_cards=red_card_current)
            db.session.add(stat_new)
            db.session.commit()
        print('Completed!')