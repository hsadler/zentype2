
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

# create english_word table
# create_table_query = """
# 	CREATE TABLE IF NOT EXISTS english_word (
# 		id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
# 		created_ts INT(11) NOT NULL,
# 		updated_ts INT(11) NOT NULL,
# 		# table specific columns here:
# 		text VARCHAR(100) NOT NULL UNIQUE,
# 		length INT(3) UNSIGNED,
# 		frequency DECIMAL(8, 6),
# 		frequency_rank INT(11) UNSIGNED,
# 		qwerty_difficulty INT(11) UNSIGNED,
# 		qwerty_difficulty_rank INT(11) UNSIGNED
# 	)
# """

# create typing_test table
# create_table_query = """
# 	CREATE TABLE IF NOT EXISTS typing_test (
# 		id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
# 		created_ts INT(11) NOT NULL,
# 		updated_ts INT(11) NOT NULL,
# 		# table specific columns here:
# 		language INT(3) UNSIGNED NOT NULL,
# 		word_count INT(4) UNSIGNED NOT NULL,
# 		min_word_length INT(3) UNSIGNED NOT NULL,
# 		max_word_length INT(3) UNSIGNED NOT NULL,
# 		avg_word_length INT(3) UNSIGNED NOT NULL,
# 		min_word_frequency_rank INT(11) UNSIGNED NOT NULL,
# 		max_word_frequency_rank INT(11) UNSIGNED NOT NULL,
# 		avg_word_frequency_rank INT(11) UNSIGNED NOT NULL,
# 		min_word_qwerty_difficulty_rank INT(11) UNSIGNED NOT NULL,
# 		max_word_qwerty_difficulty_rank INT(11) UNSIGNED NOT NULL,
# 		avg_word_qwerty_difficulty_rank INT(11) UNSIGNED NOT NULL
# 	)
# """

# create typing_test_content table
# create_table_query = """
# 	CREATE TABLE IF NOT EXISTS typing_test_content (
# 		id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
# 		created_ts INT(11) NOT NULL,
# 		updated_ts INT(11) NOT NULL,
# 		# table specific columns here:
# 		typing_test_id INT(6) UNSIGNED NOT NULL,
# 		word_id INT(6) UNSIGNED NOT NULL,
# 		position INT(4) UNSIGNED NOT NULL
# 	)
# """

# create user_typing_test table
# create_table_query = """
# 	CREATE TABLE IF NOT EXISTS user_typing_test (
# 		id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
# 		created_ts INT(11) NOT NULL,
# 		updated_ts INT(11) NOT NULL,
# 		# table specific columns here:
# 		typing_test_id INT(6) UNSIGNED NOT NULL,
# 		user_id INT(6) UNSIGNED NOT NULL,
# 		status TINYINT(1) UNSIGNED NOT NULL,
# 		test_time INT(4) UNSIGNED,
# 		wpm INT(3) UNSIGNED
# 	)
# """

# create user_typing_test_content table
# create_table_query = """
# 	CREATE TABLE IF NOT EXISTS user_typing_test_content (
# 		id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
# 		created_ts INT(11) NOT NULL,
# 		updated_ts INT(11) NOT NULL,
# 		# table specific columns here:
# 		user_typing_test_id INT(6) UNSIGNED NOT NULL,
# 		word_id INT(6) UNSIGNED NOT NULL,
# 		position INT(4) UNSIGNED NOT NULL,
# 		attempted TINYINT(1) UNSIGNED,
# 		completed_correctly TINYINT(1) UNSIGNED,
# 		completion_time INT(4)
# 	)
# """

query_result = mysql_driver.query(query_string=create_table_query)

ppp(['result of create table query:', query_result])
