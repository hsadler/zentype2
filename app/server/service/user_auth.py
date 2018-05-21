
# User Authentication Service

import sys
import hashlib
import config.config_secrets as config_secrets

from data_object.user_data_object import UserDataObject


class UserAuth():
	"""
	User Authentication Service

	"""


	@classmethod
	def create_new_user(cls, email, password):

		# attempt to find existing user by email
		find_props = { 'email': email }
		# TODO: optimize with find_by_email() method
		existing_userDO = UserDataObject.find_one(prop_dict=find_props)
		if existing_userDO is not None:
			return None

		# only create user if one doesn't already exist with given email
		hashed_password = cls.__get_hashed_password(password=password)
		create_props = {
			'email': email,
			'password_hash': hashed_password
		}
		userDO = UserDataObject.create(prop_dict=create_props)
		userDO = userDO.save()
		return userDO


	@classmethod
	def find_user_and_validate_password(cls, email, password):

		# attempt to find user by email
		find_props = { 'email': email }
		# TODO: optimize with find_by_email() method
		userDO = UserDataObject.find_one(prop_dict=find_props)

		# if user exists, compare hashed passwords
		if userDO is not None:
			hashed_password = cls.__get_hashed_password(password=password)
			if hashed_password == userDO.get_prop('password_hash'):
				return userDO

		return None


	########## PRIVATE HELPERS ##########


	@staticmethod
	def __get_hashed_password(password):
		salted_password = '{0}{1}'.format(
			password,
			config_secrets.PASSWORD_SALT
		).encode('utf-8')
		return hashlib.sha512(salted_password).hexdigest()

