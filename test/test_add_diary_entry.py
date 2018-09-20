import unittest
from run import app
from flask import jsonify, json
from app import views

class Test_Orders(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_add_order(self):
        """ a test for successful adding an order """
        response = self.app.post("/api/v1/orders", content_type='application/json',
                                data=json.dumps(dict(orderId="1", customerId="1", today="17.07.2018", thetype="breakfast", food="milk", quantity="3", price="2000", status="not completed"),)
                                )      
        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "Order successfully added")
        self.assertEquals(response.status_code, 200)

    
    def test_with_empty_customerId(self):
        """ Test for empty customerId validation """
        response = self.app.post("/api/v1/orders", content_type='application/json',
                                data=json.dumps(dict(orderId="1", customerId="", today="17.07.2018", thetype="breakfast", food="milk", quantity="3", price="2000", status="not completed"),)
                                )              
        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "The customerId is missing")
        self.assertEquals(response.status_code, 400)
      

    def test_with_empty_food(self):
        """ Test for empty content validation """
        response = self.app.post("/api/v1/orders", content_type='application/json',
                                data=json.dumps(dict(orderId="1", customerId="1", today="17.07.2018", thetype="breakfast", food="", quantity="3", price="2000", status="not completed"),)
                                )              
        reply = json.loads(response.data)
        self.assertEquals(reply['message'], 'Food is missing')
        self.assertEquals(response.status_code, 400)


    def test_with_empty_quantity(self):
        """ Test for empty content validation """
        response = self.app.post("/api/v1/orders", content_type='application/json',
                                data=json.dumps(dict(orderId="1", customerId="1", today="17.07.2018", thetype="breakfast", food="milk", quantity="", price="2000", status="not completed"),)
                                )              
        reply = json.loads(response.data)
        self.assertEquals(reply['message'], 'Quantity missing')
        self.assertEquals(response.status_code, 400)


    def test_with_empty_price(self):
        """ Test for empty content validation """
        response = self.app.post("/api/v1/orders", content_type='application/json',
                                data=json.dumps(dict(orderId="1", customerId="1", today="17.07.2018", thetype="breakfast", food="milk", quantity="3", price="", status="not completed"),)
                                )              
        reply = json.loads(response.data)
        self.assertEquals(reply['message'], 'Price missing')
        self.assertEquals(response.status_code, 400)


    def test_with_empty_type(self):
        """ Test for empty content validation """
        response = self.app.post("/api/v1/orders", content_type='application/json',
                                data=json.dumps(dict(orderId="1", customerId="1", today="17.07.2018", thetype="", food="milk", quantity="3", price="2000", status="not completed"),)
                                )              
        reply = json.loads(response.data)
        self.assertEquals(reply['message'], 'The type is missing')
        self.assertEquals(response.status_code, 400)


    def test_with_same_data(self):
        """ Test for empty content validation """
        response = self.app.post("/api/v1/orders", content_type='application/json',
                                data=json.dumps(dict(orderId="1", customerId="1", today="17.07.2018", thetype="breakfast", food="milk", quantity="3", price="2000", status="not completed"),)
                                )
        response = self.app.post("/api/v1/orders", content_type='application/json',
                                data=json.dumps(dict(orderId="1", customerId="1", today="17.07.2018", thetype="breakfast", food="milk", quantity="3", price="2000", status="not completed"),)
                                )              
        reply = json.loads(response.data)
        self.assertEquals(reply['message'], 'Make another order')
        self.assertEquals(response.status_code, 403)
