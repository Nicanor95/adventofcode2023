#!/usr/bin/env python
import re
from functools import reduce
from math import sqrt,ceil,floor


def winmargin(race: tuple) -> int:
	# 	f(x) = x * (x + (T - x)) - x^2 - D = 0 (Equal 0 because we only care about the edge roots)
	# 				f(x) = x * T - x^2 - D = 0 
	#				f(x) = x^2 - x * T + D = 0 (Doesn't describe the same curve, but we only care about roots.)
	time, distance = race

	# Calculate discriminant, -> b^2 - 4*a*c
	discriminant = (pow(time, 2)) - (4*distance) # a is always 1 in our case so we ignore it.

	# Calculate roots, we only care about Integer values.
	r1 = ceil((-time - sqrt(discriminant))/2)		# Since it's the lower edge, we use ceiling for the closest 'millisecond'
	r2 = floor((-time + sqrt(discriminant))/2+1)	# Upper edge, so we use floor instead. +1 because it should include it.	

	return r2 - r1


with open(r'./input.txt', mode='r', encoding='utf-8') as inputfile:
	times = list(map(int,re.findall(r'\d+',inputfile.readline())))
	distances = list(map(int,re.findall(r'\d+',inputfile.readline())))
	races = list(zip(times,distances))

	times_p2 = int("".join(map(str, times)))
	distances_p2 = int("".join(map(str, distances)))

	sol1 = reduce(lambda x,y: x*y, [winmargin(race) for race in races])
	sol2 = winmargin((times_p2, distances_p2))
	print("Answer 1: {}\nAnswer 2: {}".format(sol1, sol2))