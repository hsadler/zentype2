

# Typing Test API

from flask import Blueprint, jsonify, request
from flask_jwt_simple import (
	jwt_required,
	get_jwt_identity
)


typing_test_api = Blueprint('typing_test_api', __name__)


@typing_test_api.route('/get-wpm-test', methods=['GET'])
@jwt_required
def get_wpm_test():
	"""
	Get a WPM typing test.

	"""

	res = { message: 'here is your test...' }

	return jsonify(res)


@typing_test_api.route('/submit-wpm-test', methods=['POST'])
@jwt_required
def submit_wpm_test():
	"""
	Submit a WPM typing test.

	"""

	res = { message: 'your test has been submitted...' }

	return jsonify(res)

