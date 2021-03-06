import sys
sys.path.append('../..')

from data_store.database_driver.mysql_driver import MySqlDriver
from data_object.word_data_object import WordDataObject
from service.language import Language
from utils.print import ppp

# get all words from table ordered by QWERTY difficulty
# save with additional QWERTY difficulty rank value

db = MySqlDriver(database_name='zentype')
sql = 'SELECT * FROM english_word ORDER BY qwerty_difficulty'
word_datas = db.query(sql)

language = Language(Language.ENGLISH)
curr_difficulty_rank = 1

for word_data in word_datas:
	word_data['qwerty_difficulty_rank'] = curr_difficulty_rank
	word_DO = WordDataObject.create(
		prop_dict=word_data,
		language=language
	)
	save_res = word_DO.save()
	ppp(save_res)
	curr_difficulty_rank = curr_difficulty_rank + 1

ppp('All done!')
