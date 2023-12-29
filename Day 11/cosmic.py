#!/usr/bin/env python

from itertools import combinations

class Galaxy:
	def __init__(self, grid: list[list[str]]):
		self.grid = grid
	
	def getGrid(self) -> list[list[str]]:
		return self.grid
	
	def expand(self) -> None:
		column = 0
		while column < len(self.grid[0]):
			#If the line consists of void (".")
			col = [row[column] for row in self.grid]
			if len(set(col)) == 1 and col[0] == ".":
				for row in self.grid:
					row.insert(column, ".")
				column+=1
			column += 1
		
		row = 0
		while row < len(self.grid):
			line = "".join(self.grid[row])
			if len(set(line)) == 1 and line[0] == ".":
				self.grid.insert(row, self.grid[row].copy())
				row += 1
			row += 1
	
	def getCoords(self) -> list[tuple[int, int]]:
		"""Returns a list with coordinates of each galaxy"""
		coordinates = []
		for x, arr in enumerate(self.grid):
			for y, ch in enumerate(arr):
				if ch == "#":
					coordinates.append((x,y))
		return coordinates


if __name__ == "__main__":
	with open(r"./input.txt", mode="r", encoding="utf-8") as inputfile:
		galaxia = Galaxy([list(s) for s in inputfile.read().splitlines()])
		galaxia.expand()
		answer1 = 0
		for a, b in combinations(galaxia.getCoords(), 2):
			x1, y1 = a
			x2, y2 = b
			answer1 += abs(x1 - x2) + abs(y1 - y2)
		print("Answer 1:", answer1)