from collections import Counter


def handValue(hand : str, values : dict, joker = "") -> int: # This is a mess, likely wont work with all inputs.
	value = 0
	
	if joker != "":
		values[joker] = 1

	for i, card in enumerate(reversed(hand), start = 1):
		value += (i**100) * values.get(card) 
	

	quantities = Counter(hand)
	joker_quant = quantities[joker]
	quantities[joker] = 0
	
	quantities = sorted(quantities.values(), reverse=True)
	match quantities[0] + joker_quant:
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
	values = { "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14 }
	hands = [tuple(line.split()) for line in inputfile.readlines()]
	sorted_hands = sorted(hands, key = lambda x: handValue(x[0], values))
	sorted_hands_p2 = sorted(hands, key = lambda x: handValue(x[0], values, joker="J"))

	answer = 0
	for i, hand in enumerate(sorted_hands, start=1):
		answer += int(hand[1]) * i
	
	answer_p2 = 0
	for i, hand in enumerate(sorted_hands_p2, start=1):
		answer_p2 += int(hand[1]) * i
	
	print("Answer 1: {}".format(answer))
	print("Answer 2: {}".format(answer_p2))