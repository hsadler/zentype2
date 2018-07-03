
import sys
sys.path.append('..')

from service.language import Language
from utils.print import ppp


language = Language(Language.ENGLISH)

ppp('language type: {}'.format(language.get_type()))
ppp('language letter frequency for "J": {}'.format(
	language.get_letter_frequency('J')
))

