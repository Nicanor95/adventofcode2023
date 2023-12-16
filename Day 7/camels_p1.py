from collections import Counter


def handValue(hand : str, values : dict) -> int: # This is a mess, likely wont work with all inputs.
	value = 0
	for i, card in enumerate(reversed(hand), start = 1):
		value += (i**100) * values.get(card) 
	
	quantities = sorted(Counter(hand).values(), reverse=True)
	match quantities[0]:
		# Par
		case 2 if quantities[1] != 2:
			value **= 2
		# Double Par
		case 2 if quantities[1] == 2:
			value **= 3
		# Trio
		case 3 if quantities[1] != 2:
			value **= 4
		# Full house
		case 3 if quantities[1] == 2:
			value **= 5
		# Four of a kind
		case 4:
			value **= 6
		# Five of a kind
		case 5:
			value **= 7

	return value

with open(r'./input.txt', mode = 'r', encoding = 'utf-8') as inputfile:
	values = { "2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 7, "9": 8, "T": 9, "J": 10, "Q": 11, "K": 12, "A": 13 }
	hands = [tuple(line.split()) for line in inputfile.readlines()]
	sorted_hands = sorted(hands, key = lambda x: handValue(x[0], values))

	answer = 0
	for i, hand in enumerate(sorted_hands, start=1):
		answer += int(hand[1]) * i
	
	for hand in sorted_hands:
		print(hand)
	print("Answer 1: {}".format(answer))