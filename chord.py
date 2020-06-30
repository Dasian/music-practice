'''
	Translates a progression to its chord values
	chords are a list of notes
	TODO: Figure out how to generate each chord
			-input just the root or the entire chord; root makes sense but verification may need to be done [Gx aug]
			-use a combination of min/maj3?; if ext is in the input I need the entire scale [iidim9 needs tonic]
			-how to add extensions; it should be included in the note I think
			-maybe a combination of note value and ext in a tuple ('Ab', 'maj9')
				-so the scale doesn't need to be utilized here, only in progression.py
			-use key.py to generate the entire scale?
'''
import key
import note

# how do chords work?? come up with longest/most complex chord name and 
# develop chord_tup and chord generation from there

def generate(chord_tup):
	''' Takes in a tuple ('Note', 'quality', ext, mod, sus) and returns the chord '''
	# ex: generate(('Ab', 'min', 11, 'b9', None)) == Abmin11b9 => Ab Cb Eb Gb Bbb Db
	root = chord_tup[0]
	if root is not note.is_valid_note(root):
		return

	# parse further
	quality = chord_tup[1]
	ext = chord_tup[2]
	mod = chord_tup[3]
	sus = chord_tup[4]

	# generate the proper major, minor, aug, or dim chord
		# need to find the highest ext to generate
	if 'maj' in quality or 'dom' in quality:
		chord = major(root, ext, sus)
	elif 'min' in quality:
		chord = minor(root, ext, sus)
	elif 'aug' in quality:
		chord = augment(root, ext, sus)
	elif 'dim' in quality:
		chord = diminish(root, ext, sus)
	else:
		return
	# apply further modifications; b9, #5, sus4, etc.
	for deg in mod:
		# 
		print(deg)
	return chord
		
def major(root, ext=5, sus=None):
	''' Returns the major chord for a given root '''
	# maj 3, min3, maj3 

	# check if valid root
	if not key.is_valid_major_key(root):
		return

	# use key.generate_scale() ? or have own note system here
	scale = key.generate_scale(root, 'major')
	for i in range(0, ext+1, 2):
		chord.append(scale[i % len(scale)])

	return chord

def minor(root, ext=5, sus=None):
	''' Makes a chord minor '''
	# flatten 3rd and 7th [min3, maj3, min3]

	# figure out how to verify if valid minor key
	if not note.is_valid_note(note):
		return

	scale = key.generate_scale(root, 'minor')
	for i in range(0, ext+1, 2):
		chord.append(scale[i % len(scale)])

	return chord

def dominant(root, ext=7, sus=None):
	return root

def diminish(root, ext=5, sus=None):
	''' Fully diminishes a given chord '''
	# minor 3rd dim 5th and dim 7th [stack minor thirds]
	chord = minor(root, ext, sus)
	if chord is None:
		return
	# b5
	chord[2] = note.flatten(chord[2])
	if ext >= 7:
		# bb7
		chord[3] = note.flatten(note.flatten(chord[3]))

	return chord

def augment(root, ext=5, sus=None):
	''' Augments a given chord '''
	# maj 3, aug 5th, min 7 [maj3, maj3, min3]
	chord = major(root, ext, sus)
	if chord is None:
		return

	# #5
	chord[2] = note.sharpen(chord[2])
	if ext >= 7:
		# b7
		chord[3] = note.flatten(chord[3])

def flatten(chord):
	''' Flattens all notes in a chord '''
	for n in chord:
		if not note.is_valid_note(n):
			return
		new_note = note.flatten(n)
		chord[chord.index(n)] = new_note
	return chord

def sharpen(chord):
	''' Sharpens all notes in a chord '''
	for n in chord:
		if not note.is_valid_note(n):
			return
		new_note = note.sharpen(n)
		chord[chord.index(n)] = new_note
	return chord