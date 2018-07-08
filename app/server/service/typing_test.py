
# Typing Test Service

from data_object.typing_test_data_object import TypingTestDataObject
from data_object.typing_test_content_data_object \
	import TypingTestContentDataObject
from service.word import Word


class TypingTest():
	"""
	Typing Test Service. Builds typing tests from random word lists. Loads pre-
	existing typing tests. Processes typing tests for users.

	"""


	def __init__(self, typing_test_DO, typing_test_content_DOs):
		self.typing_test = typing_test_DO
		self.typing_test_content = typing_test_content_DOs


	############################################################################
	# WPM TYPING TESTS
	############################################################################

	@classmethod
	def build_and_save_wpm_typing_test(
		cls,
		language,
		word_qwerty_difficulty_rank=None,
		word_frequency_rank=None,
		word_length=None,
		word_count=None,
	):

		word_DOs = Word.get_random_list(
			language=language,
			qwerty_difficulty_rank=word_qwerty_difficulty_rank,
			frequency_rank=word_frequency_rank,
			length=word_length,
			limit=word_count,
		)

		word_lengths = [
			word_DO.get_prop('length')
			for word_DO in word_DOs
		]
		word_frequency_ranks = [
			word_DO.get_prop('frequency_rank')
			for word_DO in word_DOs
		]
		word_qwerty_difficulty_ranks = [
			word_DO.get_prop('qwerty_difficulty_rank')
			for word_DO in word_DOs
		]

		# create and save the typing test
		typing_test_props = {
			'language': language.get_type(),
			'word_count': len(word_DOs),
			'min_word_length': min(word_lengths),
			'max_word_length': max(word_lengths),
			'avg_word_length': int(sum(word_lengths) / len(word_lengths)),
			'min_word_frequency_rank': min(word_frequency_ranks),
			'max_word_frequency_rank': max(word_frequency_ranks),
			'avg_word_frequency_rank': \
				int(sum(word_frequency_ranks) / len(word_frequency_ranks)),
			'min_word_qwerty_difficulty_rank': \
				min(word_qwerty_difficulty_ranks),
			'max_word_qwerty_difficulty_rank': \
				max(word_qwerty_difficulty_ranks),
			'avg_word_qwerty_difficulty_rank': \
				int(
					sum(word_qwerty_difficulty_ranks) / \
					len(word_qwerty_difficulty_ranks)
				)
		}
		typing_test_DO = TypingTestDataObject.create(
			prop_dict=typing_test_props
		)
		typing_test_DO = typing_test_DO.save()

		# create and save the typing test content items
		typing_test_content = []
		for idx, word_DO in enumerate(word_DOs):
			ttc_props = {
				'typing_test_id': typing_test_DO.get_prop('id'),
				'word_id': word_DO.get_prop('id'),
				'position': idx
			}
			ttc_DO = TypingTestContentDataObject.create(prop_dict=ttc_props)
			ttc_DO = ttc_DO.save()
			typing_test_content.append(ttc_DO)

		return cls(
			typing_test_DO=typing_test_DO,
			typing_test_content_DOs=typing_test_content
		)


	@staticmethod
	def load_wpm_typing_test_by_id(id):
		# TODO: stub
		pass


	@staticmethod
	def load_prebuilt_wpm_typing_test(
		language
	):
		# TODO: stub
			# - add more args
			# 'word_count': len(wordDOs),
			# 'min_word_length': min(word_lengths),
			# 'max_word_length': max(word_lengths),
			# 'avg_word_length': int(sum(word_lengths) / len(word_lengths)),
			# 'min_word_frequency_rank': min(word_frequency_ranks),
			# 'max_word_frequency_rank': max(word_frequency_ranks),
			# 'avg_word_frequency_rank': \
			# 	int(sum(word_frequency_ranks) / len(word_frequency_ranks)),
			# 'min_word_qwerty_difficulty_rank': \
			# 	min(word_qwerty_difficulty_ranks),
			# 'max_word_qwerty_difficulty_rank': \
			# 	max(word_qwerty_difficulty_ranks),
			# 'avg_word_qwerty_difficulty_rank': \
			# 	int(
			# 		sum(word_qwerty_difficulty_ranks) / \
			# 		len(word_qwerty_difficulty_ranks)
			# 	)
		pass


	############################################################################
	# USER WPM TEST PROCESSING
	############################################################################

	@staticmethod
	def create_wpm_typing_test_for_user(typing_test_DO, user_DO):
		# TODO: stub
		pass


	@staticmethod
	def process_wpm_typing_test_for_user(typing_test_DO, user_DO):
		# TODO: stub
		pass

