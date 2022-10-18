from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask (__name__)
CORS(app)

@app.route('/')
def hello():
    return 'Welcome to our API!'

@app.route('/users', methods= ["GET", "POST", "DELETE"]):
def user():
    if 

if __name__=="__main__":
    app.run(debug=True)
