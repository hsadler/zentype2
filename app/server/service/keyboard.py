
# Keyboard Service

from service.language import Language


class Keyboard():
	"""
	Keyboard Service. Provides a keyboard model and methods based on key layout
	and language configurations.

	TODO:
		X make all difficulty scores higher (* 100)
		- round all score outputs to an integer

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


	# hands
	LEFT_HAND = [
		LEFT_PINKY,
		LEFT_RING,
		LEFT_MIDDLE,
		LEFT_INDEX,
		LEFT_THUMB
	]

	RIGHT_HAND = [
		RIGHT_THUMB,
		RIGHT_INDEX,
		RIGHT_MIDDLE,
		RIGHT_RING,
		RIGHT_PINKY
	]


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
		def get_difficulty(self, char=None, round_to_int=False):
			base_d = self.difficulty
			res = None
			if char is not None and char == self.get_secondary_char():
				res = base_d + (base_d * 2/3)
			else:
				res = base_d
			if round_to_int:
				return int(res)
			else:
				return res
		def set_characters(self, primary_char, secondary_char):
			self.primary_char = primary_char
			self.secondary_char = secondary_char
		def get_characters(self):
			return {
				'primary': self.primary_char,
				'secondary': self.secondary_char
			}
		def get_primary_char(self):
			return self.primary_char
		def get_secondary_char(self):
			return self.secondary_char
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
		Key([1,1], LEFT_PINKY, 275), # ['q','Q']
		Key([1,2], LEFT_RING, 150), # ['w','W']
		Key([1,3], LEFT_MIDDLE, 150), # ['e','E']
		Key([1,4], LEFT_INDEX, 150), # ['r','R']
		Key([1,5], LEFT_INDEX, 250), # ['t','T']
		Key([1,6], RIGHT_INDEX, 250), # ['y','Y']
		Key([1,7], RIGHT_INDEX, 150), # ['u','U']
		Key([1,8], RIGHT_MIDDLE, 150), # ['i','I']
		Key([1,9], RIGHT_RING, 150), # ['o','O']
		Key([1,10], RIGHT_PINKY, 275), # ['p','P']
		Key([1,11], RIGHT_PINKY, None), # ['[','{']
		Key([1,12], RIGHT_PINKY, None), # [']','}']
		Key([1,13], RIGHT_PINKY, None), # ['\\', '|']
		# 3rd row
		Key([2,0], LEFT_PINKY, None), # ['capslock']
		Key([2,1], LEFT_PINKY, 100), # ['a','A']
		Key([2,2], LEFT_RING, 100), # ['s','S']
		Key([2,3], LEFT_MIDDLE, 100), # ['d','D']
		Key([2,4], LEFT_INDEX, 100), # ['f','F']
		Key([2,5], LEFT_INDEX, 175), # ['g','G']
		Key([2,6], RIGHT_INDEX, 175), # ['h','H']
		Key([2,7], RIGHT_INDEX, 100), # ['j','J']
		Key([2,8], RIGHT_MIDDLE, 100), # ['k','K']
		Key([2,9], RIGHT_RING, 100), # ['l','L']
		Key([2,10], RIGHT_PINKY, None), # [';',':']
		Key([2,11], RIGHT_PINKY, None), # ['\'','"']
		Key([2,12], RIGHT_PINKY, None), # ['return']
		# 4th row
		Key([3,0], LEFT_PINKY, None), # ['left shift']
		Key([3,1], LEFT_PINKY, 275), # ['z','Z']
		Key([3,2], LEFT_RING, 275), # ['x','X']
		Key([3,3], LEFT_MIDDLE, 200), # ['c','C']
		Key([3,4], LEFT_INDEX, 200), # ['v','V']
		Key([3,5], LEFT_INDEX, 300), # ['b','B']
		Key([3,6], RIGHT_INDEX, 200), # ['n','N']
		Key([3,7], RIGHT_INDEX, 200), # ['m','M']
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


	def __init__(self, keyboard_layout, language=None):
		self.keyboard_layout = keyboard_layout
		self.language = Language(language) if language is not None else None
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
			# if language is set, adjust key difficulty score based on language
			if self.language is not None:
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

	@classmethod
	def calculate_key_transition_difficulty(
		cls,
		char_1,
		key_1,
		char_2,
		key_2,
		round_to_int=False
	):
		key_1_diff = key_1.get_difficulty(char=char_1)
		key_2_diff = key_2.get_difficulty(char=char_2)
		avg_difficulty = (key_1_diff + key_2_diff) / 2
		base_trans_difficulty = avg_difficulty / 4
		key_1_fing = key_1.get_finger()
		key_2_fing = key_2.get_finger()
		key_1_hand = 'left' if key_1_fing in cls.LEFT_HAND else 'right'
		key_2_hand = 'left' if key_2_fing in cls.LEFT_HAND else 'right'
		res = None
		# same key 2 times in a row
		if key_1 == key_2:
			res = base_trans_difficulty - (base_trans_difficulty / 3)
		# same finger on same hand
		elif key_1_fing == key_2_fing:
			res = base_trans_difficulty
		# same hand
		elif key_1_hand == key_2_hand:
			res = base_trans_difficulty - (base_trans_difficulty / 3)
		# otherwise, is different hand
		else:
			res = base_trans_difficulty - (base_trans_difficulty * 2/3)
		if round_to_int:
			return int(res)
		else:
			return res

	def get_keyboard_difficulty_for_word(self, word, round_to_int=False):
		keys_data = []
		for char in word:
			k = {
				'char': char,
				'key': self.get_key_from_character(char)
			}
			keys_data.append(k)
		difficulty_vals = []
		keys_data_len = len(keys_data)
		for index, key_data in enumerate(keys_data):
			# add key difficulty based on char
			k_difficulty = key_data['key'].get_difficulty(char=key_data['char'])
			difficulty_vals.append(k_difficulty)
			# add key transition difficulties
			if index < keys_data_len - 1:
				trans_difficulty = self.calculate_key_transition_difficulty(
					char_1=key_data['char'],
					key_1=key_data['key'],
					char_2=keys_data[index + 1]['char'],
					key_2=keys_data[index + 1]['key']
				)
				difficulty_vals.append(trans_difficulty)
		if round_to_int:
			return int(sum(difficulty_vals))
		else:
			return sum(difficulty_vals)

