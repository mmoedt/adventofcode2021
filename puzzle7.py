#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import sys
from util import debug


def main(args):
    global positions
    positions = [16, 1, 2, 0, 4, 7, 2, 1, 2, 14]

    tests_totalFuelForA()
    puzA(True)

    with open('input/input7.txt', 'r') as infile:
        positions = [int(i, 10) for i in infile.readline().strip().split(',')]

    puzA()
    # Got it:
    # Average: 472
    # Checked adjacent values and stopped at local minimum 328, with 339321 fuel.

    positions = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
    tests_fuelForB()
    tests_totalFuelForB()
    puzB(True)

    with open('input/input7.txt', 'r') as infile:
        positions = [int(i, 10) for i in infile.readline().strip().split(',')]

    puzB()
    # Got it:
    # Average: 472
    # Checked adjacent values and stopped at local minimum 471, with 95476244 fuel.

    return 0


def tests_totalFuelForA():
    tests = [(2, 37), (1, 41), (3, 39), (10, 71)]
    for case, expected in tests:
        result = totalFuelForA(case)
        fail_str = "" if result == expected else bold(' *** FAIL ***')
        print(f"Fuel for {case}: {result}, should be {expected}{fail_str}")


def tests_fuelForB():
    tests = [(16, 5, 66), (1, 5, 10), (2, 5, 6), (0, 5, 15), (14, 5, 45)]
    for start, end, expected in tests:
        result = fuelForB(start, end)
        fail_str = "" if result == expected else bold(' *** FAIL ***')
        print(f"Fuel for {start} to {end}: {result}, should be {expected}{fail_str}")


def tests_totalFuelForB():
    tests = [(5, 168), (2, 206)]
    for case, expected in tests:
        result = totalFuelForB(case)
        fail_str = "" if result == expected else bold(' *** FAIL ***')
        print(f"Fuel for {case}: {result}, should be {expected}{fail_str}")


def debug(myobj):
    global verbose
    if verbose:
        print(str(myobj))


def bold(s):
    return '\u001b[1m' + s + '\u001b[0m'


def totalFuelForA(pos):
    global positions
    fuel = 0
    for crab in positions:
        fuel += abs(crab - pos)
    return fuel


def fuelForB(start, end):
    dist = abs(start - end)
    return dist * (dist + 1) / 2


def totalFuelForB(pos):
    global positions
    fuel = 0
    for crab in positions:
        fuel += fuelForB(crab, pos)
    return fuel


def getAvg(x, y):
    return math.floor((x / y) + 0.5)


def tryPosA(pos):
    global positions
    debug(f"Trying {pos}")
    fuel = totalFuelForA(pos)
    debug(f" ... got {fuel} fuel needed.")
    return fuel


def tryPosB(pos):
    global positions
    debug(f"Trying {pos}")
    fuel = totalFuelForB(pos)
    debug(f" ... got {fuel} fuel needed.")
    return fuel


def puzA(beVerbose=False):
    puz(tryPosA, beVerbose)


def puzB(beVerbose=False):
    puz(tryPosB, beVerbose)


def puz(tryPos, beVerbose=False):
    global verbose
    global positions
    verbose = beVerbose

    print("Initial state:   %s" % (positions,))
    total = sum(positions)
    number = len(positions)
    average = getAvg(total, number)

    print(f'Average: {average}')

    # Average is a decent starting point ..
    last = average
    last_val = tryPos(last)
    next = last + 1
    next_val = tryPos(next)
    if next_val < last_val:
        # if going up improves, increase until we stop
        while next_val < last_val:
            last = next
            last_val = next_val
            next += 1
            next_val = tryPos(next)
    else:
        # otherwise try going down; decrease until we stop improving
        next = last - 1
        next_val = tryPos(next)
        while next_val < last_val:
            last = next
            last_val = next_val
            next -= 1
            next_val = tryPos(next)

    print(f'Checked adjacent values and stopped at local minimum {last}, with {last_val} fuel.')

    return


if __name__ == '__main__':
    sys.exit(main(sys.argv))
