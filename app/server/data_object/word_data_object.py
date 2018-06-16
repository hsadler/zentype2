

from data_object.base_data_object import BaseDataObject
from data_store.database_driver.mysql_driver import MySqlDriver
from data_store.cache_driver.redis_driver import RedisDriver


class WordDataObject(BaseDataObject):
	"""
	Word Data Object

	"""

	ENGLISH_1 = 'english_word_1'
	ENGLISH_2 = 'english_word_2'

	TABLE_NAME = ENGLISH_1
	DEFAULT_DB_DRIVER_CLASS = MySqlDriver
	DEFAULT_CACHE_DRIVER_CLASS = RedisDriver
	DEFAULT_CACHE_TTL = 3600


	@classmethod
	def create(
		cls,
		prop_dict={},
		db_driver_class=None,
		cache_driver_class=None,
		language=None
	):
		if language is not None:
			cls.TABLE_NAME = language
		return super().create(
			prop_dict=prop_dict,
			db_driver_class=db_driver_class,
			cache_driver_class=cache_driver_class
		)
