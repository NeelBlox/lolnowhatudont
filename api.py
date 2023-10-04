from flask import  Flask, request, redirect, url_for, render_template, jsonify
import json
import requests
from firebase import firebase
firebase = firebase.FirebaseApplication("https://premis-f8e8d-default-rtdb.firebaseio.com/", None)
app = Flask(__name__)
@app.route('/')
def no():
    return '?'

@app.route('/premis/<string:n>')
def premis(n):
    user_id = firebase.get('/',n)
    if user_id!=None:
        result={
        "access_key":n,
        "user_id":user_id,
        "status":True
            }
    else:
        result={
            "status":False
            }
    return jsonify(result)
    
if __name__=="__main__":
    app.run()