

# User Authentication API

from flask import Blueprint, jsonify, request
from flask_jwt_simple import (
	jwt_optional,
	create_jwt,
	get_jwt_identity
)

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

	userDO = UserAuth.create_new_user(
		email=user_email,
		password=user_password
	)

	if userDO is not None:
		# if the user was created successfully, give them a jwt token
		token = get_encode_auth_token(userDO=userDO)
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

	r = request.get_json()
	user_email = r.get('email', None)
	user_password = r.get('password', None)

	userDO = UserAuth.find_user_and_validate_password(
		email=user_email,
		password=user_password
	)

	if userDO is not None:
		# if the user was created successfully, give them a jwt token
		token = get_encode_auth_token(userDO=userDO)
		res = {
			'success': True,
			'result': { 'token': token }
		}
	else:
		res = { 'success': False }

	return jsonify(res)


@user_auth_api.route('/refresh-token', methods=['GET'])
@jwt_optional
def refresh_token():
	"""
	Refresh user's token.

	"""

	identity = get_jwt_identity()

	if identity is not None:
		new_token = create_jwt(identity=get_jwt_identity())
		res = {
			'success': True,
			'result': { 'token': new_token }
		}
	else:
		res = {
			'success': False
		}
	return jsonify(res)


########## PRIVATE HELPERS ##########


def get_encode_auth_token(userDO):
	# TODO: decide what we want to encode into the token (more or less data?)
	return create_jwt(identity=userDO.to_dict())

