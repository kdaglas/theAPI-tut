import unittest
from app import views
from run import app
import json

class Test_Edit_Entry(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_edit_entry(self):
        '''Test to modify single diary'''
        response = self.app.post("/api/v1/diaries",
                                content_type='application/json',
                                data=json.dumps(dict(id="1", title="Coding", content="The best way of life is code", today="17.07.2018"),)
                                )

        response = self.app.put("/api/v1/diaries/1",
                                content_type='application/json',
                                data=json.dumps(dict(id="1", title="Andela", content="The way to me, code", today="17.07.2018"),)
                                )

        data = json.loads(response.data.decode())
        self.assertEquals(data["message"], "Entry has been modified")
