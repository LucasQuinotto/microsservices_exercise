from flask import Flask
from order import Order

app = Flask(__name__)

@app.route("/order/create_order/", methods=['POST'])
def create_order():
    return Order().create_order()

@app.route("/order/update_order/", methods=['PUT'])
def update_order():
    return Order().update_order()

@app.route("/order/delete_order/", methods=['DELETE'])
def delete_order():
    return Order().delete_order()

@app.route("/order/select_orders/", methods=["GET"])
def select_orders():
    return Order().select_orders()

@app.route("/order/select_users_with_orders/", methods=["GET"])
def select_users_with_orders():
    return Order().select_users_with_orders()

if __name__ == "__main__":
    app.run(debug=True)