import re

def minimumPossible(game:str):
	count_r, count_g, count_b = [], [], []
	rounds = game.split(': ')[1].split('; ')
	for round in rounds:
		r = re.search(r"(?P<red>\d+) (?:red)", round)
		count_r.append(int(r.group('red')) if r else 0)

		g = re.search(r"(?P<green>\d+) (?:green)", round)
		count_g.append(int(g.group('green')) if g else 0)
		
		b = re.search(r"(?P<blue>\d+) (?:blue)", round)
		count_b.append(int(b.group('blue')) if b else 0)
	return (max(count_r) * max(count_g) * max(count_b))



with open(r'./input.txt', mode='r', encoding='utf-8') as inputfile:
	sumatoria = 0
	for line in inputfile:
		line.strip();
		sumatoria += minimumPossible(line)
	print(sumatoria)