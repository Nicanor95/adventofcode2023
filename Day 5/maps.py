###########################################################################################
# The maps are [Destination start, Source start, Range]                                   #
# So [50, 80, 2], given the range of 2, the destination is [50, 51] and source is [80,81] #
# This means that Seed 81 (source in a seed-to-soil map), would go in Soil 51.            #
###########################################################################################

import re


with open(r'./input.txt', mode='r', encoding='utf-8') as inputfile:
	regex = re.compile(r'(?:^seeds: )(?P<seeds>.+$)(?:\n+^seed-to-soil map:\n)(?P<seed_to_soil>(?:^.+\n)+)(?:\n^soil-to-fertilizer map:\n)(?P<soil_to_fertilizer>(?:^.+\n)+)(?:\n^fertilizer-to-water map:\n)(?P<fertilizer_to_water>(?:^.+\n)+)(?:\n^water-to-light map:\n)(?P<water_to_light>(?:^.+\n)+)(?:\n^light-to-temperature map:\n)(?P<light_to_temperature>(?:^.+\n)+)(?:\n^temperature-to-humidity map:\n)(?P<temperature_to_humidity>(?:^.+\n)+)(?:\n^humidity-to-location map:\n)(?P<humidity_to_location>(?:^.+\n?)+)', 
					flags=re.MULTILINE)
	maps = regex.search(inputfile.read())
	maps = {
		'seeds' : [int(x) for x in maps.group('seeds').strip().split()],
		'seed-to-soil' : [ [int(y) for y in x.split()] for x in maps.group('seed_to_soil').strip().split('\n') ],
		'soil-to-fertilizer' : [ [int(y) for y in x.split()] for x in maps.group('soil_to_fertilizer').strip().split('\n') ],
		'fertilizer-to-water' : [ [int(y) for y in x.split()] for x in maps.group('fertilizer_to_water').strip().split('\n') ],
		'water-to-light' : [ [int(y) for y in x.split()] for x in maps.group('water_to_light').strip().split('\n') ],
		'light-to-temperature' : [ [int(y) for y in x.split()] for x in maps.group('light_to_temperature').strip().split('\n') ],
		'temperature-to-humidity' : [ [int(y) for y in x.split()] for x in maps.group('temperature_to_humidity').strip().split('\n') ],
		'humidity-to-location' : [ [int(y) for y in x.split()] for x in maps.group('humidity_to_location').strip().split('\n') ]
	}

	def get_destination(almanac:list, source:int):
		destination = None
		for rangemap in almanac:
			source_range = range(rangemap[1], rangemap[1] + rangemap[2])
			destination_range = range(rangemap[0], rangemap[0] + rangemap[2])
			if source in source_range:
				destination = destination_range[source_range.index(source)]
		return destination if destination else source

	# Find the information for each seed
	seedinfo = []
	for seed in maps.get('seeds'):
		soil = get_destination(maps.get('seed-to-soil'), seed)
		fertilizer = get_destination(maps.get('soil-to-fertilizer'), soil)
		water = get_destination(maps.get('fertilizer-to-water'), fertilizer)
		light = get_destination(maps.get('water-to-light'), water)
		temperature = get_destination(maps.get('light-to-temperature'), light)
		humidity = get_destination(maps.get('temperature-to-humidity'), temperature)
		location = get_destination(maps.get('humidity-to-location'), humidity)
		
		seedinfo.append( {
			'seed': seed,
			'soil': soil,
			'fertilizer': fertilizer,
			'water': water,
			'light': light,
			'temperature': temperature,
			'humidity': humidity,
			'location': location
		} )

	# First answer, lowest location of any seed.
	print("Answer 1: {}".format(min([x.get('location') for x in seedinfo])))