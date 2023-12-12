###########################################################################################
# The maps are [Destination start, Source start, Range]                                   #
# So [50, 80, 2], given the range of 2, the destination is [50, 51] and source is [80,81] #
# This means that Seed 81 (source in a seed-to-soil map), would go in Soil 51.            #
###########################################################################################

import re
from functools import reduce


with open(r'./input.txt', mode='r', encoding='utf-8') as inputfile:
	regex = re.compile(r'(?:^seeds: )(?P<seeds>.+$)(?:\n+^seed-to-soil map:\n)(?P<seed_to_soil>(?:^.+\n)+)(?:\n^soil-to-fertilizer map:\n)(?P<soil_to_fertilizer>(?:^.+\n)+)(?:\n^fertilizer-to-water map:\n)(?P<fertilizer_to_water>(?:^.+\n)+)(?:\n^water-to-light map:\n)(?P<water_to_light>(?:^.+\n)+)(?:\n^light-to-temperature map:\n)(?P<light_to_temperature>(?:^.+\n)+)(?:\n^temperature-to-humidity map:\n)(?P<temperature_to_humidity>(?:^.+\n)+)(?:\n^humidity-to-location map:\n)(?P<humidity_to_location>(?:^.+\n?)+)', 
					flags=re.MULTILINE)
	maps = regex.search(inputfile.read())
	maps = {
		'seeds' : [int(x) for x in maps.group('seeds').strip().split()],
		'seeds_p2': [(x, x+y) for x, y in [list(map(int, x.split())) for x in re.findall(r"\d+ \d+", maps.group('seeds').strip())]], # For part 2
		'seed-to-soil' : [ list(map(int, x.split())) for x in maps.group('seed_to_soil').strip().split('\n') ],
		'soil-to-fertilizer' : [ list(map(int, x.split())) for x in maps.group('soil_to_fertilizer').strip().split('\n') ],
		'fertilizer-to-water' : [ list(map(int, x.split())) for x in maps.group('fertilizer_to_water').strip().split('\n') ],
		'water-to-light' : [ list(map(int, x.split())) for x in maps.group('water_to_light').strip().split('\n') ],
		'light-to-temperature' : [ list(map(int, x.split())) for x in maps.group('light_to_temperature').strip().split('\n') ],
		'temperature-to-humidity' : [ list(map(int, x.split())) for x in maps.group('temperature_to_humidity').strip().split('\n') ],
		'humidity-to-location' : [ list(map(int, x.split())) for x in maps.group('humidity_to_location').strip().split('\n') ]
	}

	def get_destination(almanac:list, source:int) -> int:
		for dst, src, size in almanac:
			if source in range(src, src + size):
				return source + dst - src 
		return source

	def get_sinfo(seeds:list, master_almanac:list) -> list:
		locations = []
		for seed in seeds:
			soil = get_destination(master_almanac.get('seed-to-soil'), seed)
			fertilizer = get_destination(master_almanac.get('soil-to-fertilizer'), soil)
			water = get_destination(master_almanac.get('fertilizer-to-water'), fertilizer)
			light = get_destination(master_almanac.get('water-to-light'), water)
			temperature = get_destination(master_almanac.get('light-to-temperature'), light)
			humidity = get_destination(master_almanac.get('temperature-to-humidity'), temperature)
			location = get_destination(master_almanac.get('humidity-to-location'), humidity)
		
			locations.append(location)
		return locations

	# Find the information for each seed
	locations = get_sinfo(maps.get('seeds'), maps)

	# Do something else for part 2 I guess.
	seedranges = maps.get('seeds_p2')
	
	def get_sinfo_range(seedrgs: list, master_almanac: list) -> list:
		rgstages = [master_almanac.get(x) for x in ['seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water', 'water-to-light', 'light-to-temperature', 'temperature-to-humidity', 'humidity-to-location']]

		for rgstage in rgstages:
			seedranges_new = [] # Here we store the ranges after processing the stage
			while seedrgs: # While there are seed ranges left
				start, end = seedrgs.pop() # Pop one from the list
				for destination, source, length in rgstage: # For each mapping in the stage
					overlap_start = max(start, source)	# Beginning of the overlap
					overlap_end = min(end, source + length) # Ending of the overlap
					if overlap_start < overlap_end: # If we have an overlap
						seedranges_new.append((overlap_start - source + destination, overlap_end - source + destination))
						if overlap_start > start: # If the overlap is to the right in the range
							seedrgs.append((start, overlap_start)) # Add the non overlapping section to the seedranges to check after
						if end > overlap_end: # If the overlap is to the left in the range
							seedrgs.append((overlap_end, end)) 
						break # After breaking up the range, stop and go to the next seedrange, this avoids the else in the for-loop.
				else:
					seedranges_new.append((start, end)) # If no overlap in map, add the whole range by itself without any modifications.
			seedrgs = seedranges_new # seedrgs is gonna be empty for the next stage, so we add the newly processed ranges.
		return(seedrgs)


	location_ranges = get_sinfo_range(seedranges, maps)
	print("Answer 1: {}".format(min(locations)))
	print("Answer 2: {}".format(min(location_ranges)[0]))