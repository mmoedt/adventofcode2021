#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re


def main(args):
    test_ages = [3,4,3,1,2]
    puz(test_ages, 18, True)
    puz(test_ages, 80)

    with open('input6.txt', 'r') as infile:
        line = infile.readline()
        fishies = [int(s, 10) for s in line.strip().split(',')]
        puz(fishies, 256)

    return 0

def debug(myobj):
    global verbose
    if verbose:
        print(str(myobj))

def addDayForAges():
    global fishAges
    for i in range(0, 9):
        fishAges[i-1] = fishAges[i]
    fishAges[8] = fishAges[-1] # new fish
    fishAges[6] += fishAges[-1] # renewed fish
    fishAges[-1] = 0 # done with these guys

def getTotal():
    global fishAges
    return sum(fishAges.values())

def puz(fishDays, totalDays, beVerbose=False):
    global verbose
    verbose = beVerbose

    print("Initial state:   %s" % (','.join([str(i) for i in fishDays]),))

    global fishAges
    fishAges = {}
    for i in range(0,9):
        fishAges[i] = 0

    # Add counts for each of the fish
    for fd in fishDays:
        fishAges[fd] += 1

    print("Initially: %d fish" % (getTotal(),))

    for i in range (1, totalDays+1):
        addDayForAges()
        debug("After %5d days: %s" % (i, fishAges))

    print("Total at %3d: %d" % (totalDays, getTotal()))

    return


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
