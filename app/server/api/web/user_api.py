

# User API

from flask import Blueprint, jsonify, request
from flask_jwt_simple import (
	jwt_required,
	get_jwt_identity
)

from service.user import User


user_api = Blueprint('user_api', __name__)


@user_api.route('/user-data', methods=['GET'])
@jwt_required
def user_data():
	"""
	Get api formatted user data.

	TODO: implement from this stub

	"""

	# TESTING: display the user identity
	identity = get_jwt_identity()
	return jsonify(identity)

	# userDO = UserAuth.create_new_user(
	# 	email=user_email,
	# 	password=user_password
	# )

	# if userDO is not None:
	# 	# if the user was created successfully, give them a jwt token
	# 	token = get_encode_auth_token(userDO=userDO)
	# 	res = {
	# 		'success': True,
	# 		'result': { 'token': token }
	# 	}
	# else:
	# 	res = { 'success': False }

	# return jsonify(res)

