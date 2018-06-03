
# Keyboard Service


class Keyboard():
	"""
	Keyboard Service. Provides a keyboard model based on configuration options.

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
		def __init__(self, position, finger, difficulty):
			self.position = position
			self.finger = finger
			self.difficulty = difficulty
			self.primary_char = None
			self.secondary_char = None
		def set_characters(self, primary_char, secondary_char):
			self.primary_char = primary_char
			self.secondary_char = secondary_char


	# base keyboard model

	BASE_KEYBOARD_MODEL = [
		# 1st row
		Key([0,0], LEFT_PINKY, None), # ['`','~']
		LEFT_PINKY, # ['1','!'],
		LEFT_RING, # ['2','@'],
		LEFT_MIDDLE, # ['3','#'],
		LEFT_INDEX, # ['4','$'],
		LEFT_INDEX, # ['5','%'],
		RIGHT_INDEX, # ['6','^'],
		RIGHT_INDEX, # ['7','&'],
		RIGHT_MIDDLE, # ['8','*'],
		RIGHT_RING, # ['9','('],
		RIGHT_PINKY, # ['0',')'],
		RIGHT_PINKY, # ['-','_'],
		RIGHT_PINKY, # ['=','+'],
		RIGHT_PINKY, # ['delete']
		# 2nd row
		LEFT_PINKY, # ['tab'],
		LEFT_PINKY, # ['q','Q'],
		LEFT_RING, # ['w','W'],
		LEFT_MIDDLE, # ['e','E'],
		LEFT_INDEX, # ['r','R'],
		LEFT_INDEX, # ['t','T'],
		RIGHT_INDEX, # ['y','Y'],
		RIGHT_INDEX, # ['u','U'],
		RIGHT_MIDDLE, # ['i','I'],
		RIGHT_RING, # ['o','O'],
		RIGHT_PINKY, # ['p','P'],
		RIGHT_PINKY, # ['[','{'],
		RIGHT_PINKY, # [']','}'],
		RIGHT_PINKY, # ['\\', '|']
		# 3rd row
		LEFT_PINKY, # ['capslock'],
		LEFT_PINKY, # ['a','A'],
		LEFT_RING, # ['s','S'],
		LEFT_MIDDLE, # ['d','D'],
		LEFT_INDEX, # ['f','F'],
		LEFT_INDEX, # ['g','G'],
		RIGHT_INDEX, # ['h','H'],
		RIGHT_INDEX, # ['j','J'],
		RIGHT_MIDDLE, # ['k','K'],
		RIGHT_RING, # ['l','L'],
		RIGHT_PINKY, # [';',':'],
		RIGHT_PINKY, # ['\'','"'],
		RIGHT_PINKY, # ['return']
		# 4th row
		LEFT_PINKY, # ['left shift'],
		LEFT_PINKY, # ['z','Z'],
		LEFT_RING, # ['x','X'],
		LEFT_MIDDLE, # ['c','C'],
		LEFT_INDEX, # ['v','V'],
		LEFT_INDEX, # ['b','B'],
		RIGHT_INDEX, # ['n','N'],
		RIGHT_INDEX, # ['m','M'],
		RIGHT_MIDDLE, # [',','<'],
		RIGHT_RING, # ['.','>'],
		RIGHT_PINKY, # ['/','?'],
		RIGHT_PINKY, # ['right shift']
		# 5th row
		LEFT_PINKY, # ['left fn'],
		LEFT_PINKY, # ['left control'],
		LEFT_THUMB, # ['left option'],
		LEFT_THUMB, # ['left command'],
		THUMB, # ['spacebar'],
		RIGHT_THUMB, # ['right command'],
		RIGHT_PINKY # ['right option']
	]


	# keyboard configurations

	QWERTY_CONFIG = [
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

	def __init__(self, keyboard_config):
		self.keyboard_config = keyboard_config
		self.keyboard_model = self.BASE_KEYBOARD_MODEL
		# for key, keyboard_key in self.model.items():
		# 	key_chars = keyboard_config[key]
		# 	primary_char = key_chars[0]
		# 	if len(key_chars) == 2:
		# 		secondary_char = key_chars[1]
		# 	else:
		# 		secondary_char = None
		# 	keyboard_key.set_characters(primary_char, secondary_char):





