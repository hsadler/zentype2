
import sys
sys.path.append('..')

from data_object.word_data_object import WordDataObject
from service.language import Language
from utils.print import ppp


language = Language(Language.ENGLISH)

wordDO = WordDataObject.find_one(
	prop_dict={ 'id': 10 },
	language=language
)


ppp(wordDO.to_dict())

