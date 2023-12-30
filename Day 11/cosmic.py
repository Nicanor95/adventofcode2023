#!/usr/bin/env python

from itertools import combinations
from copy import deepcopy

class Galaxy:
	def __init__(self, grid: list[list[str]]):
		self.grid = grid
		self.expandedGrid = []
		self.emptyColumns = []
		self.emptyRows = []
		self.fillEmptyRC()
		self.expand()
	
	def getGrid(self) -> list[list[str]]:
		return self.grid
	
	def fillEmptyRC(self) -> None:
		for column in range(0,len(self.grid)):
			col = [row[column] for row in self.grid]
			if len(set(col)) == 1 and col[0] == ".":
				self.emptyColumns.append(column)
		
		for i, row in enumerate(self.grid):
			if len(set(row)) == 1 and row[0] == ".":
				self.emptyRows.append(i) 

		
	def expand(self) -> None:
		self.expandedGrid = deepcopy(self.grid)
		column = 0
		while column < len(self.expandedGrid[0]):
			#If the line consists of void (".")
			col = [row[column] for row in self.expandedGrid]
			if len(set(col)) == 1 and col[0] == ".":
				for row in self.expandedGrid:
					row.insert(column, ".")
				column+=1
			column += 1
		
		row = 0
		while row < len(self.expandedGrid):
			line = "".join(self.expandedGrid[row])
			if len(set(line)) == 1 and line[0] == ".":
				self.expandedGrid.insert(row, self.expandedGrid[row].copy())
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
	
	def getExpandedCoords(self) -> list[tuple[int, int]]:
		"""Returns a list with coordinates of each galaxy in the expanded grid"""
		coordinates = []
		for x, arr in enumerate(self.expandedGrid):
			for y, ch in enumerate(arr):
				if ch == "#":
					coordinates.append((x,y))
		return coordinates

	def calcDistance(self, a: tuple, b: tuple) -> int:
		"""
		Returns the distance between two galaxies, contemplating
		the expanded universe for part 2.
		"""
		x1, y1 = a
		x2, y2 = b
		voidsBetween = 0
		for void in self.emptyColumns:
			if (y1 < void < y2) or (y1 > void > y2):
				voidsBetween += 1

		for void in self.emptyRows:
			if (x1 < void < x2) or (x1 > void > x2):
				voidsBetween += 1
		return abs(x1 - x2) + abs(y1 - y2) + 999999 * voidsBetween

if __name__ == "__main__":
	with open(r"./input.txt", mode="r", encoding="utf-8") as inputfile:
		galaxia = Galaxy([list(s) for s in inputfile.read().splitlines()])
		answer1 = 0
		answer2 = 0
		for a, b in combinations(galaxia.getExpandedCoords(), 2):
			x1, y1 = a
			x2, y2 = b
			answer1 += abs(x1 - x2) + abs(y1 - y2)
		
		for a, b in combinations(galaxia.getCoords(), 2):
			answer2 += galaxia.calcDistance(a, b)

		print("Answer 1:", answer1)
		print("Answer 2:", answer2)