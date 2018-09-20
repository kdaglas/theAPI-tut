import unittest
from app import views
from run import app
import json

class Test_Edit_Entry(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_edit_order(self):
        '''Test to modify single diary'''
        response = self.app.post("/api/v1/orders", content_type='application/json',
                                data=json.dumps(dict(orderId="1", customerId="1", today="17.07.2018", thetype="breakfast", food="milk", quantity="3", price="2000", status="not completed"),)
                                )

        response = self.app.put("/api/v1/orders/1", content_type='application/json',
                                data=json.dumps(dict(orderId="1", customerId="1", today="17.07.2018", thetype="breakfast", food="milk", quantity="3", price="2000", status="completed"),)
                                )

        data = json.loads(response.data.decode())
        self.assertEquals(data["message"], "order has been modified")
