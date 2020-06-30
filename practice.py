'''
	Select a key, a mode, and generate a chord progression

	Implement: major/minor, random key, chord substitution capability
		show notes along with scale degrees, 

	Figure out: chord progression representation, enharmonics,
		substiutions, voicings
'''
import practice_core

p = practice_core.practice()
i = 0

while i is 0:
	try:
		p.print_ops()
		inp = int(input('Input: '))
		i = p.op(inp)
	except:
		print('oop dont do that')