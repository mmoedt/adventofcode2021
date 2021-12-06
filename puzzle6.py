#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

def main(args):

    #puz('input6.txt')
    #test_ages = [3,4,3,1,2]
    #puz(test_ages, True)

    with open('input6.txt', 'r') as infile:
        line = infile.readline()
        fishies = [ int(s, 10) for s in line.strip().split(',') ]
        puz(fishies)

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

def puz(fishDays, beVerbose=False):
    global verbose
    verbose = beVerbose

    print("Initial state:   %s" % (','.join([str(i) for i in fishDays]),))
    for i in range(1, 18+1):
        fishDays = getNextFishDays(fishDays)
        debug("After %05d days: %s" % (i, ','.join([str(i) for i in fishDays]),))

    print("Total at end: %d" % (len(fishDays),))
    return


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
