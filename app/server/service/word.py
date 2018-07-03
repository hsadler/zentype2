
# Word Service

import config.config as config
from data_store.database_driver.mysql_driver import MySqlDriver
from data_object.word_data_object import WordDataObject
from service.language import Language


class Word():
	"""
	Word Service

	"""


	@staticmethod
	def get_random_list(
		language,
		qwerty_difficulty_rank=None,
		frequency_rank=None,
		length=None,
		substring=None,
		limit=None,
	):

		mysql_driver = MySqlDriver(database_name=config.MYSQL_DB_NAME)

		sql_parts = []
		bind_vars = {}

		# select component
		table_name = WordDataObject\
			.LANGUAGE_TYPE_TO_WORD_TABLE[language.get_type()]
		sql_parts.append('SELECT * FROM {0}'.format(table_name))

		# where clause components
		where_parts = []
		where_range_vals = {
			'qwerty_difficulty_rank': qwerty_difficulty_rank,
			'frequency_rank': frequency_rank,
			'length': length
		}
		for k, v in where_range_vals.items():
			if v is not None:
				if 'min' in v:
					where_parts.append('{0} > %({0}_min)s'.format(k))
					bind_vars['{0}_min'.format(k)] = v['min']
				if 'max' in v:
					where_parts.append('{0} < %({0}_max)s'.format(k))
					bind_vars['{0}_max'.format(k)] = v['max']
		if substring is not None:
			where_parts.append('text LIKE %(substring)s')
			bind_vars['substring'] = '%{0}%'.format(substring)
		sql_parts.append('WHERE {0}'.format(' AND '.join(where_parts)))

		# limit component
		if limit is not None:
			sql_parts.append('LIMIT %(limit)s')
			bind_vars['limit'] = limit

		sql = ' '.join(sql_parts)

		result = mysql_driver.query_bind(sql, bind_vars)
		wordDOs = [
			WordDataObject.create(prop_dict=x, language=language)
			for x in result
		]
		return wordDOs

