import re

def isPossible(game:str):
	rounds = game.split(': ')[1].split('; ')
	for round in rounds:
		r = re.search(r"(?P<red>\d+) (?:red)", round)
		r = int(r.group('red')) if r else 0
		
		g = re.search(r"(?P<green>\d+) (?:green)", round)
		g = int(g.group('green')) if g else 0
		
		b = re.search(r"(?P<blue>\d+) (?:blue)", round)
		b = int(b.group('blue')) if b else 0

		if (r+g+b > 39) or (r > 12) or (g > 13) or (b > 14):
			return False
	return True

with open(r'./input.txt', mode='r', encoding='utf-8') as inputfile:
	sumatoria = 0
	idregex = re.compile(r'(?:Game )(?P<ID>\d+)')
	for line in inputfile:
		line.strip();
		id = int(idregex.match(line).group('ID'))
		sumatoria += id if isPossible(line) else 0
	print(sumatoria)