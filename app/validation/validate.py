import re
from flask import jsonify
# from app.modules.order_model import Order
# from app.modules.customer_model import Customer


class Validate():

    # def __init__(self, mealId, thetype, food, price, quantity):

    #     # valiation class for the meal inputs

    #     self.mealId = mealId
    #     self.thetype = thetype
    #     self.food = food
    #     self.price = price
    #     self.quantity = quantity


    @classmethod
    def validate_registration_inputs(cls, username, emailaddress, contact, password):

        # method to validate customer input

        if username == '' or emailaddress == '' or contact == '' or password == '':
            return jsonify({"message": "Some data is missing"}), 400
        elif ' ' in username:
            return jsonify({"message": "Username should have no spaces"}), 400
        elif not re.search(r"\b[a-zA-Z]+\b", username):
            return jsonify({"message": "Username should be in characters"}), 400
        elif not re.search(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", emailaddress):
            return jsonify({"message": "Email address should be like this format 'daglach7@gmail.com'"}), 400
        elif not re.search(r"^\+256[-]\d{3}[-]\d{6}$", contact):
            return jsonify({"message": "Contact should be like this format '+256-755-598090'"}), 400
        elif not re.search(r"^(?=.*[a-zA-Z])(?=.*\d)[a-zA-Z\d]{7}$", password):
            return jsonify({"message": "Password must have 7 characters with atleast a lowercase, uppercase letter and a number"}), 400
        else:
            return True


    @classmethod
    def validate_order_input(cls, customerId, thetype, food, price, quantity):

        # method to validate my order input

        if customerId == '' or thetype == '' or food == '' or price == '' or quantity == '':
            return jsonify({"message": "Some data is missing"}), 400
        elif not re.search(r"\b[0-9]+\b", customerId):
            return jsonify({"message": "The customer's id should be a number"}), 400
        elif ' ' in thetype or ' ' in price or ' ' in quantity:
            return jsonify({"message": "No spaces allowed"}), 400
        elif not re.search(r"\b[a-zA-Z]+\b", thetype):
            return jsonify({"message": "The type of food should be in characters"}), 400
        elif not re.search(r"^([a-zA-Z]+\s)*[a-zA-Z]+$", food):
            return jsonify({"message": "The food should be in characters"}), 400
        elif not re.search(r"\b[0-9]+\b", price):
            return jsonify({"message": "The price should be in numbers"}), 400
        elif not re.search(r"\b[0-9]+\b", quantity):
            return jsonify({"message": "The quantity should be a number"}), 400
        else:
            return True


    # @classmethod
    # def validate_id(cls, orderId):
        
    #     # method to validate the ids input by the customer

    #     if type(orderId) != int:
    #         return jsonify({"message": "Your order id should be a number"}), 400
    #     elif not orderId:
    #         return jsonify({"message": "Your order id is missing"}), 400
    #     else:
    #         return True


    # @classmethod
    # def validate_duplicate(cls, customerId, all_orders):
        
    #     # method to validate the ids input by the customer

    #     for order in all_orders:
    #         if order['customerId'] == customerId:
    #             return True




    # def __init__(self, customerId, username, emailaddress, contact, password):

    #     # valiation class for the meal inputs

    #     self.customerId = customerId
    #     self.username = username
    #     self.emailaddress = emailaddress
    #     self.contact = contact
    #     self.password = password


    

        