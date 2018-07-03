

from data_object.base_data_object import BaseDataObject
from data_store.database_driver.mysql_driver import MySqlDriver
from data_store.cache_driver.redis_driver import RedisDriver


class WordDataObject(BaseDataObject):
	"""
	Word Data Object

	"""

	LANGUAGE_TYPE_TO_WORD_TABLE = {
		1: 'english_word'
	}
	TABLE_NAME = LANGUAGE_TYPE_TO_WORD_TABLE[1]
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
			language_type = language.get_type()
			cls.TABLE_NAME = cls.LANGUAGE_TYPE_TO_WORD_TABLE[language_type]
		return super().create(
			prop_dict=prop_dict,
			db_driver_class=db_driver_class,
			cache_driver_class=cache_driver_class
		)


	@classmethod
	def find_one(
		cls,
		prop_dict={},
		db_driver_class=None,
		cache_driver_class=None,
		cache_ttl=None,
		language=None
	):
		if language is not None:
			language_type = language.get_type()
			cls.TABLE_NAME = cls.LANGUAGE_TYPE_TO_WORD_TABLE[language_type]
		return super().find_one(
			prop_dict=prop_dict,
			db_driver_class=db_driver_class,
			cache_driver_class=cache_driver_class,
			cache_ttl=cache_ttl
		)

