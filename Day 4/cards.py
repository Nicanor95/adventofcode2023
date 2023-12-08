import re

with open(r'./input.txt', mode='r', encoding='utf-8') as inputfile:
	# It'd be faster to use str.split() but I love regex.
	regex = re.compile(r'(?:^Card +)(?P<ID>\d+)(?:: +)(?P<winning_numbers>.+)(?: \| +)(?P<numbers_in_card>.+)(?:$)')
	card_values = []

	for line in inputfile:
		line = regex.match(line)
		gameid = line.group('ID')
		winning_numbers = line.group('winning_numbers').split()
		numbers_in_card = line.group('numbers_in_card').split()

		for hits in [len(list(filter(lambda x: x in numbers_in_card, winning_numbers)))]:
			if hits: 
				card_values.append(pow(2,hits-1)) # -1 Because the first hit is worth 1 point
		
	print("Answer: {}".format(sum(card_values)))