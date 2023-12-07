def clamp(x:int , minimum:int, maximum:int):
	"""Limit value to be between minimum and maximum constraints."""
	return max(minimum, min(x,maximum))

with open('./input.txt', mode='r', encoding='utf-8') as inputfile:
	chargrid = [list(line.strip()) for line in inputfile]
	matches = []
	ILEN = len(chargrid)
	JLEN = len(chargrid[0])

	for i in range(0,ILEN):
		for j in range(0,JLEN):
			if chargrid[i][j].isnumeric() and (not chargrid[i][clamp(j-1, 0, JLEN+1)].isdigit() if j != 0 else True):
				numboundary = 0
				num = ""
				part = False
				for x in range(j, JLEN):
					numboundary = x
					if not chargrid[i][x].isdigit():
						break
					num += chargrid[i][x]

				for x in range(clamp(j-1, 0, JLEN-1), numboundary+1):
					for y in [clamp(i-1, 0, ILEN-1), i, clamp(i+1, 0, ILEN-1)]:
						if not chargrid[y][x].isdecimal() and chargrid[y][x] != '.':
							part = True
				if part:
					matches.append(int(num))
	
	print("Answer: {}".format(sum(matches)))