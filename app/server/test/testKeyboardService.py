
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


sentence = """
	In 1758, the taxonomist Linnaeus published in his Systema Naturae the
	classification of species. Canis is a Latin word meaning dog,[33] and under
	this genus he listed the dog-like carnivores including domestic dogs,
	wolves, and jackals. He classified the domestic dog as Canis familiaris and
	on the next page as a separate species he classified the wolf as Canis
	lupus.[2] In 1926, the International Commission on Zoological Nomenclature
	(ICZN) in Opinion 91 included Genus Canis on its Official Lists and Indexes
	of Names in Zoology.[3] In 1955, the ICZN's Direction 22 added Canis
	familiaris as the type species for genus Canis to the official list.[34] In
	1957, the ICZN ruled in Opinion 451 that Canis dingo be placed on its
	official list.[35][36]

	In 1978, a review to minimize the number species listed under genus Canis
	proposed that "Canis dingo is now generally regarded as a distinctive feral
	domestic dog. Canis familiaris is used for domestic dogs, although
	taxonomically it should probably be synonymous with Canis lupus."[37] In
	1982, the first edition of Mammal Species of the World included a note under
	Canis lupus with the comment: "Probably ancestor of and conspecific with the
	domestic dog, familiaris".[38]

	In 2003, the ICZN ruled in its Opinion 2027 that the "name of a wild
	species...is not invalid by virtue of being predated by the name based on a
	domestic form." Additionally, the ICZN placed the taxon Canis lupus as a
	conserved name on the official list under this opinion.[39] In the third
	edition of Mammal Species of the World published in 2005, the mammalogist W.
	Christopher Wozencraft listed under the wolf Canis lupus what he proposed to
	be two subspecies: "familiaris Linneaus, 1758 [domestic dog]" and "dingo
	Meyer, 1793 [domestic dog]",[a] with the comment "Includes the domestic dog
	as a subspecies, with the dingo provisionally separate – artificial variants
	created by domestication and selective breeding. Although this may stretch
	the subspecies concept, it retains the correct allocation of synonyms."[1]

	This classification by Wozencraft is hotly debated by zoologists.[40] Mathew
	Crowther, Stephen Jackson and Colin Groves disagree with Wozencraft and
	argue that based on ICZN Opinion 2027, the implication is that a domestic
	animal cannot be a subspecies.[41][42] Crowther, Juliet Clutton-Brock and
	others argue that because the dingo differs from wolves by behavior,
	morphology, and that the dingo and dog do not fall genetically within any
	extant wolf clade, that the dingo should be considered the distinct taxon
	Canis dingo.[43][40][42] Jackson and Groves regard the dog Canis familiaris
	as a taxonomic synonym for the wolf Canis lupus with them both equally
	ranked at the species level. They also disagree with Crowther, based on the
	overlap between dogs and dingoes in their morphology, in their ability to
	easily hybridize with each other, and that they show the signs of
	domestication by both having a cranium of smaller capacity than their
	progenitor, the wolf. Given that Canis familiaris Linnaeus, 1758 has date
	priority over Canis dingo Meyer, 1793, they regard the dingo as a junior
	taxonomic synonym for the dog Canis familiaris.[41] Gheorghe Benga and
	others support the dingo as a subspecies of the dog from the earlier Canis
	familiaris dingo designated by Johann Friedrich Blumenbach in 1799.

	The paleontologists Xiaoming Wang and Richard H. Tedford propose that the
	dog could be classified as Canis lupus familiaris under the Biological
	Species Concept because the dog can interbreed with the gray wolf (Canis
	lupus), and Canis familiaris under the Evolutionary Species Concept because
	the dog has commenced down a separate evolutionary pathway to the gray wolf.
"""
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
		'length': len(word),
		'difficulty': word_difficulty
	})
sorted_word_difficulties = sorted(
	word_difficulties,
	key=itemgetter('difficulty')
)
ppp(sorted_word_difficulties)










