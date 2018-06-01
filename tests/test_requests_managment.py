import unittest
import json
from app import create_new_app
from app.authentication_handler import generate_new_token

#This class is used to test user maintenance requests
class RequestManagmentTest(unittest.TestCase):
    def setUp(self):
        """Initialize the app"""
        self.app = create_new_app(config_name="App Testing")
        #Declare variables
        self.user = self.app.test_user
        self.request_msg = {
            'request_id':201,
            'user': 102,
            'project_id': 101,
            'request_type': 'Maintenance',
            'request_description': 'Ugrade to the latest version.',
            'request_date': '12/23/2017',
            'Approved/Rejected':'Approved',
            'status':'Resolved'
        }

        self.request_msg_route = '/api/v1/requests/'

        # bind the app to the current context
        with self.app.app_context():
            self.confirm_token = generate_new_token("email@mail.com")

    def test_create_requests(self):
        """Test API with POST request"""
        # create a new post request
        user_requests = self.user().post(self.request_msg_route,data=self.request_msg)
        self.assertEqual(user_requests.status_code, 201)

    def test_get_all_user_requests(self):
        """Test API with GET request"""
        # get all the user requests
        user_requests = self.user().get(self.request_msg_route,)
        self.assertEqual(user_requests.status_code, 200)

    def test_get_request_by_id(self):
        """Test get a single request usign request_id."""
        user_requests = self.user().get(
            self.request_msg_route + '{}'.format(['request_id']))
        self.assertEqual(result.status_code, 200)

    def test_modify_request(self):
        """Test API with PUT request"""
        # modify and existing request
        user_requests = self.user().put(self.request_msg_route + '{}'.format(['request_id']),
                                  data={
                                      "status": "success"
                                  })
        self.assertEqual(user_requests.status_code, 200)

    def test_delete_request(self):
        """Test user can delete created request"""
        user_requests = self.user().delete(self.request_msg_route + '{}'.format(['request_id']))
        self.assertEqual(user_requests.status_code, 200)

if __name__ == "__main__":
    unittest.main()
