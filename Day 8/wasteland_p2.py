#!/usr/bin/env python

###############################################################################
# Doesn't need to be multithreaded (multiprocess?) but I wanted to try
# some multithreading stuff and it looked geared towards it (it wasn't really,
# unless you were bruteforcing it).
###############################################################################


import re
import multiprocessing
from math import lcm

WORKERS = 6


def findZeds(info: tuple) -> tuple:
    location, directions, locations, destinations = info
    steps, loc = location
    while loc not in destinations or steps == location[0]:
        for dir in directions:
            left, right = locations[loc]
            if dir == "L":
                loc = left
            if dir == "R":
                loc = right
            steps += 1
            if loc in destinations:
                break
    return (steps, loc)


if __name__ == "__main__":
    with open(r"./input.txt", mode="r", encoding="utf-8") as inputfile:
        regex = re.compile(r"(\w+)(?: = \()(\w+)(?:. )(\w+)(?:\)\n?)")
        directions, locations = inputfile.read().split("\n\n")
        locations = {x: (y, z) for x, y, z in regex.findall(locations)}

        # For start_locs, the tuples are formatted as: (steps, location)
        # fmt:off
        start_locs = list(map(lambda x: (0, x), filter(lambda x: re.match(r"\w\wA", x), locations)))
        end_locs = list(filter(lambda x: re.match(r"\w\wZ", x), locations))
        # fmt: on

        with multiprocessing.Pool(processes=WORKERS) as pool:
            payloads = [(sl, directions, locations, end_locs) for sl in start_locs]
            slopes = pool.map(findZeds, payloads)  # Blocks until result.
            slopes = [x for x, _ in slopes]  # Keep only the steps.
            print(slopes)
            print(lcm(*slopes))
