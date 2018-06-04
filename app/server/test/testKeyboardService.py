
import sys
sys.path.append('..')

from testie import Testie
from service.keyboard import Keyboard
from utils.print import ppp


t = Testie()

keyboard = Keyboard(Keyboard.QWERTY_CONFIG)
for key in keyboard.keyboard_model:
	ppp(key.position)
	ppp(key.finger)
	ppp(key.difficulty)
	ppp(key.primary_char)
	ppp(key.secondary_char)

t.print_report()





