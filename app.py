from flask import  Flask, request, redirect, url_for, render_template, jsonify
import json
import requests
import string
import secrets
from firebase import firebase
firebase = firebase.FirebaseApplication("https://premis-f8e8d-default-rtdb.firebaseio.com/", None)
app = Flask(__name__)
@app.route('/')
def no():
    return '?'

@app.route('/premis/<string:n>')
def premis(n):
    user_id = firebase.get('/',n)
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
@app.route('/premis/code=<string:m>')
def gen(m):
    if m=='parthmani':
        characters = string.ascii_lowercase + string.digits
        key = ''.join(secrets.choice(characters) for _ in range(16))
        np=True
        result={
            "key":key,
            "status":np
            }
        firebase.put('/',key,np)
    else:
        result={
            "key":'Code invalid not authorized'
            }
    return result
if __name__=="__main__":
    app.run()
