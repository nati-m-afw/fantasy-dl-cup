from flask import Flask, session, render_template, request, redirect, url_for, jsonify
from dotenv import load_dotenv
from flask_cors import CORS


app = Flask(__name__)
load_dotenv()


# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


PLAYERS = [
    {
        'name': 'Sportsguy',
        'price': '3.5'
    },
    {
        'name': 'Bguy',
        'price': '4.5'
    }
]


@app.route('/getplayers/<position>')
def getPlayers(position):
    response = { 'status': 'success'}
    response['players'] = PLAYERS
    return response

if __name__ == '__main__':
    app.run()