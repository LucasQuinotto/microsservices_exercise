from flask import Flask, request
from user import User

app = Flask(__name__)

@app.route("/user/create_user/", methods=['POST'])
def create_user():
    return User().create_user()

if __name__ == "__main__":
    app.run(debug=True)