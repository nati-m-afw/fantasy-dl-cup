# Importing
from flask import Blueprint,request,json

# Importing DB Instance
from main import db

# Importing DB Models
from models.users import Users

# Importing Restx Api
from flask_restx import Resource, Api

# Import JWT
from flask_jwt_extended import create_access_token


# Creating a Blueprint
auth_app = Blueprint("auth",__name__)

# Creating API Instance
auth = Api(auth_app)



#Route to add user to database
@auth.route("/signuser")
class Register(Resource):
    def post(self):
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
                
            return (response_object) , 200
        except:
            print("ERRORRRR")
            return ({}) 
   
   
   
# Route to get User ID
@auth.route("/getUserID/<firebase_id>")
class UserId(Resource):
    def post(self,firebase_id):
        # ******************
        print("GET USER ID")
        # ******************
        
        user = Users.query.filter_by(firebase_id=firebase_id).first()
        if(user):
            access_token = create_access_token(identity=user.id)
            response_object = {
                "code": "Success",
                "id": user.id,
                "token":access_token,
                "team_name": user.teamname
            }
            return (response_object)
        response_object = {"code":"Error"}
        return (response_object)
   
   
# Route to Check User Firebase ID
@auth_app.route("/getuser/<firebase_id>")
class User(Resource):
    def get(self,firebase_id):
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
            return(response_object)
        response_object = {"code":"Success"}
        return (response_object)
