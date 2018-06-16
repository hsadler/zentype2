import sys
sys.path.append('../..')

from data_object.word_data_object import WordDataObject
from service.keyboard import Keyboard
from service.language import Language
from utils.print import ppp


keyboard = Keyboard(Keyboard.QWERTY, Language.ENGLISH)

with open('../../sources/word_sources/word_frequency/word_frequency_5000.txt', 'r') as file:
	for line_index, line in enumerate(file):
		if line_index > 0:
			parts = [x.strip(' ') for x in line.split()]
			word_props = {
				'text': parts[1],
				'length': len(parts[1]),
				'part_of_speech': parts[2],
				'frequency': int(parts[3]),
				'frequency_rank': int(parts[0]),
				'qwerty_difficulty': keyboard.get_keyboard_difficulty_for_word(
					parts[1],
					round_to_int=True
				)
			}
			wordDO = WordDataObject.create(
				prop_dict=word_props,
				language=WordDataObject.ENGLISH_2
			)
			res = wordDO.save()
			ppp(res.to_dict())


