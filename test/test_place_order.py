import unittest
from run import app
from flask import jsonify, json
from app import views

class Test_Orders(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()


    def test_add_order(self):

        # a test for successful adding an order

        response = self.client.post("/api/v1/orders", data = json.dumps(
            dict(customerId = "12345", orderId = "09876", thetype = "breakfast", food = "milk and bread", 
                 price = "2000", quantity = "2", today = "2018-09-16", status="not completed")), content_type = 'application/json') 

        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "Your order has been placed")
        self.assertEquals(response.status_code, 201)

    
    def test_with_empty_customerId(self):

        # Test for empty customerId validation """

        response = self.client.post("/api/v1/orders", data = json.dumps(
            dict(customerId = "", orderId = "09876", thetype = "breakfast", food = "milk and bread", 
                 price = "2000", quantity = "2", today = "2018-09-16", status="not completed")), content_type = 'application/json')

        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "The customerId is missing")
        self.assertEquals(response.status_code, 400)
      

    def test_with_empty_food(self):

        # Test for empty content validation

        response = self.client.post("/api/v1/orders", data = json.dumps(
            dict(customerId = "12345", orderId = "09876", thetype = "breakfast", food = "", 
                 price = "2000", quantity = "2", today = "2018-09-16", status="not completed")), content_type = 'application/json') 

        reply = json.loads(response.data)
        self.assertEquals(reply['message'], 'Food is missing')
        self.assertEquals(response.status_code, 400)


    def test_with_empty_quantity(self):

        # Test for empty content validation

        response = self.client.post("/api/v1/orders", data = json.dumps(
            dict(customerId = "12345", orderId = "09876", thetype = "breakfast", food = "milk and bread", 
                 price = "2000", quantity = "", today = "2018-09-16", status="not completed")), content_type = 'application/json')  

        reply = json.loads(response.data)
        self.assertEquals(reply['message'], 'Quantity missing')
        self.assertEquals(response.status_code, 400)


    def test_with_empty_price(self):

        # Test for empty content validation """

        response = self.client.post("/api/v1/orders", data = json.dumps(
            dict(customerId = "12345", orderId = "09876", thetype = "breakfast", food = "milk and bread", 
                 price = "", quantity = "2", today = "2018-09-16", status="not completed")), content_type = 'application/json')

        reply = json.loads(response.data)
        self.assertEquals(reply['message'], 'Price missing')
        self.assertEquals(response.status_code, 400)


    def test_with_empty_type(self):

        # Test for empty content validation """

        response = self.client.post("/api/v1/orders", data = json.dumps(
            dict(customerId = "12345", orderId = "09876", thetype = "", food = "milk and bread", 
                 price = "2000", quantity = "2", today = "2018-09-16", status="not completed")), content_type = 'application/json') 

        reply = json.loads(response.data)
        self.assertEquals(reply['message'], 'The type is missing')
        self.assertEquals(response.status_code, 400)


    # def test_with_same_data(self):
    #     """ Test for empty content validation """
    #     response = self.app.post("/api/v1/orders", content_type='application/json',
    #                             data=json.dumps(dict(orderId="1", customerId="1", today="17.07.2018", thetype="breakfast", food="milk", quantity="3", price="2000", status="not completed"),)
    #                             )
    #     response = self.app.post("/api/v1/orders", content_type='application/json',
    #                             data=json.dumps(dict(orderId="1", customerId="1", today="17.07.2018", thetype="breakfast", food="milk", quantity="3", price="2000", status="not completed"),)
    #                             )              
    #     reply = json.loads(response.data)
    #     self.assertEquals(reply['message'], 'Make another order')
    #     self.assertEquals(response.status_code, 403)