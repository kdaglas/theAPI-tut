import unittest
from app import views
from run import app
import json

class Test_View_Orders(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_get_all_orders(self):
        """ a test for getting all entries """
        response = self.app.post("/api/v1/orders", content_type='application/json',
                                data=json.dumps(dict(orderId="1", customerId="1", today="17.07.2018", thetype="breakfast", food="milk", quantity="3", price="2000", status="not completed"),)
                                )
                  
        reply = json.loads(response.data.decode())
        response2 = self.app.get("/api/v1/orders",
                                content_type='application/json', data=reply)
        reply2 = json.loads(response2.data.decode())
        self.assertEquals(reply2["message"],"All orders successfully viewed")


    # def test_get_all_orders_emty_list(self):
    #     """ a test for getting all entries """
    #     response = self.app.post("/api/v1/orders", content_type='application/json',
    #                             data=json.dumps(dict(orderId="", customerId="", today="", thetype="", food="", quantity="", price="", status="not completed"),)
    #                             )
                  
    #     reply = json.loads(response.data.decode())
    #     response2 = self.app.get("/api/v1/orders",
    #                             content_type='application/json', data=reply)
    #     reply2 = json.loads(response2.data.decode())
    #     self.assertEquals(reply2["message"],"No order added")


    def test_get_single_diary(self):
        '''Test to fetch single diary'''
        response = self.app.post("/api/v1/orders", content_type='application/json',
                                data=json.dumps(dict(orderId="1", customerId="1", today="17.07.2018", thetype="breakfast", food="milk", quantity="3", price="2000", status="not completed"),)
                                )     
            
        reply = json.loads(response.data.decode())
        response2 = self.app.get("/api/v1/orders/1",
                                content_type='application/json', data=reply)
        reply2 = json.loads(response2.data.decode())
        self.assertEquals(reply2["message"],"Single order successfully viewed")

