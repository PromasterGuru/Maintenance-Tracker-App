import unittest
import json
from app import create_new_app
from app import views
from app.authentication_handler import generate_new_token

"""Authentication test"""
class AuthenticationTest(unittest.TestCase):

	"""set up test variables and create new app with testing config"""
	#create app with testing config
	def setUp(self):
		
		self.app = create_new_app(config_name="testing")
		#test user
		self.user = self.app.test_user
		# user test json with predifined variables
		self.db_users= {
			'requestid':201,
			'user': 102,
			'projectid': 101,
			'request_type': 'Maintenance', 
			'request_description': 'Ugrade to the latest version.',
            'request_date': '12/23/2017',
            'Approved/Rejected':'Approved',
            'status':'Resolved'
			}
		#initialize endpoints
		self.rgtr_route = '/api/v1/register'
		self.lgn_route= '/api/v1/login'
		self.confirm_route = '/verify/'

		with self.app.app_context():
			self.confirm_token=generate_new_token('email@mail.com')

	def test_registration(self):
		user = {'user_id': 101,'username': 'promaster','email': 'promaster@daisy.com','userpassword': 'promaster'}
		user_requests = self.user().post(self.rgtr_route, data=user)
		#check that the status code is 201
		self.assertEqual(user_requests.status_code, 201)

	def test_existing_user(self):
		"""test user can only register only once"""
		user_requests = self.user().post(self.rgtr_route, data=self.user_data)
		second_user_requests = self.user().post(self.rgtr_route, data=self.user_data)
		self.assertEqual(second_user_requests.status_code, 409)

	def test_user_login(self):
		"""Test if registered user can login"""
		user_requests = self.user().post(self.rgtr_route, data=self.user_data)
		self.user().get(self.confirm_route + '{}'.format(self.confirm_token.decode("utf-8")))
		login_user_requests = self.user().post(self.lgn_route, data=self.user_data)
		#get jsonified result and test whether the status code is 200
		result = json.loads(login_user_requests.data.decode())
		self.assertEqual(login_user_requests.status_code, 200)
		#check if it has an access token
		self.assertTrue(result['access_token'])

	def test_non_registered_user_login(self):
		"""Test that anathenticated user can't login"""
		#create a dict for unregistered users
		anonymous = {
			'username': 'anonymuser',
			'password': 'nopassword'
		}
		#try to login as an anonymous user
		user_requests = self.user().post(self.lgn_route, data=anonymous)
		# get jsonified result and check for aunauthenticated status code (401)
		result = json.loads(user_requests.data.decode())
		self.assertEqual(user_requests.status_code, 401)

if __name__ == "__main__":
	unittest.main()
