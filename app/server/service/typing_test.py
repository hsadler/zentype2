
# Typing Test Service

from data_object.typing_test_data_object import TypingTestDataObject
from data_object.typing_test_content_data_object \
	import TypingTestContentDataObject
from service.word import Word


class TypingTest():
	"""
	Typing Test Service

	"""


	def __init__(self, typingTestDO, typingTestContentDOs):
		self.typing_test = typingTestDO
		self.typing_test_content = typingTestContentDOs


	@classmethod
	def build_wpm_typing_test(
		cls,
		language,
		word_qwerty_difficulty_rank=None,
		word_frequency_rank=None,
		word_length=None,
		word_count=None,
	):
		# TODO:
			# get random words
			# calculate attributes for typing test
			# instantiate TypingTestDO
			# instantiate typingTestContentDOs
			# instantiate TypingTest with TypingTestDO and TypingTestContentDOs

		wordDOs = Word.get_random_list(
			language=language,
			qwerty_difficulty_rank=word_qwerty_difficulty_rank,
			frequency_rank=word_frequency_rank,
			length=word_length,
			limit=word_count,
		)

		#### word:
		# | text                   | varchar(100)
		# | length                 | int(3)
		# | frequency              | decimal(8,6)
		# | frequency_rank         | int(11)
		# | qwerty_difficulty      | int(11)
		# | qwerty_difficulty_rank | int(11)

		word_lengths = [
			wordDO.get_prop('length')
			for wordDO in wordDOs
		]
		word_frequency_ranks = [
			wordDO.get_prop('frequency_rank')
			for wordDO in wordDOs
		]
		word_qwerty_difficulty_ranks = [
			wordDO.get_prop('qwerty_difficulty_rank')
			for wordDO in wordDOs
		]

		#### typing test:
		# | language                        | int(3)
		# | word_count                      | int(4)
		# | min_word_length                 | int(3)
		# | max_word_length                 | int(3)
		# | avg_word_length                 | int(3)
		# | min_word_frequency_rank         | int(11)
		# | max_word_frequency_rank         | int(11)
		# | avg_word_frequency_rank         | int(11)
		# | min_word_qwerty_difficulty_rank | int(11)
		# | max_word_qwerty_difficulty_rank | int(11)
		# | avg_word_qwerty_difficulty_rank | int(11)


		# create and save the typing test
		typing_test_props = {
			'language': language.get_type(),
			'word_count': len(wordDOs),
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
		typingTestDO = TypingTestDataObject.create(
			prop_dict=typing_test_props
		)
		typingTestDO = typingTestDO.save()

		# create and save the typing test content items
		typing_test_content = []
		for idx, wordDO in enumerate(wordDOs):
			ttc_props = {
				'typing_test_id': typingTestDO.get_prop('id'),
				'word_id': wordDO.get_prop('id'),
				'position': idx
			}
			ttcDO = TypingTestContentDataObject.create(prop_dict=ttc_props)
			ttcDO.save()
			typing_test_content.append(ttcDO)

		return cls(
			typingTestDO=typingTestDO,
			typingTestContentDOs=typing_test_content
		)


	@staticmethod
	def get_prebuilt_wpm_typing_test(
		language
	):
		# TODO: stub
			# - add more args
		pass


	@staticmethod
	def process_wpm_typing_test_for_user(testDO, userDO):
		# TODO: stub
		pass
