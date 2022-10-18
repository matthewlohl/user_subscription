from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.exceptions import BadRequest

app = Flask (__name__)
CORS(app)

users = [
    {'id': 1, 'name':'Stefan', 'email':'something@example.com'},
    {'id':2, 'name':'Camila', 'email':'something1@example.com'},
    {'id':3, 'name':'Matt', 'email':'something2@example.com'}
]

# print(type(users))
# users[:] = (user for user in users if user['id'] != 1)
# print('Here is the new list', users)

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


@app.route('/users/<int:user_id>', methods= ["GET", "DELETE"])
def get_by_id(user_id):
    if request.method == "GET":
        try:
            return next(user for user in users if user['id'] == user_id)
        except:
            raise BadRequest(f"Sorry no user with that id found: {user_id}")

    elif request.method == "DELETE":
        try:
            users[:] = (user for user in users if user['id'] != user_id)
            return f"User with id: {user_id} was deleted"
        except:
            raise BadRequest(f"Sorry no user with that id found: {user_id}")


if __name__=="__main__":
    app.run(debug=True)
