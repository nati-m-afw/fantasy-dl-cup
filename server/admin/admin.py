# Importing
from flask import Blueprint, request, jsonify,json
from models.matches import Match
from models.players import Players
from flask_cors import cross_origin
from main import db

#Creating Blueprint for Admin
admin_app = Blueprint("admin",__name__)


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
        
    for item in fix:
        # new_fix = Match(team=item[0],opponent=item[1],game_week=item[2],time="16:00",date="2021-03-23",state=0,score="")
        # db.session.add(new_fix)
        # db.session.commit()
        print(item)
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
    

    