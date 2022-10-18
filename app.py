from flask import Flask, request, jsonify, json
import os
from flask_cors import CORS
from werkzeug.exceptions import BadRequest
from flask_mail import Mail, Message

app = Flask (__name__)
CORS(app)

app.config['MAIL_SERVER']='smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = '2a17158b4544d4'
app.config['MAIL_PASSWORD'] = '257030c43b7251'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

users = os.path.join(app.static_folder, 'users.json')

with open(users) as user_file:
    users = json.load(user_file)

@app.route('/')
def hello():
    return 'Welcome to our API!'

@app.route('/users', methods= ["GET", "POST"])
def user():
    if request.method == "GET":
        return jsonify(users), 200

    elif request.method == "POST":
        new_user = request.json
        last_id = users[-1]['id']
        new_user['id'] = last_id + 1
        users.append(new_user)
        print('Here is the new user', new_user)
        return "User was created", 201

@app.route('/subscribe')
def index():
    msg = Message('Hello from the other side', sender= 'from@example.com', recipients= ['to@example.com'])
    msg.body = "Hey Matt, sending you a message - Shaw"
    mail.send(msg)
    return "Message sent!"

@app.route('/users/<int:user_id>', methods= ["GET", "DELETE"])
def get_by_id(user_id):
    if request.method == "GET":
        try:
            return next(user for user in users if user['id'] == user_id), 200
        except:
            raise BadRequest(f"Sorry no user with that id found: {user_id}")

    elif request.method == "DELETE":
        try:
            length_before = len(users)
            users[:] = (user for user in users if user['id'] != user_id)
            length_after = len(users)
            if length_before == length_after:
                raise Exception('user not found')
            else:
                return f"User with id: {user_id} was deleted", 204
        except:
            raise BadRequest(f"Sorry no user with that id found: {user_id}")


if __name__=="__main__":
    app.run(debug=True)
