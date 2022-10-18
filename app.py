from flask import Flask, request, jsonify
from flask_mail import Mail, Message

app = Flask (__name__)

app.config['MAIL_SERVER']='smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = '2a17158b4544d4'
app.config['MAIL_PASSWORD'] = '257030c43b7251'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

users = [
    {'id': 1, 'name': 'Romeo', 'email': 'romeo@example.com'}
]

@app.route('/')
# def home():
#     return("Home of API")
def index():
    msg = Message('Hello from the other side', sender= 'from@example.com', recipients= ['to@example.com'])
    msg.body = "Hey Matt, sending you a message - Shaw"
    mail.send(msg)
    return "Message sent!"


@app.route('/users', methods=['GET', 'POST'])
def user():
    if request.method == 'GET':
        return jsonify(users), 200
    elif request.method == 'POST':
        new_user = request.json
        last_id = users[-1]['id']
        new_user['id'] = last_id + 1
        users.append(new_user)
        return f"{new_user} is created", 201

if __name__ == '__main__':
    app.run(debug=True)
