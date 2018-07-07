
import sys
sys.path.append('..')

from data_object.typing_test_data_object import TypingTestDataObject
from service.typing_test import TypingTest
from service.language import Language
from utils.print import ppp

typing_test_DO = TypingTestDataObject.find_one(prop_dict={
	'id': 1
})

ppp(typing_test_DO.to_dict())

