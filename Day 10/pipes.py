#!/usr/bin/env python

def findSnake(grid: list) -> tuple[int, int]:
	for i, line in enumerate(grid):
		if "S" in line:
			return (i, line.index("S"))
	return (-1,-1)
			
def revealPipe(snakePos: tuple, grid: list) -> str:
	x, y = snakePos
	north, east, south, west = (False, False, False, False)
	
	# Check north
	if grid[x - 1][y] in ("|", "7", "F"):
		north = True
	# Check east
	if grid[x][y + 1] in ("-", "J", "7"):
		east = True
	# Check south
	if grid[x + 1][y] in ("|", "L", "J"):
		south = True
	# Check west
	if grid[x][y - 1] in ("-", "L", "F"):
		west = True
	
	connections = (north, east, south, west)

	match connections: 
		case (True,True,False,False):
			return "L"
		case (True,False,True,False):
			return "|"
		case (True,False,False,True):
			return "J"
		case (False,True,True,False):
			return "F"
		case (False,False,True,True):
			return "7"
		case (False,True,False,True):
			return "-"
		case _: # Shouldn't happen unless snakePos is incorrect.
			return "."

def nextPipes(pos: tuple, grid: list) -> list[tuple[int, int]]:
	x, y = pos
	ret = []
	match grid[x][y] if grid[x][y] != "S" else revealPipe(pos, grid):
		case "L":
			ret.append((x - 1, y))
			ret.append((x, y + 1))
		case "|":
			ret.append((x - 1, y))
			ret.append((x + 1, y))
		case "J":
			ret.append((x - 1, y))
			ret.append((x, y - 1))
		case "F":
			ret.append((x, y + 1))
			ret.append((x + 1, y))
		case "7":
			ret.append((x, y - 1))
			ret.append((x + 1, y))
		case "-":
			ret.append((x, y - 1))
			ret.append((x, y + 1))
	return ret

def followPipe(snakePos: tuple, grid: list) -> int:
	x, y = snakePos
	x1, y1 = snakePos
	prev1 = (x1, y1)
	x2, y2 = snakePos
	prev2 = (x2, y2)
	count = 0
	while True:
		if (x1, y1) == (x2, y2) == (x, y):
			next = nextPipes((x,y), grid)
			x1, y1 = next[0]
			x2, y2 = next[1]
			continue
		if (x1, y1) != (x2, y2):
			count += 1
			next1 = nextPipes((x1,y1), grid)
			next2 = nextPipes((x2,y2), grid)
			for nextpipe in next1:
				if nextpipe != (x1, y1) and nextpipe != prev1:
					prev1 = (x1, y1)
					x1, y1 = nextpipe
					break
			for nextpipe in next2:
				if nextpipe != (x2, y2) and nextpipe != prev2:
					prev2 = (x2, y2)
					x2, y2 = nextpipe
					break
		if (x1, y1) == (x2, y2):
			count += 1
			break
		
	return count


if __name__ == '__main__':
	with open(r"./input.txt", mode="r", encoding="utf-8") as inputfile:
		grid = inputfile.read().splitlines()
		snake = findSnake(grid)
		print("Answer 1:", followPipe(snake,grid))
