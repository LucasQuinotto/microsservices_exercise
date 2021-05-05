from flask import Flask
from user import User

app = Flask(__name__)

@app.route("/user/create_user/", methods=['POST'])
def create_user():
    return User().create_user()

@app.route("/user/delete_user/", methods=['DELETE'])
def delete_user():
    return User().delete_user()

@app.route("/user/select_users/", methods=['GET'])
def select_users():
    return User().select_users()

@app.route("/user/update_user/", methods=['PUT'])
def update_user():
    return User().update_user()

if __name__ == "__main__":
    app.run(debug=True)