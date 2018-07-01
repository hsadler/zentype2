

from data_object.base_data_object import BaseDataObject
from data_store.database_driver.mysql_driver import MySqlDriver
from data_store.cache_driver.redis_driver import RedisDriver


class UserTypingTestDataObject(BaseDataObject):
	"""
	User Typing Test Data Object

	"""


	TABLE_NAME = 'user_typing_test'
	DEFAULT_DB_DRIVER_CLASS = MySqlDriver
	DEFAULT_CACHE_DRIVER_CLASS = RedisDriver
	DEFAULT_CACHE_TTL = 3600
