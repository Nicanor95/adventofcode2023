from functools import reduce

def clamp(x:int , minimum:int, maximum:int):
	"""Limit value to be between minimum and maximum constraints."""
	return max(minimum, min(x,maximum))

with open('./input.txt', mode='r', encoding='utf-8') as inputfile:
	chargrid = [list(line.strip()) for line in inputfile]
	parts = []
	cogcalibration = []
	ILEN = len(chargrid)
	JLEN = len(chargrid[0])

	for i in range(0,ILEN):
		for j in range(0,JLEN):
			# Part 1 stuff.
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
					parts.append(int(num))

			# Part 2 stuff.
			if chargrid[i][j] == "*":
				cogparts = []
				for x in [clamp(i-1, 0, ILEN-1), i, clamp(i+1, 0, ILEN-1)]:
					for y in [clamp(j-1, 0, JLEN-1), j, clamp(j+1, 0, JLEN-1)]:
						if chargrid[x][y].isnumeric():
							nstart = y
							while nstart >= 0 and chargrid[x][nstart].isnumeric():
								nstart -= 1
							nstart += 1 
							cogpart = (x, nstart)
							if cogpart not in cogparts:
								cogparts.append(cogpart)
				partnumbers = []
				for x, y in cogparts:
					partnumber = ""
					while chargrid[x][y].isnumeric():
						partnumber += chargrid[x][y]
						y += 1
						if y >= JLEN: break
					partnumbers.append(int(partnumber))
				
				if len(partnumbers) > 1:
					cogcalibration.append(reduce(lambda x, y: x * y, partnumbers))
	
	print("Answer 1: {}\nAnswer 2: {}".format(sum(parts), sum(cogcalibration)))