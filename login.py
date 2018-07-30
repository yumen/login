from flask import Flask
from flask import request,make_response,jsonify
import sys
from flask_cors import *
import json,time,jwt,re
 
 

app = Flask(__name__)
CORS(app, supports_credentials=True)

payload = {
    "iat": int(time.time()),
    "exp": int(time.time()) + 86400 * 7,
    "aud": "www.gusibi.com",
    "username": "",
}
secret = "secret_test123"


ss = {"test":"test123"} 

def verify_bearer_token(token):
    #  如果在生成token的时候使用了aud参数，那么校验的时候也需要添加此参数
    p = jwt.decode(token, secret, audience='www.gusibi.com', algorithms=['HS256'])
    if p:
        print(p)
        return True, token
    return False, token

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
        # elif usernamx=="admin" and passwordx == res:
            # print("admin")
            # return "admin"
        else:
            payload["username"] = usernamx
            token = jwt.encode(payload, secret, algorithm='HS256')
            response = make_response(jsonify({'token':token.decode('utf-8')}))
            
            response.set_cookie('username','usernamx')
            response.set_cookie('token',token.decode('utf-8'))
            #response.headers['token'] = 456

            return response
    else:
        return "cccc"
 
@app.route("/main",methods=["GET"])
def getmain():
    print(request.headers.get("Cookie"))
    #token = re.findall("token=(.*)",request.headers.get("Cookie"))
    #print(token[0])
    print(verify_bearer_token(request.cookies.get('token')))
    if request.method == 'GET':
        return json.dumps([user for user in ss.keys()])
 
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