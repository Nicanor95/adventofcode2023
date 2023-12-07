with open(r'./input.txt', mode="r", encoding='utf-8') as inputfile:
	sumatoria = 0
	for line in inputfile:
		numbers = list(filter(lambda x: x.isnumeric(), line.strip()))
		sumatoria += int(numbers[0] + numbers[-1])
	print(sumatoria)
