'''
	Generates a scale given a key and mode
	TODO: figure out if there's a seperate way to generate scales using note module
			-make it more efficient/comprehensive
'''

import note

# These are inverses but having two lists helps conceptually
sharp_order = ['F', 'C', 'G', 'D', 'A', 'E', 'B']
flat_order = ['B', 'E', 'A', 'D', 'G', 'C', 'F']

major_keys = {'C': ('#', 0), 'G': ('#', 1), 'D': ('#', 2), 'A': ('#', 3), 'E': ('#', 4), 'B': ('#', 5), 
	'F#': ('#', 6), 'C#': ('#', 7), 'F': ('b', 1), 'Bb': ('b', 2), 'Eb': ('b', 3), 'Ab': ('b', 4),
	'Db': ('b', 5), 'Gb': ('b', 6), 'Cb': ('b', 7)}

# intervals of a scale, defaults to major
# apply a shift to generate different modes
# w w h w w w h
steps = [2, 2, 1, 2, 2, 2, 1]

# mode values are relative to the relative major 
# values determine the index of the first step in the steps list
modes = {'major': 0, 'ionian': 0, 'dorian': 1, 'phrygian': 2, 'lydian': 3, 
	'mixolydian': 4, 'minor': 5, 'aeolian': 5, 'locrian': 6}

def is_valid_mode(mode_name):
	if mode_name not in modes.keys():
		return False
	return True

def is_valid_major_key(n):
	''' Determines if a note is a key for any scale/mode combination'''
	if not note.is_valid_note(n) or n not in major_keys.keys():
		return False
	return True

def get_modes():
	return modes.keys()

# enharmonics E# D# Fb Gb B# Cb major
# do more
def generate_scale(root, mode_name):
	'''
		generate a scale given the starting note and mode
	'''
	if (not is_valid_mode(mode_name)):
		print('invalid input', note.is_valid_note(root))
		return

	# determine which major key to generate
	mode = modes[mode_name]
	rel_maj = relative_major(root, mode_name)
	scale = note.get_notes_unmodified().copy()
	key = major_keys[rel_maj]
	modifier = key[0]
	if modifier is '#':
		order = sharp_order
	else:
		order = flat_order

	# gernerate major scale
	for i in range(0, key[1]):
		change = order[i]
		if modifier is '#':
			scale[scale.index(change)] = note.sharpen(change)
		else:
			scale[scale.index(change)] = note.flatten(change)

	# shift scale to match mode
	if root not in scale:
		print("doesn't handle theoretical keys")
		return
	shift = scale.index(root)
	scale = scale[shift:] + scale[:shift]
	return scale

def relative_major(root, mode_name):
	'''
		determines the relative major of a scale given the root and mode
	'''
	if not is_valid_mode(mode_name):
		return

	# find starting set of notes
	notes = note.get_chromatic_sharps()
	enharmonic = note.get_chromatic_flats()
	if root not in notes:
		notes = note.get_chromatic_flats()
		enharmonic = note.get_chromatic_sharps()

	# apply steps to notes, stop at relative major
	steps_i = modes[mode_name]
	notes_i = notes.index(root)
	rel_maj = root
	while steps_i is not 0:
		notes_i = (notes_i + steps[steps_i]) % len(notes)
		rel_maj = notes[notes_i]
		steps_i = (steps_i + 1) % len(steps)

	# enharmonic adjusting
	if rel_maj not in major_keys.keys():
		rel_maj = enharmonic[notes.index(rel_maj)]

	print('Relative major:', rel_maj)

	return rel_maj