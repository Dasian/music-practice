''' Note manipulation and verification
	note is a string with a modifier
		ex: A, Bb, C#, Dxx#
	TODO: modify is_valid_note to account for proper double sharp usage;
			-only 1 sharp should ever be present, 2 sharps become a double sharp
		determine how to evaluate intervals/if they should be eval here
'''

notes_unmodified = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
chromatic_sharps = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
chromatic_flats = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'Cb']
# maps note to number of halfsteps from C
note_values = {'C': 0, 'D': 2, 'E': 3, 'F': 4, 'G': 6, 'A': 8, 'B': 9}
modifier_values = {'#': 1, 'x': 2, 'b': -1}

def is_valid_note(note):
	''' Determines if a given note is valid '''
	# valid unmodified notes + valid modifier usage
	if note[0] not in notes_unmodified:
		return False

	# determine which modifier will be used
	if len(note) > 1 and note[1] is 'b':
		flats = True
	else:
		flats = False

	# determine if the corret modifier is being used [if used at all]
	for i in range(1, len(note)):
		if flats and note[i] is not 'b':
			return False
		elif not flats and note[i] is not 'x':
			if not flats and note[i] is not '#':
				return False

	return True

def sharpen(note):
	''' Raises a given note by 1 half step '''
	if not is_valid_note(note):
		return

	if '#' in note:
		return note[:-1] + 'x'
	elif 'b' in note:
		return note[:-1]
	else:
		return note + '#'

def flatten(note):
	''' Lowers a given note by 1 half step '''
	if not is_valid_note(note):
		return

	if '#' in note:
		return note[:-1]
	elif 'x' in note:
		return note[:-1] + '#'
	else:
		return note + 'b'

def get_value(note):
	''' determines the numerical value of a note '''
	if not is_valid_note(note):
		return -1

	val = note_values[note[0]]
	for i in range(1, len(note)):
		val += modifier_values[note[i]]

	return val

# these return references to the lists
def get_notes_unmodified():
	return notes_unmodified

def get_chromatic_sharps():
	return chromatic_sharps

def get_chromatic_flats():
	return chromatic_flats
