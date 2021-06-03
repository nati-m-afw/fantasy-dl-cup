# Importing
from flask import Blueprint,request,json
from main import db
from models.users import Users


# Creating a Blueprint
auth_app = Blueprint("auth",__name__)

# Registering Routes

#Route to add user to database
@auth_app.route("/signuser",methods=['POST'])
def register_user():
    # if request.method == 'POST':
       try:
            response_object = {'status':'success'}
            post_data = request.get_json()['user_info']
            lname = " "
            firebase_id =post_data['firebase_id']
            fname=post_data['fname']
            team_name=post_data['team_name']
            if(post_data['lname']):
                lname = post_data['lname']
            # print(firebase_id,fname,lname,team_name);
            new_user = Users(firebase_id=firebase_id,fname=fname,lname=lname,teamname=team_name);
            db.session.add(new_user)
            db.session.commit()
        
            # *****************
            print("USER ADDED")
          
            # *****************
           
            return json.dumps(response_object)
       except:
          print("ERRORRRR")
          return json.dumps({})
   
   
   
# Route to get User ID
@auth_app.route("/getUserID/<firebase_id>",methods=['GET','POST'])
def get_user_id(firebase_id):
    
    # ******************
    print("GET USER ID")
    # ******************
    
    user = Users.query.filter_by(firebase_id=firebase_id).first()
    if(user):
        response_object = {
            "code": "Success",
            "id": user.id,
            "team_name": user.teamname
        }
        return json.dumps(response_object)
    response_object = {"code":"Error"}
    return json.dumps(response_object)
   
   
# Route to Check User Firebase ID
@auth_app.route("/getuser/<firebase_id>")
def get_user(firebase_id):
    
    # **************
    print("GET USER")
    # **************
    
    
    user = Users.query.filter_by(firebase_id=firebase_id).first()
    if(user):
        print("User Exists");
        response_object = {
            "code": "Error",
            "message": "firebase_id already in database"
        }
        return json.dumps(response_object)
    response_object = {"code":"Success"}
    return json.dumps(response_object)

