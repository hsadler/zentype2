

# Typing Test API

from flask import Blueprint, jsonify, request
from flask_jwt_simple import (
	jwt_required,
	get_jwt_identity
)


typing_test_api = Blueprint('typing_test_api', __name__)


@typing_test_api.route('/test', methods=['GET'])
@jwt_required
def test():
	"""
	Test API endpoint.

	"""

	res = { message: 'hi there' }

	return jsonify(res)

