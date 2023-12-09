import re

with open(r'./input.txt', mode='r', encoding='utf-8') as inputfile:
	# It'd be faster to use str.split() but I love regex.
	regex = re.compile(r'(?:^Card +)(?P<ID>\d+)(?:: +)(?P<winning_numbers>.+)(?: \| +)(?P<numbers_in_card>.+)(?:$)')
	card_values = []
	all_cards = []
	all_cards = []

	for line in inputfile:
		line = regex.match(line)
		gameid = line.group('ID')
		winning_numbers = line.group('winning_numbers').split()
		numbers_in_card = line.group('numbers_in_card').split()

		for hits in [len(list(filter(lambda x: x in numbers_in_card, winning_numbers)))]:
			all_cards.append([gameid, hits, 1]) # [card id, matches, amount of cards.]
			all_cards.append([gameid, hits, 1]) # [card id, matches, amount of cards.]
			if hits: 
				card_values.append(pow(2,hits-1)) # -1 Because the first hit is worth 1 point

	for index, card in enumerate(all_cards):
		i = index + card[1] if index+card[1] < len(all_cards) else len(all_cards)-1
		while i > index:
			all_cards[i][2] += card[2]
			i -= 1
			
	print("Answer 1: {}\nAnswer 2: {}".format(sum(card_values),sum([x[2] for x in all_cards])))