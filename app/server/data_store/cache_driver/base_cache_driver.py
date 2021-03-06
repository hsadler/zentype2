
# Base Cache Driver

from abc import ABCMeta, abstractmethod


class BaseCacheDriver(metaclass=ABCMeta):
	"""
	Provides interface for all proper cache drivers.
	"""


	@abstractmethod
	def __init__(self):
		pass


	########## CRUD INTERFACE METHODS ##########

	@abstractmethod
	def set(self, key, value, ttl=None):
		pass

	@abstractmethod
	def get(self, key):
		pass

	@abstractmethod
	def delete(self, key):
		pass