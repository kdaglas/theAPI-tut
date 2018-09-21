import unittest
from run import app
from flask import jsonify, json
from app.modules.customer_model import Customer

class Test_auth(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_registration(self):
        """ a test for successful user registration """
        
        response = self.client.post("/api/v1/register", data = json.dumps(
            dict(username = "Douglas", emailaddress="daglach7@gmail.com", contact = "+256-755-598090", 
                password = "Dag1234")), content_type = 'application/json')
                                        
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "Customer has been registered")
        self.assertEqual(response.status_code, 201)

    
    def test_registration_with_empty_username(self):
        """ Test for empty username validation """
        
        response = self.client.post("/api/v1/register", data = json.dumps(
            dict(username = "", emailaddress="daglach7@gmail.com", contact = "+256-755-598090", 
                password = "Dag1234")), content_type = 'application/json')
                                        
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "Username is missing")
        self.assertEqual(response.status_code, 400)
      

    def test_registration_with_empty_emailaddress(self):
        """ Test for empty emailaddress validation """
        
        response = self.client.post("/api/v1/register", data = json.dumps(
            dict(username = "Douglas", emailaddress="", contact = "+256-755-598090", 
                password = "Dag1234")), content_type = 'application/json')              
        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "Emailaddress is missing")
        self.assertEquals(response.status_code, 400)
    
    
    def test_registration_with_empty_password(self):
        """ Test for empty password validation """
        
        response = self.client.post("/api/v1/register", data = json.dumps(
            dict(username = "Douglas", emailaddress="daglach7@gmail.com", contact = "+256-755-598090", 
                password = "")), content_type = 'application/json')              
        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "Password is missing")
        self.assertEquals(response.status_code, 400)


    def test_registration_with_empty_contact(self):
        """ Test for empty password validation """
        
        response = self.client.post("/api/v1/register", data = json.dumps(
            dict(username = "Douglas", emailaddress="daglach7@gmail.com", contact = "", 
                password = "Dag1234")), content_type = 'application/json')              
        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "Contact is missing")
        self.assertEquals(response.status_code, 400)

    
    # def test_user_login_successful(self):
    #     """ Test for successful login """
        
    #     response = self.client.post("/api/v1/login", data = json.dumps(
    #         dict(username = "Douglas", password = "Dag1234")), content_type = 'application/json')           
    #     reply = json.loads(response.data)
    #     self.assertEquals(reply["message"], "Customer has been logged in")
    #     self.assertEquals(response.status_code, 200)


    # def test_user_login_with_no_username(self):
    #     """ Test for login with wrong or no username """       
        
    #     response = self.client.post("/api/v1/login", data = json.dumps(
    #         dict(username = "", password = "Dag1234")), content_type = 'application/json')            
    #     reply = json.loads(response.data)
    #     self.assertEquals(reply["message"], "Username is missing")
    #     self.assertEquals(response.status_code, 400)


    # def test_user_login_with_no_password(self):
    #     """ Test for login with wrong or no password """
        
    #     response = self.client.post("/api/v1/login", data = json.dumps(
    #         dict(username = "Douglas", password = "")), content_type = 'application/json')            
    #     reply = json.loads(response.data)
    #     self.assertEquals(reply["message"], "Password is missing")
    #     self.assertEquals(response.status_code, 400)


    # def test_user_login_with_wrong_information(self):
    #     """ Test for login with wrong or no password """
    #     response = self.client.post(
    #             "/api/v1/login",
    #             content_type='application/json',
    #             data=json.dumps(dict(username="dan", password="itsme"))
    #             )            
    #     reply = json.loads(response.data)
    #     self.assertEquals(reply["message"], "Customer does not exist")
    #     self.assertEquals(response.status_code, 400)
