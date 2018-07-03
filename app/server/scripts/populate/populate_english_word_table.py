import sys
sys.path.append('../..')

from data_object.word_data_object import WordDataObject
from service.keyboard import Keyboard
from service.language import Language
from utils.print import ppp


keyboard = Keyboard(Keyboard.QWERTY, Language.ENGLISH)


with open('../../sources/word_sources/number27.org/words_90K.txt', 'r') as file:
	for line_index, line in enumerate(file):
		parts = [x.strip('() ') for x in line.split(',')]
		word_props = {
			'text': parts[0],
			'length': len(parts[0]),
			'frequency': float(parts[1]),
			'frequency_rank': line_index + 1,
			'qwerty_difficulty': keyboard.get_keyboard_difficulty_for_word(
				parts[0],
				round_to_int=True
			)
		}
		wordDO = WordDataObject.create(
			prop_dict=word_props,
			language=WordDataObject.ENGLISH
		)
		res = wordDO.save()
		ppp(res.to_dict())


