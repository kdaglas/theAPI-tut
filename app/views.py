from app import app
from flask import request, json, jsonify
from app.modules.customer_model import Customer
from app.modules.order_model import Order
from app.validation.validate import Validate
from datetime import date
import uuid


@app.route("/api/v1/register", methods=['POST'])
def register():

    try:
        data = request.get_json()
        customerId = int(str(uuid.uuid1().int)[:5])
        username = data.get('username')
        emailaddress = data.get('emailaddress')
        contact = data.get('contact')
        password = data.get('password')

        valid = Validate.validate_registration_inputs(data['username'], data['emailaddress'], data['contact'], data['password'])

        if valid == True:
            new_customer = Customer(customerId, username, emailaddress, contact, password)
            registered_customer = Customer.register_customer(new_customer)
            return jsonify({'New customer':registered_customer,
                            'message': 'Customer has been registered'}), 201
        else:
            return valid
    except:
        response = jsonify({"message": "The key or value fields are invalid or missing"})
        response.status_code = 403
        return response 


@app.route("/api/v1/login", methods=['POST'])
def login(username, password):
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if len(username) < 1:
        return jsonify({'message': 'Username is missing'}), 400
    if len(password) < 1:
        return jsonify({'message': 'Password is missing'}), 400

    # customer = Customer.get_a_customer(customerId)
    # return jsonify({'Customer': customer, 'message': 'Your one order successfully viewed'}), 201

    # for customer in all_customers:
    #     if customer.username == username and customer.password == password:
    #         return jsonify({'message': 'Successfully logged in'}), 200
    # return jsonify({'message': 'Customer does not exist'}), 400

    customer = Customer.login(username, password)
    return jsonify({'message': 'Customer has been logged in'}), 200


@app.route("/api/v1/orders", methods=['POST'])
def place_order():

    try:
        data = request.get_json()
        orderId = int(str(uuid.uuid1().int)[:5])
        customerId = data.get('customerId')
        today = str(date.today())
        food = data.get('food')
        thetype = data.get('thetype')
        price = data.get('price')
        quantity = data.get('quantity')
        status = 'not completed'

        valid = Validate.validate_order_input(data['customerId'], data['thetype'], data['food'], data['price'], data['quantity'])

        if valid == True:     
            new_order = Order(customerId, orderId, thetype, food, price, quantity, status, today)
            placed_order = Order.place_order(new_order)
            return jsonify({'Placed order': placed_order,
                            'message': 'Your order has been placed'}), 201
        else:
            return valid
    except:
        response = jsonify({"message": "The key or value fields are invalid or missing"})
        response.status_code = 403
        return response


@app.route("/api/v1/orders", methods=['GET'])
def get_all_orders():
    
    all_orders = Order.get_all_orders()
    return jsonify({'All your orders': all_orders,
                    'message': 'All orders have been viewed'}), 302


@app.route("/api/v1/orders/<orderId>", methods=["GET"])
def get_single_order(orderId):
    
    order = Order.get_one_order(orderId)
    return jsonify({"Your order": order,
                    'message': 'One order has been viewed'}), 302


@app.route("/api/v1/orders/<orderId>", methods=["PUT"])
def edit_order(orderId):
    
    data = request.get_json()
    status = data.get('status')

    updated_order = Order.update_order(orderId, status)
    return jsonify({"Updated order": updated_order,
                'message': 'Order status has been updated'}), 201
