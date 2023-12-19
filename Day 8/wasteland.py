#!/usr/bin/env python

import re

START = 'AAA'
DESTINATION = 'ZZZ'

def moveToTop(l: list, item: str) -> list:
    for i, location in enumerate(l):
        if location[0] == item:
            l.insert(0, l.pop(i))
            break
    return l

with open(r'./input.txt', mode='r', encoding='utf-8') as inputfile:
    regex = re.compile(r'^(?P<location>\w+)(?: = \()(?P<left>\w+)(?:. )(?P<right>\w+)')
    lines = inputfile.read().splitlines()
    directions = lines[0].strip()

    locations = []
    for line in lines[2:]:
        match = regex.match(line)
        if match:
            locations.append((match.group('location'), (match.group('left'), match.group('right'))))

    # We set the START at the beginning
    locations =  moveToTop(locations, START)

    found = False
    steps = -1
    while not found:
        for direction in directions:
            steps += 1
            if locations[0][0] != DESTINATION:
                print(locations[0], direction)
                if direction == 'R':
                    locations = moveToTop(locations, locations[0][1][1])
                if direction == 'L':
                    locations = moveToTop(locations, locations[0][1][0])
            else:
                found = True
                break

    print("Answer 1: {}".format(steps))
