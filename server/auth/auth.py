# Importing
from flask import Blueprint,request,json
from main import db
from models.users import Users


# Creating a Blueprint
auth_app = Blueprint("auth",__name__)

# Registering Routes

#Route to add user to database
@auth_app.route("/signUpUser",methods=['GET','POST'])
def register_user():
    if request.method == 'POST':
        response_object = {'status':'success'}
        post_data = request.get_json()
        new_firebase_id = post_data['firebase_id']
        new_user = Users(firebase_id=new_firebase_id);
        db.session.add(new_user)
        db.session.commit()
        print("User Added")
        return json.dumps(response_object)
   
   
   
# Route to get User ID
@auth_app.route("/getUserID/<firebase_id>",methods=['GET','POST'])
def get_user_id(firebase_id):
    print("Invoked")
    user = Users.query.filter_by(firebase_id=firebase_id).first()
    if(user):
        response_object = {
            "code": "Success",
            "id": user.id
        }
        return json.dumps(response_object)
    response_object = {"code":"Error"}
    return json.dumps(response_object)
   
   
# Route to Check User Firebase ID
@auth_app.route("/getUser/<firebase_id>")
def get_user(firebase_id):
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

