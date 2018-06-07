
import sys
sys.path.append('..')

from operator import itemgetter

from service.keyboard import Keyboard
from service.language import Language
from utils.print import ppp


keyboard = Keyboard(Keyboard.QWERTY, Language.ENGLISH)
for key in keyboard.keyboard_model:
	ppp(key.to_dict())


lingo = Language(Language.ENGLISH)
ppp(lingo.letter_frequencies)


word_text = 'word'
for ch in word_text:
	key = keyboard.get_key_from_character(ch)
	ppp(key.to_dict())


sentence = 'Cats are similar in anatomy to the other felids, with a strong flexible body, quick reflexes, sharp retractable claws and teeth adapted to killing small prey. Cat senses fit a crepuscular and predatory ecological niche. Cats can hear sounds too faint or too high in frequency for human ears, such as those made by mice and other small animals. They can see in near darkness. Like most other mammals, cats have poorer color vision and a better sense of smell than humans. Cats, despite being solitary hunters, are a social species, and cat communication includes the use of a variety of vocalizations (mewing, purring, trilling, hissing, growling and grunting) as well as cat pheromones and types of cat-specific body language.'
cleaned_sentence = []
for ch in sentence:
	if ch.isalpha() or ch == ' ':
		cleaned_sentence.append(ch)
sentence = ''.join(cleaned_sentence)
words = sentence.split()
word_difficulties = []
for word in words:
	word_difficulty = keyboard.get_keyboard_difficulty_for_word(
		word=word,
		round_to_int=True
	)
	word_difficulties.append({
		'word': word,
		'difficulty': word_difficulty
	})
sorted_word_difficulties = sorted(
	word_difficulties,
	key=itemgetter('difficulty')
)
ppp(sorted_word_difficulties)










