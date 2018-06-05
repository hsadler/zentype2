
# Keyboard Service

from service.language import Language


class Keyboard():
	"""
	Keyboard Service. Provides a keyboard model and methods based on key layout
	and language configurations.

	"""


	# fingers

	LEFT_PINKY = 'LP'
	LEFT_RING = 'LR'
	LEFT_MIDDLE = 'LM'
	LEFT_INDEX = 'LI'
	LEFT_THUMB = 'LT'

	THUMB = 'T'

	RIGHT_THUMB = 'RT'
	RIGHT_INDEX = 'RI'
	RIGHT_MIDDLE = 'RM'
	RIGHT_RING = 'RR'
	RIGHT_PINKY = 'RP'


	class Key():
		def __init__(
			self,
			position,
			finger,
			difficulty=None,
			primary_char=None,
			secondary_char=None,
		):
			self.position = position
			self.finger = finger
			self.difficulty = difficulty
			self.primary_char = primary_char
			self.secondary_char = secondary_char
		def get_finger(self):
			return self.finger
		def set_difficulty(self, difficulty):
			self.difficulty = difficulty
		def get_difficulty(self):
			return self.difficulty
		def set_characters(self, primary_char, secondary_char):
			self.primary_char = primary_char
			self.secondary_char = secondary_char
		def get_characters(self):
			return {
				'primary': self.primary_char,
				'secondary': self.secondary_char
			}
		def to_dict(self):
			return {
				'position': self.position,
				'finger': self.finger,
				'difficulty': self.difficulty,
				'primary_char': self.primary_char,
				'secondary_char': self.secondary_char
			}


	# base keyboard model

	BASE_KEYBOARD_MODEL = [
		# 1st row
		Key([0,0], LEFT_PINKY, None), # ['`','~']
		Key([0,1], LEFT_PINKY, None), # ['1','!']
		Key([0,2], LEFT_RING, None), # ['2','@']
		Key([0,3], LEFT_MIDDLE, None), # ['3','#']
		Key([0,4], LEFT_INDEX, None), # ['4','$']
		Key([0,5], LEFT_INDEX, None), # ['5','%']
		Key([0,6], RIGHT_INDEX, None), # ['6','^']
		Key([0,7], RIGHT_INDEX, None), # ['7','&']
		Key([0,8], RIGHT_MIDDLE, None), # ['8','*']
		Key([0,9], RIGHT_RING, None), # ['9','(']
		Key([0,10], RIGHT_PINKY, None), # ['0',')']
		Key([0,11], RIGHT_PINKY, None), # ['-','_']
		Key([0,12], RIGHT_PINKY, None), # ['=','+']
		Key([0,13], RIGHT_PINKY, None), # ['delete']
		# 2nd row
		Key([1,0], LEFT_PINKY, None), # ['tab']
		Key([1,1], LEFT_PINKY, 2.75), # ['q','Q']
		Key([1,2], LEFT_RING, 1.5), # ['w','W']
		Key([1,3], LEFT_MIDDLE, 1.5), # ['e','E']
		Key([1,4], LEFT_INDEX, 1.5), # ['r','R']
		Key([1,5], LEFT_INDEX, 2.5), # ['t','T']
		Key([1,6], RIGHT_INDEX, 2.5), # ['y','Y']
		Key([1,7], RIGHT_INDEX, 1.5), # ['u','U']
		Key([1,8], RIGHT_MIDDLE, 1.5), # ['i','I']
		Key([1,9], RIGHT_RING, 1.5), # ['o','O']
		Key([1,10], RIGHT_PINKY, 2.75), # ['p','P']
		Key([1,11], RIGHT_PINKY, None), # ['[','{']
		Key([1,12], RIGHT_PINKY, None), # [']','}']
		Key([1,13], RIGHT_PINKY, None), # ['\\', '|']
		# 3rd row
		Key([2,0], LEFT_PINKY, None), # ['capslock']
		Key([2,1], LEFT_PINKY, 1), # ['a','A']
		Key([2,2], LEFT_RING, 1), # ['s','S']
		Key([2,3], LEFT_MIDDLE, 1), # ['d','D']
		Key([2,4], LEFT_INDEX, 1), # ['f','F']
		Key([2,5], LEFT_INDEX, 1.75), # ['g','G']
		Key([2,6], RIGHT_INDEX, 1.75), # ['h','H']
		Key([2,7], RIGHT_INDEX, 1), # ['j','J']
		Key([2,8], RIGHT_MIDDLE, 1), # ['k','K']
		Key([2,9], RIGHT_RING, 1), # ['l','L']
		Key([2,10], RIGHT_PINKY, None), # [';',':']
		Key([2,11], RIGHT_PINKY, None), # ['\'','"']
		Key([2,12], RIGHT_PINKY, None), # ['return']
		# 4th row
		Key([3,0], LEFT_PINKY, None), # ['left shift']
		Key([3,1], LEFT_PINKY, 2.75), # ['z','Z']
		Key([3,2], LEFT_RING, 2.75), # ['x','X']
		Key([3,3], LEFT_MIDDLE, 2), # ['c','C']
		Key([3,4], LEFT_INDEX, 2), # ['v','V']
		Key([3,5], LEFT_INDEX, 3), # ['b','B']
		Key([3,6], RIGHT_INDEX, 2), # ['n','N']
		Key([3,7], RIGHT_INDEX, 2), # ['m','M']
		Key([3,8], RIGHT_MIDDLE, None), # [',','<']
		Key([3,9], RIGHT_RING, None), # ['.','>']
		Key([3,10], RIGHT_PINKY, None), # ['/','?']
		Key([3,11], RIGHT_PINKY, None), # ['right shift']
		# 5th row
		Key([4,0], LEFT_PINKY, None), # ['left fn']
		Key([4,1], LEFT_PINKY, None), # ['left control']
		Key([4,2], LEFT_THUMB, None), # ['left option']
		Key([4,3], LEFT_THUMB, None), # ['left command']
		Key([4,4], THUMB, None), # ['spacebar']
		Key([4,5], RIGHT_THUMB, None), # ['right command']
		Key([4,6], RIGHT_PINKY, None) # ['right option']
	]


	# keyboard layouts

	QWERTY = [
		# 1st row
		['`','~'],
		['1','!'],
		['2','@'],
		['3','#'],
		['4','$'],
		['5','%'],
		['6','^'],
		['7','&'],
		['8','*'],
		['9','('],
		['0',')'],
		['-','_'],
		['=','+'],
		['delete'],
		# 2nd row
		['tab'],
		['q','Q'],
		['w','W'],
		['e','E'],
		['r','R'],
		['t','T'],
		['y','Y'],
		['u','U'],
		['i','I'],
		['o','O'],
		['p','P'],
		['[','{'],
		[']','}'],
		['\\', '|'],
		# 3rd row
		['capslock'],
		['a','A'],
		['s','S'],
		['d','D'],
		['f','F'],
		['g','G'],
		['h','H'],
		['j','J'],
		['k','K'],
		['l','L'],
		[';',':'],
		['\'','"'],
		['return'],
		# 4th row
		['left shift'],
		['z','Z'],
		['x','X'],
		['c','C'],
		['v','V'],
		['b','B'],
		['n','N'],
		['m','M'],
		[',','<'],
		['.','>'],
		['/','?'],
		['right shift'],
		# 5th row
		['left fn'],
		['left control'],
		['left option'],
		['left command'],
		['spacebar'],
		['right command'],
		['right option']
	]

	def __init__(self, keyboard_layout, language):
		self.keyboard_layout = keyboard_layout
		self.language = Language(language)
		self.keyboard_model = self.BASE_KEYBOARD_MODEL
		# configure keyboard keys base on configurations
		for i, keyboard_key in enumerate(self.keyboard_model):
			# set key characters based on keyboard layout
			key_chars = keyboard_layout[i]
			primary_char = key_chars[0]
			if len(key_chars) == 2:
				secondary_char = key_chars[1]
			else:
				secondary_char = None
			keyboard_key.set_characters(primary_char, secondary_char)
			# adjust key difficulty score based on language
			key_char_frequency = self.language.get_letter_frequency(
				letter=primary_char.upper()
			)
			if key_char_frequency is not None:
				init_score = keyboard_key.get_difficulty()
				to_deduct = init_score * (key_char_frequency / 100)
				adjusted_score = init_score - to_deduct
				keyboard_key.set_difficulty(adjusted_score)

	def get_key_from_character(self, char):
		for key in self.keyboard_model:
			chars = list(key.get_characters().values())
			if char in chars:
				return key
		return None






