import jwt
from datetime import datetime, timedelta
from flask import current_app

def generate_new_token(email):
	#Generating confirmation token
	try:
		# set up a payload
		# set expiration time to 30 minutes in UTC
		jwt_string = jwt.encode({'user_id' : users.db_users, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, current_app.config.get('SECRET'))
		return jwt_string

	except Exception as e:
		# error returned in string format
		return str(e)

def decode_user_token(token):
	"""Decodes user access token"""
	try:
		# Decode the token using SECRET
		payload = jwt.decode(token, current_app.config.get('SECRET'))
		return payload['sub']
	except jwt.ExpiredSignatureError:
		# return an error string when the token is has expired
		return "Your token has expired."
	except jwt.InvalidTokenError:
		# return an error string for invalid tokens
		return "Your token is invalid."
