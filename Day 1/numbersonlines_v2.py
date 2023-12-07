with open(r'./input.txt', mode="r", encoding='utf-8') as inputfile:
	sumatoria = 0
	for line in inputfile:
		line = line.strip()
		#Replace the named numbers by their symbols.
		line = line.replace('one', 'o1e').replace('two', 't2o').replace('three', 't3e').replace('four', 'f4r').replace('five', 'f5e').replace('six', 's6x').replace('seven', 's7n').replace('eight', 'e8t').replace('nine', 'n9e')

		numbers = list(filter(lambda x: x.isnumeric(), line))
		sumatoria += int(numbers[0] + numbers[-1])
	print(sumatoria)
