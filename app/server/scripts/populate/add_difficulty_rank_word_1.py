import sys
sys.path.append('../..')

from data_store.database_driver.mysql_driver import MySqlDriver
from data_object.word_data_object import WordDataObject
from utils.print import ppp

# get all words from table ordered by QWERTY difficulty
# save with additional QWERTY difficulty rank value

db = MySqlDriver(database_name='zentype')

sql = 'SELECT * FROM english_word_1 ORDER BY qwerty_difficulty'

res = db.query(sql)

ppp(res)

