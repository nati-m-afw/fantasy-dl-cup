# Importing
from flask import Blueprint, request,json,jsonify
from flask.globals import session
from flask_restx import Resource, Api
# from flask_restplus import Resource, Api
from models.matches import Match
from models.players import Players
from models.event import Event
from models.department import Dept
from models.score import Scores
from flask_cors import cross_origin
from main import db,jwt




#Creating Blueprint for Admin
admin_app = Blueprint("admin",__name__)
admin = Api(admin_app)

jwt._set_error_handler_callbacks(admin)

# Importing JWT Helpers
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

# ####################
# Endpoints for admin
######################
def check_admin():
    if(get_jwt_identity() == 5):
       return "Admin"
    else:
        "Non-Admin"
       
@admin.route("/teams")
class Team(Resource):
    # Get All teams
    @jwt_required()
    def get(self):
        if(check_admin() == "Admin"):
            all_teams = Dept.query.all()
            all_teams =  list(map(lambda p: p.serialize(), all_teams))
            return {"response_data":all_teams} , 200
        else:
            return {"message":"Forbidden Access"}, 403

@admin.route("/schedule/<id>")
class Schedule(Resource):
    # Get Schedule by GAMEWEEK ID
    @jwt_required()
    def get(self,id):
        if(check_admin() == "Admin"):
            schedule = Match.query.filter_by(game_week=id).order_by(Match.state.asc(),Match.time.asc())
            schedule =list(map(lambda p: p.serialize(), schedule))
            return {"response_data":schedule} , 200
        else:
             return {"message":"Forbidden Access"}, 403
     
    # Update Schedule By GAMEWEEK ID  
    @jwt_required()
    def patch(self,id):
        if(check_admin() == "Admin"):
            response_data = request.get_json()['match_schedules']
            for item in response_data:       
                curr_match = Match.query.filter_by(id=id).first()
                curr_match.time = item['time']
                curr_match.date = item['date']
                db.session.commit()
            return {"message":"Update Successful"} , 204
        else:
             return {"message":"Forbidden Access"}, 403

    #  Generate Match Schedule
      
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
            print(current_player)
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
            print("Invoked for",id)  
            # Players.query.filter_by(id=id).delete()
            # db.session.commit()
            return {"message":"Player Successfully Deleted"} , 204
        else:
            return {"message":"Forbidden Access"}, 403
               
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
            curr_match.goals_scored = response_data['goals_scored'],
            curr_match.goals_conceded=response_data['goals_conceded'],
            curr_match.assists_provided=response_data['assists_provided'], 
            curr_match.minutes_played=response_data['minutes_played'], 
            curr_match.yellow_cards=response_data['yellow_cards'],  
            curr_match.red_cards=response_data['red_cards'], 
            db.session.commit()
        
            return {"message":"Update Successful"} , 204
        else:
            return {"message":"Forbidden Access"}, 403
        
         
@admin.route("/score")
class Score(Resource):
    def get(self):
        scores= []
        all_player_events = []
        all_players = db.session.query(Players.id).all()
        for player in all_players:
            current_event = Event.query.filter_by(players_id=player[0]).all()
            current_event =  list(map(lambda p: p.serialize(), current_event))
            if len(current_event) == 0:
                continue
            all_player_events.append(current_event)
        
        
        for event in all_player_events:
            # Event Info
            player_id = event[0]['player_id']
            match_id = event[0]['match_id']
            gameweek_id = event[0]['gameweek_id']
            score = 0
            # Get Player Position
            curr_player = Players.query.filter_by(id=event[0]['id']).first()
            position = curr_player.position
            # Get Events
            goal_scored = event[0]['goals_scored']
            goals_assisted = event[0]['assists_provided']
            goals_conceded = event[0]['goals_conceded']
            yellow_cards = event[0]['yellow_cards']
            red_cards = event[0]['red_cards']
            minutes_played = event[0]['minutes_played']
            
            

            # Handle Minutes Played
            if(minutes_played >= 45):
                # print("Here")
                score = score + 2
            elif(minutes_played <45):
                score = score + 1
            
            # Handle Yellow Cards
            if(yellow_cards == 1):
                score = score - 1
                
            # Red card
            if(red_cards == 1):
                score = score - 3
                
            # Handle Goals
            if(position == "goalkeeper"):
                score = score + (goal_scored * 6)
            elif(position == "defender"):
                score = score + (goal_scored * 5)
            elif (position == " midfielder"):
                score = score + (goal_scored * 4)
            elif (position == "striker"):
                score = score + (goal_scored * 3)
                
            # Handle Assists
            if (position == "goalkeeper"):
                score = score + (goals_assisted * 5)
            elif (position == "defender"):
                score = score + (goals_assisted * 4)
            elif (position == "midfielder" or position=='striker'):
                score = score + (goals_assisted * 3)
                
            # Handle Goals Conceded
            if(position == "goalkeeper"):
                if goals_conceded == 0:
                    score = score + 3
                else:
                    score = score - goals_conceded
        
            elif(position == "defender"):
                if goals_conceded == 0:
                    score = score + 3
                else:
                    score = score - goals_conceded
        
            elif(position == "midfielder"):
                if goals_conceded == 0:
                    score = score + 3
                else:
                    score = score - goals_conceded
        
            print("Insertion")            
            curr_score = Scores(players_id=player_id,gameweek_id=gameweek_id,match_id=match_id,score=score)
            db.session.add(curr_score)
            db.session.commit()
            scores.append(curr_score)
           
            
        return all_players , 200
    
    
@admin.route("/score/<player_id>")
class Score(Resource):
    def post(self,player_id):
        game_week = request.get_json()['event_info']['game_week']
    
        any_score = Scores.query.filter_by(players_id=player_id,gameweek_id=game_week).first()
        if(any_score):
            current_player_score = Scores.query.filter_by(players_id=player_id,gameweek_id=game_week).first()
            current_player_score.score = 500
            db.session.add(current_player_score)
            db.session.commit()
            print("Updated")
        else:
            
            all_players = Players.query.filter_by().all()
            print(all_players)
            for player in all_players:
                current_event = Scores(players_id=player.id,match_id=1,gameweek_id=game_week,score=0)
                db.session.add(current_event)
                db.session.commit()
            print("Done")



# Set Zero to all scores
# Update on Player ID
