
import sys
sys.path.append('..')

import config.config as config
from data_store.database_driver.mysql_driver import MySqlDriver
from utils.print import ppp


mysql_driver = MySqlDriver(
	database_name=config.MYSQL_DB_NAME
)

# create user table
# create_table_query = """
# 	CREATE TABLE IF NOT EXISTS user (
# 		id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
# 		created_ts INT(11) NOT NULL,
# 		updated_ts INT(11) NOT NULL,
# 		# table specific columns here:
# 		email VARCHAR(255) NOT NULL UNIQUE,
# 		password_hash VARCHAR(255) NOT NULL
# 	)
# """

# create english_word_1 table
# create_table_query = """
# 	CREATE TABLE IF NOT EXISTS english_word_1 (
# 		id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
# 		created_ts INT(11) NOT NULL,
# 		updated_ts INT(11) NOT NULL,
# 		# table specific columns here:
# 		text VARCHAR(100) NOT NULL UNIQUE,
# 		length INT(3),
# 		frequency DECIMAL(8, 6),
# 		frequency_rank INT(11),
# 		qwerty_difficulty INT(11),
# 		qwerty_difficulty_rank INT(11)
# 	)
# """

# create english_word_2 table
# create_table_query = """
# 	CREATE TABLE IF NOT EXISTS english_word_2 (
# 		id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
# 		created_ts INT(11) NOT NULL,
# 		updated_ts INT(11) NOT NULL,
# 		# table specific columns here:
# 		text VARCHAR(100) NOT NULL,
# 		length INT(3),
# 		part_of_speech VARCHAR(50),
# 		frequency INT(11),
# 		frequency_rank INT(11),
# 		qwerty_difficulty INT(11),
# 		qwerty_difficulty_rank INT(11)
# 	)
# """

query_result = mysql_driver.query(query_string=create_table_query)

ppp(['result of create table query:', query_result])
