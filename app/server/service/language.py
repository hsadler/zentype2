
# Language Service


class Language():
	"""
	Language Service. Provides language information for selected language.

	"""


	# settings per language

	ENGLISH = {
		'type': 1,
		'letter_frequencies': {
			'E': 12.02,
			'T': 9.10,
			'A': 8.12,
			'O': 7.68,
			'I': 7.31,
			'N': 6.95,
			'S': 6.28,
			'R': 6.02,
			'H': 5.92,
			'D': 4.32,
			'L': 3.98,
			'U': 2.88,
			'C': 2.71,
			'M': 2.61,
			'F': 2.30,
			'Y': 2.11,
			'W': 2.09,
			'G': 2.03,
			'P': 1.82,
			'B': 1.49,
			'V': 1.11,
			'K': 0.69,
			'X': 0.17,
			'Q': 0.11,
			'J': 0.10,
			'Z': 0.07
		}
	}


	def __init__(self, language):
		self.type = language['type']
		self.letter_frequencies = language['letter_frequencies']


	def get_type(self):
		return self.type


	def get_letter_frequency(self, letter):
		if letter in self.letter_frequencies:
			return self.letter_frequencies[letter]
		else:
			return None

