from flask import Flask
from flask import request
import sys
from flask_cors import *
import json
 
 

app = Flask(__name__)
CORS(app, supports_credentials=True)

ss = {"username":"test","password":"test123"} 
ss = {"test":"test123"} 
@app.route('/')
def hello_world():
    return 'Hello World!'
 
@app.route("/login", methods=['POST'])
def login():
    if request.method == 'POST' and request.form.get('username') and request.form.get('password'):
        datax = request.form.to_dict()
        usernamx = datax.get("username")
        passwordx = datax.get("password")
        print(usernamx,passwordx)
        res = ss.get(usernamx)
        if not res:
            print("-1")
            return "-1"
        elif passwordx != res:
            print("0")
            return "0"
        elif usernamx=="admin" and passwordx == res:
            print("admin")
            return "admin"
        else:
            return "1"
    else:
        return "cccc"
 
@app.route("/main",methods=["GET"])
def getmain():
    if request.method == 'GET':
        res = ss
        xx = json.dumps(res)
        return xx
 
@app.route("/register",methods=["POST"])
def register():
    if request.method == 'POST' and request.form.get('username') and request.form.get('password'):
        datax = request.form.to_dict()
        usernamx = datax.get("username")
        passwordx = datax.get("password")
        ss[usernamx] = passwordx

        return "OK"

    else:
        return "no"
 
if __name__ == '__main__':
    app.run(debug=True)