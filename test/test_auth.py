import unittest
from run import app
from flask import jsonify, json
from app.modules.customer_model import Customer

class Test_auth(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_registration(self):

        # Testing for user registration
        
        response = self.client.post("/api/v1/register", data = json.dumps(
            dict(username = "Douglas", emailaddress="daglach7@gmail.com", contact = "+256-755-598090", 
                password = "Dag1234")), content_type = 'application/json')
                                        
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "Customer has been registered")
        self.assertEqual(response.status_code, 201)


    def test_registration_with_wrong_keys(self):

        # Testing for user registration
        
        response = self.client.post("/api/v1/register", data = json.dumps(
            dict(username = "Douglas", email = "daglach7@gmail.com", contact = "+256-755-598090", 
                password = "Dag1234")), content_type = 'application/json')
                                        
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "The key or value fields are invalid or missing")
        self.assertEqual(response.status_code, 403)

    
    def test_registration_with_empty_username(self):
        
        # Test for empty username validation
        
        response = self.client.post("/api/v1/register", data = json.dumps(
            dict(username = "", emailaddress = "daglach7@gmail.com", contact = "+256-755-598090", 
                password = "Dag1234")), content_type = 'application/json')
                                        
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "Username is missing")
        self.assertEqual(response.status_code, 400)
      

    def test_registration_with_empty_emailaddress(self):

        # Testing for empty emailaddress validation
        
        response = self.client.post("/api/v1/register", data = json.dumps(
            dict(username = "Douglas", emailaddress="", contact = "+256-755-598090", 
                password = "Dag1234")), content_type = 'application/json')

        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "Email address is missing")
        self.assertEquals(response.status_code, 400)
    
    
    def test_registration_with_empty_password(self):
        
        # Test for empty password validation """
        
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


    def test_input_with_wrong_username(self):

        # Test for wrong username validation 

        response = self.client.post("/api/v1/register", data = json.dumps(
            dict(username = "2dag", emailaddress="daglach7@gmail.com", contact = "+256-755-598090", 
                 password = "Dag1234")), content_type = 'application/json')
                                           
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "Username should be in characters")
        self.assertEqual(response.status_code, 400)


    def test_input_with_spaces_in_username(self):

        # Test for spaces in username validation 

        response = self.client.post("/api/v1/register", data = json.dumps(
            dict(username = " dag", emailaddress="daglach7@gmail.com", contact = "+256-755-598090", 
                 password = "Dag1234")), content_type = 'application/json')
                                           
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "Username should have no spaces")
        self.assertEqual(response.status_code, 400)


    def test_input_with_wrong_emailaddress(self):

        # Test for wrong emailaddress validation 

        response = self.client.post("/api/v1/register", data = json.dumps(
            dict(username = "Dag", emailaddress="daglach7gmailcom", contact = "0755598090", 
                 password = "Dag1234")), content_type = 'application/json')
                                           
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "Email address should be like this format 'daglach7@gmail.com'")
        self.assertEqual(response.status_code, 400)


    def test_input_with_wrong_contact(self):

        # Test for wrong contact validation 

        response = self.client.post("/api/v1/register", data = json.dumps(
            dict(username = "Dag", emailaddress="daglach7@gmail.com", contact = "0755598090", 
                 password = "Dag1234")), content_type = 'application/json')
                                           
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "Contact should be like this format '+256-755-598090'")
        self.assertEqual(response.status_code, 400)


    def test_input_with_wrong_password(self):

        # Test for empty password validation 

        response = self.client.post("/api/v1/register", data = json.dumps(
            dict(username = "Dag", emailaddress="daglach7@gmail.com", contact = "+256-755-598090", 
                 password = "fgt5")), content_type = 'application/json')
                                           
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "Password must have 7 characters with atleast a lowercase, uppercase letter and a number")
        self.assertEqual(response.status_code, 400)

    
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
