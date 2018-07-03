
# Typing Test Service

from service.word import Word


class TypingTest():
	"""
	Typing Test Service

	"""


	def __init__(self, typingTestDO, typingTestContentDOs):
		self.typing_test = typingTestDO
		self.typing_test_content = typingTestContentDOs


	@staticmethod
	def build_wpm_typing_test(
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

		return wordDOs


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
