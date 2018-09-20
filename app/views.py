from app import app
import json
from flask import request, json, jsonify
from app.models import Customer, Order
from datetime import date


customers = []
orders = []


@app.route("/api/v1/register", methods=['POST'])
def register():
    data = request.get_json()
    customerId = len(customers) + 1
    username = data.get('username')
    emailaddress = data.get('emailaddress')
    contact = data.get('contact')
    password = data.get('password')

    if len(username) < 1:
        return jsonify({'message': 'Username is missing'}), 400
    if len(emailaddress) < 1:
        return jsonify({'message': 'Emailaddress is missing'}), 400
    if len(contact) < 1:
        return jsonify({'message': 'Contact is missing'}), 400
    if len(password) < 1:
        return jsonify({'message': 'Password is missing'}), 400

    new_customer = Customer(id, username, emailaddress, contact, password)
    customers.append(new_customer)
    return jsonify({'message': 'Customer successfully registered'})


@app.route("/api/v1/login", methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if len(username) < 1:
        return jsonify({'message': 'Username is missing'}), 400
    if len(password) < 1:
        return jsonify({'message': 'Password is missing'}), 400

    for customer in customers:
        if customer.username == username and customer.password == password:
            return jsonify({'message': 'Successfully logged in'}), 200
    return jsonify({'message': 'Customer does not exist'}), 400


@app.route("/api/v1/orders", methods=['POST'])
def place_order():
    data = request.get_json()
    orderId = len(orders) + 1
    customerId = data.get('customerId')
    today = str(date.today())
    food = data.get('food')
    thetype = data.get('thetype')
    price = data.get('price')
    quantity = data.get('quantity')
    status = 'not completed'

    if len(food) < 1:
        return jsonify({'message': 'Food is missing'}), 400
    elif len(customerId) < 1:
        return jsonify({'message': 'The customerId is missing'}), 400
    elif len(thetype) < 1:
        return jsonify({'message': 'The type is missing'}), 400
    elif len(price) < 1:
        return jsonify({'message': 'Price missing'}), 400
    elif len(quantity) < 1:
        return jsonify({'message': 'Quantity missing'}), 400

    for order in orders:
        if order.customerId == customerId and order.food == food:
            return jsonify({'message':'Make another order'}), 403
        
    new_order = Order(orderId, today, customerId, thetype, food, price, quantity, status)
    orders.append(new_order)   
    
    return jsonify({'message': 'Order successfully added'}), 200


@app.route("/api/v1/orders", methods=['GET'])
def get_all_orders():
    if len(orders) > 0:
        return jsonify({'message': 'All orders successfully viewed',
                        'All entries here': [
                            order.__dict__ for order in orders
                        ]}), 200

    return jsonify({'message': 'No order added'}), 404


@app.route("/api/v1/orders/<orderId>", methods=["GET"])
def get_single_order(orderId):
    if int(orderId) > 0:
        if len(orders) > 0:
            for order in orders:
                if order.orderId == int(orderId):
                    return jsonify({
                        "message": "Single order successfully viewed",
                        "Diary Entry": order.__dict__
                    }), 200

            return jsonify({"message": "order doesnot exist"})
        return jsonify({"message": "No order has been registered yet"}), 404
    return jsonify({"message": "Single order id has to bigger than zero"}), 404


@app.route("/api/v1/orders/<orderId>", methods=["PUT"])
def edit_order(orderId):
    data = request.get_json()
    new_order = {}
    new_order['status'] = data.get('status')

    for order in orders:
        if order.orderId == int(orderId):
            order.status = new_order['status']
            return jsonify({"message": "order has been modified"}), 200
        return jsonify({"message": "No such order"}), 404
    return jsonify({"message": "Single order id has to be bigger than zero"}), 404
