from flask import Flask, session, render_template, request, redirect, url_for, jsonify
from dotenv import load_dotenv


app = Flask(__name__)
load_dotenv()


if __name__ == '__main__':
    app.run()