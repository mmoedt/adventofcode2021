#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from util import debug


def main(args):
    test_ages = [3,4,3,1,2]
    puz(test_ages, 18, True)
    puz(test_ages, 80)

    with open('input/input6.txt', 'r') as infile:
        line = infile.readline()
        fishies = [int(s, 10) for s in line.strip().split(',')]

    puz(fishies, 256)

    return 0


def debug(myobj):
    global verbose
    if verbose:
        print(str(myobj))


def getNextFishDays(fishDays):
    newFishies = []
    newDays = [i-1 for i in fishDays]
    for i in range(0, len(newDays)):
        if newDays[i] == -1:
            newDays[i] = 6
            newFishies.append(8)
    return newDays[:] + newFishies[:]


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


def puz(fishDays, days, beVerbose=False):
    #puzA(fishDays, days, beVerbose)
    puzB(fishDays, days, beVerbose)


def puzA(fishDays, days, beVerbose=False):
    global verbose
    verbose = beVerbose

    print("Initial state:   %s" % (','.join([str(i) for i in fishDays]),))
    for i in range(1, days+1):
        fishDays = getNextFishDays(fishDays)
        debug("After %05d days: %s" % (i, ','.join([str(i) for i in fishDays]),))

    print("Total at end: %d" % (len(fishDays),))
    return


def puzB(fishDays, totalDays, beVerbose=False):
    global verbose
    verbose = beVerbose

    print("Initial state:   %s" % (','.join([str(i) for i in fishDays]),))

    global fishAges
    fishAges = {}
    for i in range(0,9):
        fishAges[i] = 0

    # Count up each of the fish, according to due days
    for fd in fishDays:
        fishAges[fd] += 1

    print("Initially: %d fish" % (getTotal(),))

    for i in range(1, totalDays+1):
        addDayForAges()
        debug("After %5d days: %s" % (i, fishAges))

    print("Total at %3d: %d" % (totalDays, getTotal()))

    return


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
