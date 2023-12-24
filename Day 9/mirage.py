#!/usr/bin/env python

from itertools import pairwise

def predict(line: str) -> int:
	"""
	Takes a string with a sequence of integers and returns the
	next integer in the sequence.

	Args:
		line (str): The sequence of integers, ex: "1 12 31 45"
	
	Returns:
		int: The next integer in the sequence
	"""
	values = list(map(int, line.split()))
	if len(set(values)) == 1 and values[0] == 0:
		return 0
	else:
		values_next = [y - x for x, y in pairwise(values)]
		return values[-1] + predict(" ".join(map(str, values_next)))


if __name__ == '__main__':
	with open(r"./input.txt", mode="r", encoding="utf-8") as inputfile:
		input = inputfile.read().splitlines()
		nextvalues = [predict(line) for line in input]

		nextvalues_p2 = [" ".join(reversed(line.split())) for line in input]
		nextvalues_p2 = [predict(line) for line in nextvalues_p2]

		print("Answer 1: {}\nAnswer 2: {}".format(sum(nextvalues), sum(nextvalues_p2)))