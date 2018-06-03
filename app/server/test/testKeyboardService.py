
import sys
sys.path.append('..')

from testie import Testie
from service.keyboard import Keyboard
from utils.print import ppp


t = Testie()

keyboard = Keyboard(Keyboard.QWERTY_CONFIG)
ppp(keyboard.keyboard_config)
ppp(keyboard.keyboard_model)

t.print_report()





