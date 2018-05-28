

# User API

from flask import Blueprint, jsonify, request
from flask_jwt_simple import (
	jwt_required,
	get_jwt_identity
)

from service.user import User


user_api = Blueprint('user_api', __name__)


@user_api.route('/get-data', methods=['GET'])
@jwt_required
def get_data():
	"""
	Get api formatted user data.

	"""

	user_data = get_jwt_identity()

	api_formatted_user_data = {}
	allowed_keys = ['email']
	for key in allowed_keys:
		api_formatted_user_data[key] = user_data[key]

	res = {
		'success': True,
		'result': { 'user_data': api_formatted_user_data }
	}

	return jsonify(res)

