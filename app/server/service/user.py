
# User Service

from data_object.user_data_object import UserDataObject


class User():
	"""
	User Service

	"""


	def get_user_data_by_id(user_id):

		userDO = UserDataObject.find_one(prop_dict={ 'id': user_id })

		return userDO.to_dict()



