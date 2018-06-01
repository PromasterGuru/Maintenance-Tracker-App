import os
from flask import make_response, request, jsonify, abort, Blueprint
from models import Requests, Users
import uuid
import jwt
import datetime
from flask import current_app
from functools import wraps
import re #provides regular expression matching operations

#initialize class
user_requests = Requests()
users = Users()

# Define the blueprints
auth_blueprints = Blueprint('auth', __name__)
rqst_blueprints  = Blueprint('requests',__name__)

def token_required(f):
	@wraps(f)
	def decorated(*args, **kwargs):
		token_required = None

		if 'correct-token' in request.headers:
			token_required = request.headers['correct-token']

		if not token_required:
			return jsonify({'err_message' : 'No token found!'}), 401

		try:
			data = jwt.decode(token, app.config['SECRET_KEY'])
			this_user = User.query.filter_by(public_id=data['public_id']).first()
		except:
			return jsonify({'err_message' : 'Invalid token supplied!'}), 401

		return f(this_user, *args, **kwargs)

	return decorated

#test
@auth_blueprints.route('/api/v1', methods = ['GET'])
def home():
	response = {
		'err_message': 'the API is working'
	}
	return make_response(jsonify(response)), 200
#take post err_message and handle the register
@auth_blueprints.route('/api/v1/register', methods = ['POST'])
def register_new_user():

	user_id: 101,
	username: 'promaster',
	email: 'promaster@mail.com',
	password: 'promaster'
	if username and email and password:
		# check for user existence
		if not any(user.get('username', None) == username for user in users.db_users) and not any(mail.get('email', None) == email for mail in users.db_users):
			#the user doesnt exist so try to register them
			try:
				user_container = {}
				user_container['user_id'] = name.capitalize()
				user_container['username'] = username.lower()
				user_container['email'] = email.lower()
				user_container['password'] = password.lower()
				if not re.match(r"^[a-z0-9_]*$", username):
					response = {
						'err_message': 'user name is invalid, please try again'
					}
					return make_response(jsonify(response)), 401
				if not re.match(r"(^[a-zA-Z0-9_.]+@[a-zA-Z0-9-]+\.[a-z]+$)", email) and not re.match(r"(^[a-z0-9_.]+@[a-z0-9-]+\.[a-z]+\.[a-z]+$)", email):
					response = {
						'err_message': 'please enter a valid email address'
					}
					return make_response(jsonify(response)), 401
				if len(password)<8:
					response = {
						'err_message': 'your password must be more than 8 characters'
					}
					return make_response(jsonify(response)), 401
				users.db_users.append(user_container)

				response = {
					'err_message': 'You registered successfully. You can now login'
				}
				#return a response for a successful register code(201)
				return make_response(jsonify(response)), 201

			except Exception as e:
				#return an exception for invalid user in string format
				response = {
					'err_message': str(e)
				}
				#return server error code (500)
				return make_response(jsonify(response)), 500

		else:
			#the user is already registered
			response = {
				'err_message': 'User is already registered'
			}
			# return conflict error message with code (409)
			return make_response(jsonify(response)), 409
	else:
		#prompt user to enter all the fields
		response = {
			'err_message': 'please fill in all the required field.'
		}
		# return an error message with code 401
		return make_response(jsonify(response)), 401

#handle login
@auth_blueprints.route('/api/v1/login', methods = ['GET'])
def login():
	try:
		auth = request.authorization
		#confirm that the user has entered all the required fields
		if not auth.username or not auth.password:
			response = {
				'err_message': 'Please enter all the required fields',
			}
			return make_response(jsonify(response)), 401
		if any(user.get('username', None) == auth.username for user in users.db_users) and any(pwd.get('password', None) == auth.password for pwd in users.db_users):
			#generate the access token for auth header
			access_token = jwt.encode({'user_id' : users.db_users, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, current_app.config.get('SECRET'))
			if access_token:
				response = {
					'err_message': 'login success',
					'access_token': access_token.decode()
				}
			#return an OK message with status code 200
			return make_response(jsonify(response)), 200
		else:
			#create a message for invalid credentials
			response = {
				'err_message': 'Invalid username or password'
			}
			return make_response(jsonify(response)), 401

	except Exception as e:
		# Create an error message response
		response = {
			'err_message': str(e)
		}
		#return internal server error with code (500)
		return make_response(jsonify(response)), 500

#add request endpoint
@rqst_blueprints .route('/api/v1/requests/', methods = ['POST'])
def add_requests():
	request_container=
	{
		'user': 102,
		'projectid': 101,
		'request_type': 'Maintenance',
		'request_description': 'Ugrade to the latest version.',
		'request_date': '12/23/2017',
		'Approved/Rejected':'Approved',
		'status':'Resolved'
	}
	user_requests.db_requests.append(request_container)
	response = {'result':mainrequests_db.db_requests}
	return make_response(jsonify(response)), 201

#get all requests
@rqst_blueprints .route('/api/v1/requests/', methods = ['GET'])
def get_all_requests():
	response = {'result' : user_requests.db_requests}
	return make_response(jsonify(response)), 200

#get all requests for a specific user
@rqst_blueprints .route('/api/v1/requests/<user_id>', methods = ['GET'])
def get_all_user_requests(user_id):
	rqst = [user_requests for user_requests in db_requests if user_requests['user_id'] == user_id]
	response = {
	'result' : rqst
	}
	return make_response(jsonify(response)), 200

#update the status of a request
@rqst_blueprints .route('/api/v1/requests/<request_id>', methods = ['PUT'])
def update_requests(request_id):
	rqst = [user_requests for user_requests in db_requests if user_requests['request_id'] == request_id]
	rqst[0]['status'] = request.json['status']
	response = {
	'result' : rqst[0]
	}
	return make_response(jsonify(response)), 200

#delete a request
@rqst_blueprints .route('/api/v1/requests/<request_id>', methods = ['DELETE'])
def delete_requests(request_id):
	rqst = [user_requests for user_requests in rqsts if user_requests['request_id'] == request_id]
	rqsts.remove(rqst[0])
	response = {'result' : rqsts}
	return make_response(jsonify(response)), 200
