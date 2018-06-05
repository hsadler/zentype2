
import sys
sys.path.append('..')

from testie import Testie
from service.keyboard import Keyboard
from service.language import Language
from utils.print import ppp


# t = Testie()

keyboard = Keyboard(Keyboard.QWERTY, Language.ENGLISH)
for key in keyboard.keyboard_model:
	ppp(key.to_dict())

lingo = Language(Language.ENGLISH)
ppp(lingo.letter_frequencies)

text = 'word'
for ch in text:
	key = keyboard.get_key_from_character(ch)
	ppp(key.to_dict())


# t.print_report()








