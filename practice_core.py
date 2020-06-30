''' Tracks and stores the scales and progressions the user is working on'''

import note
import key
import chord
import progression

import time
import random

class practice:

	def __init__(self):
		random.seed()

	def print_ops(self):
		''' Shows the options the user can take '''
		print('\nRandom Note: 1')
		print('Generate Scale: 2')
		print('Random Scale: 3')
		# print('Generate Chord: 4')
		# print('Random Chord: 5')
		# print('Show Progression Menu: 6')
			# prog menu: 1 - show prog
			# 			2 - add degree
			#			3 - remove degree
			# 			4 - chain
			# 			5 - tritone sub
			# 			6 - rand prog
		print('Quit: -1')

	def op(self, num):
		if num is 1:
			# generate a random note
			# number of notes to generate [-1 for infinite]
			num_notes = int(input('Number of notes to generate [-1 for infinite]: '))
			# time between note generation
			sec = float(input('Number of seconds between output: '))
			# countdown
			for x in range (1, 5):
				print(x)
				time.sleep(sec)
			# generate
			i = 0
			while i is not num_notes:
				print(self.rand_note())
				time.sleep(sec)
				i += 1
		elif num is 2:
			# take input and generate scale
			tonic = input('\ninput key [C, F#, Bb, ...]: ')
			mode = input('input mode: ')
			scale = key.generate_scale(tonic, mode)
			print('Scale:', scale)
		elif num is 3:
			# rand scale
			print(self.rand_scale())
		elif num is -1:
			# quit
			print('Goodbye')
			return -1
		return 0

	def rand_note(self):
		''' generates a random note '''
		a = note.get_chromatic_sharps()
		b = note.get_chromatic_flats()

		n1 = random.randint(0, 1)
		i = random.randint(0, len(a) - 1)
		if n1 is 0:
			return a[i]
		else:
			return b[i]

	def rand_scale(self):
		root = self.rand_note()
		modes = list(key.get_modes())
		i = random.randint(0, len(modes) - 1)
		mode = modes[i]
		print('\n' + root, mode)
		return key.generate_scale(root, mode)