from flask import  Flask, request, redirect, url_for, render_template, jsonify
import json
import requests
import string

import secrets
from firebase import firebase
firebase1 = firebase.FirebaseApplication("https://premis-f8e8d-default-rtdb.firebaseio.com/", None)
firebase2=firebase.FirebaseApplication("https://premis-userdb-default-rtdb.firebaseio.com/")
app = Flask(__name__)
@app.route('/')
def no():
    moh={
        "message":"Premis API is live",
        "success": True
        }
    return moh

@app.route('/premis/<string:n>')
def premis(n):
    user_id = firebase1.get('/',n)
    if user_id==True:
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
@app.route('/premis/code=<string:m>/user=<int:y>')
def gen(m,y):
    get_first=firebase2.get('/',y)
    
    if get_first==True:
        result={
            "status":False,
            "reason":"User already has a key!"
            }
        
    else:
        if m=='parthmani':
            characters = string.ascii_lowercase + string.digits
            key = ''.join(secrets.choice(characters) for _ in range(16))
            np=True
            result={
                "key":key,
                "status":True
                }
            firebase1.put('/',key,np)
            firebase2.put('/',y,np)
        else:
            result={
            "status":"notok"
            }
    return result


if __name__=="__main__":
    app.run()
