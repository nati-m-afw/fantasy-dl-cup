# Importing
from flask import Blueprint, request,json
from flask_restful import Resource, Api
from models.matches import Match
from models.players import Players
from models.event import Event
from models.department import Dept
from flask_cors import cross_origin
from main import db

#Creating Blueprint for Admin
admin_app = Blueprint("admin",__name__)
admin = Api(admin_app)


# ####################
# Endpoints for admin
######################


#Endpoint to create match_schedule
@admin_app.route("/schedule/generate")
def generate_schedule():
    teams = [1,2,3,4,5,6]
    fix = []
    i = 0
    while i < len(teams):
        j = i + 1
        k = i + 1
        while j < len(teams):
            if(i == j):
                j = j + 1
                continue
            else:
                fix_curr = (teams[i],teams[j],k)
                fix.append(fix_curr)
                k = k +1
                j = j + 1
        
        i = i + 1
        
    # for item in fix:
    #     # new_fix = Match(team=item[0],opponent=item[1],game_week=item[2],time="16:00",date="2021-03-23",state=0,score="")
    #     # db.session.add(new_fix)
    #     # db.session.commit()
    #     print(item)
    return ""

# Endpoint to get matches
@admin_app.route("/schedule/<id>",methods=["GET","POST"])
def get_schedule(id):
        if request.method == "GET":
            schedule = Match.query.filter_by(game_week=id).order_by(Match.state.asc(),Match.time.asc())
            schedule =list(map(lambda p: p.serialize(), schedule))
            # print(schedule)
            return json.dumps(schedule)
  
# Endpoint to save updated match_info   
@admin_app.route("/schedule/update",methods=["POST","GET"])
def update_schedule():
    response_data = request.get_json()['match_schedules']
    # db_match_info = Match.query
    for item in response_data:       
       curr_match = Match.query.filter_by(id=item['id']).first()
       curr_match.time = item['time']
       curr_match.date = item['date']
       db.session.commit()
    return ""


@admin_app.route("/players/<dept_id>")
def get_players_by_dept(dept_id):
    curr_players = Players.query.filter_by(dept_id=dept_id).all()
    curr_players = list(map(lambda p: p.serialize(), curr_players))
    
    return json.dumps(curr_players)
    

@admin_app.route("/event/player/<player_id>")
def get_player_stat(player_id):
    curr_data = Event.query.filter_by(players_id=player_id).all()
    curr_data =  list(map(lambda p: p.serialize(), curr_data))
    return json.dumps(curr_data)

@admin_app.route("/event/matches/<gameweek_id>",methods=["POST","GET"])
def update_match_stats(gameweek_id):
    if request.method == "POST":
       
        response_data = request.get_json()['updated_stats']
        curr_match = Event.query.filter_by(gameweek_id=gameweek_id,players_id=response_data['player_id']).first()
        curr_match.goals_scored = response_data['goals_scored'],
        curr_match.goals_conceded=response_data['goals_conceded'],
        curr_match.assists_provided=response_data['assists_provided'], 
        curr_match.minutes_played=response_data['minutes_played'], 
        curr_match.yellow_cards=response_data['yellow_cards'],  
        curr_match.red_cards=response_data['red_cards'], 
        # curr_match =  list(map(lambda p: p.serialize(), curr_match))
        #  print(curr_match['goals_scored'],
        #  curr_match['goals_conceded'],
        #  curr_match['assists_provided'], 
        #  curr_match['minutes_played'], 
        #  curr_match['yellow_cards'],  
        #  curr_match['red_cards'])
        db.session.commit()
       
        return json.dumps("Done")
        
    

    
    
# # End point to get all teams from dept table
@admin_app.route("/teams")
def get_all_teams():
    all_teams = Dept.query.all()
    all_teams =  list(map(lambda p: p.serialize(), all_teams))
    return json.dumps(all_teams)
    # return "Here"
    
# End point to update player info
@admin_app.route("/player/update",methods=["POST"])
def update_player():
    if request.method == "POST":
        response_data = request.get_json()['updated_player_data']
        current_player = Players.query.filter_by(id=response_data['id']).all()
        current_player[0].fname = response_data['fname']
        current_player[0].lname = response_data['lname']
        current_player[0].position = response_data['position']
        db.session.commit()
        current_player =  list(map(lambda p: p.serialize(), current_player))
        print(current_player)
        return "Done"
    
#end point to add new Player
#end point to add new Player
class AddNewPlayer(Resource):
    def post(self):
        response_data = request.get_json()['new_player']
        check_player = Players.query.filter_by(fname=response_data['fname'],lname=response_data['lname']).first()
        # If Duplicate Data
        if(check_player):
            return {"message":"Player '{} {}' Exsists".format(check_player.fname,check_player.lname)} , 209
        
      
        new_player = Players(fname=response_data['fname'],lname=response_data['lname'],position=response_data['position'],dept_id=response_data['team'])
        db.session.add(new_player)
        db.session.commit()
       
        return {"message":"Player '{} {}' added Successfully".format(new_player.fname,new_player.lname)}
     
class RemovePlayer(Resource):
    def delete(self,id):
        Players.query.filter_by(id=id).delete()
        db.session.commit()
        
        print("Invoked for",id)  
        return {"message":"Player Successfully Deleted"} , 204
        
        
admin.add_resource(AddNewPlayer,"/player/new")
admin.add_resource(RemovePlayer,"/player/delete/<id>")
    
    