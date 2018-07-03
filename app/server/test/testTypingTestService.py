
import sys
sys.path.append('..')

from service.typing_test import TypingTest
from service.language import Language
from utils.print import ppp


language = Language(Language.ENGLISH)

word_qwerty_difficulty_rank = {
	'min': 0,
	'max': 10000
}
word_frequency_rank = {
	'min': 0,
	'max': 10000
}
word_length = {
	'min': 0,
	'max': 100
}
word_count = 10

typing_test = TypingTest.build_wpm_typing_test_from_random_words(
	language=language,
	word_qwerty_difficulty_rank=word_qwerty_difficulty_rank,
	word_frequency_rank=word_frequency_rank,
	word_length=word_length,
	word_count=word_count,
)

ppp(typing_test)

