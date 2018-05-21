

from data_object.base_data_object import BaseDataObject
from data_store.database_driver.mysql_driver import MySqlDriver
from data_store.cache_driver.redis_driver import RedisDriver


class UserDataObject(BaseDataObject):
	"""
	User Data Object

	"""


	TABLE_NAME = 'user'
	DEFAULT_DB_DRIVER_CLASS = MySqlDriver
	DEFAULT_CACHE_DRIVER_CLASS = RedisDriver
	DEFAULT_CACHE_TTL = 3600


	@classmethod
	def find_by_email(
		cls,
		email,
		db_driver_class=None,
		cache_driver_class=None,
		cache_ttl=None
	):
		"""
		TODO: find a better way to cache gets by any column
		(private method?)

		"""

		db_driver, cache_driver = cls.get_drivers(
			db_driver_class=db_driver_class,
			cache_driver_class=cache_driver_class
		)

		cache_key = '{0}_email={1}'.format(cls.TABLE_NAME, email)
		cached_value = cache_driver.get(cache_key)
		userDO = None

		if cached_value is not None:
			userDO = cls(
				prop_dict=cached_value,
				db_driver_class=db_driver_class,
				cache_driver_class=cache_driver_class
			)
		else:
			find_props = { 'email': email }
			userDO = cls.find_one(
				prop_dict=find_props,
				db_driver_class=db_driver_class,
				cache_driver_class=cache_driver_class
			)
			if userDO is not None:
				ttl = cache_ttl if cache_ttl is not None \
				else cls.DEFAULT_CACHE_TTL
				cache_driver.set(
					key=cache_key,
					value=userDO.to_dict(),
					ttl=ttl
				)

		return userDO


