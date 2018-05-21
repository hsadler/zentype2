

# User Authentication API

from flask import Blueprint, jsonify, request
from flask_jwt_simple import (
	jwt_required, create_jwt, get_jwt_identity
)

from data_store.cache_driver.redis_driver import RedisDriver
from service.user_auth import UserAuth
user_auth_api = Blueprint('user_auth_api', __name__)


@user_auth_api.route('/signup', methods=['POST'])
def signup():
	"""
	Sign-up user for a ZenType account.

	"""

	r = request.get_json()
	user_email = r.get('email', None)
	user_password = r.get('password', None)

	userDO = UserAuth.signup(
		email=user_email,
		password=user_password
	)

	if userDO is not None:
		# if the user was created successfully, give them a jwt token
		token = create_jwt(identity=userDO.to_dict())
		res = {
			'success': True,
			'result': { 'token': token }
		}
	else:
		res = { 'success': False }

	return jsonify(res)


@user_auth_api.route('/login', methods=['POST'])
def login():
	"""
	Login user to ZenType account.

	"""

	# TODO
	r = request.get_json()
	user_email = r['email']
	user_password = r['password']
	res = {
		'success': True,
		'result': {
			'message': 'user has been logged in',
			'email': user_email,
			'password': user_password
		}
	}
	return jsonify(res)


# TODO: DON'T THINK THIS IS NEEDED
# @user_auth_api.route('/validate-token', methods=['POST'])
# def validate_token():
# 	"""
# 	Validate user's token for authentication.

# 	"""

# 	# TODO
# 	r = request.get_json()
# 	user_token = r['token']
# 	res = {
# 		'success': True,
# 		'result': {
# 			'message': 'user\'s token has been validated',
# 			'token': user_token
# 		}
# 	}
# 	return jsonify(res)


# test jwt
@user_auth_api.route('/protected', methods=['GET'])
@jwt_required
def protected():
	# Access the identity of the current user with get_jwt_identity
	return jsonify({'hello_from': get_jwt_identity()}), 200



