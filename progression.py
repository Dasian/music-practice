'''
	Generates and displays a chord progression
	progressions are a list of scale degrees with extensions
		ex: ['ii7', 'V7', 'Imaj9']
	
	TODO: Figure basically all of this out
		Figure out if the translation from scale degrees to note values should occur here

	add: chaining functionality, tritone subs, rootless chords
		individual note modifications?
'''
import chord

class Progression:
	# meat and potatoes bb
	# representation?? - list of str containing scale degrees
	progressions = [['ii', 'V', 'I'], ['IV', 'V', 'I']]

	# maybe shift qualities according to mode, then apply to create degrees
	qualities = ['maj', 'min', 'min', 'maj', 'maj', 'min', 'hdim']
	
	# don't default degrees? apply once mode is applied to qualities
	degrees = ['I', 'ii', 'iii', 'IV', 'V', 'vi', 'viihdim']

	def __init__(self, scale, mode):
		self.scale = scale
		self.mode = mode
		# check if this works one day
		self.qualities = qualities[mode:] + qualities[:mode]
		# apply qualities to degree list
		self.progression = []

	def get_scale(self):
		return scale

	def set_scale(self, scale):
		self.scale = scale

	def set_progression(self, prog):
		self.progression = prog

	def create_rand_prog(self):
		''' Creates a random progression, resets prev set progression '''

	# should this be done in progression.py?
	def translate_degrees(self, prog, scale):
		''' Returns a double array where the progression scale degrees
			are translated into the full chord
		'''

	def display_progression(self):
		''' Prints scale degrees and corresponding notes to the screen '''
		translated_chords = translate_degrees(progression, scale)
		i = 0
		for chord in translated_chords:
			c = ''
			for note in chord:
				c += note + ' '
			i += 1
			print(progression[i] + ':', c)


	def chain_chord(self, degree, prog):
		''' Chains a given progression to the first occurrences of the given degree '''
		# ii V I -> iii VI ii V I
		# ii/VI

	def tritone_sub(self, degree):
		''' Substitues the first occurences of the degree with a new chord '''
		# V -> bii