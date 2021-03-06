
import sys
sys.path.append('..')

from data_object.word_data_object import WordDataObject
from service.word import Word
from service.language import Language
from utils.print import ppp


# random word list options
language = Language(Language.ENGLISH)
qwerty_difficulty_rank = {
	'min': 0,
	'max': 10000
}
frequency_rank = {
	'min': 0,
	'max': 10000
}
length = {
	'min': 0,
	'max': 100
}
substring = 'ba'
limit = 10

word_list = Word.get_random_list(
	language=language,
	qwerty_difficulty_rank=qwerty_difficulty_rank,
	frequency_rank=frequency_rank,
	length=length,
	substring=substring,
	limit=limit
)

ppp(word_list)
for wordDO in word_list:
	ppp(wordDO.to_dict())
ppp("length: {0}".format(len(word_list)))

