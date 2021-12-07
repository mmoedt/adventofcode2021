#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

def main(args):
    puz('input/test5.txt', True)
    puz('input/input5.txt', False)
    return 0


def debug(myobj):
    global verbose
    if verbose:
        print(str(myobj))


def resetPoints():
    global points
    points = {}


def incrPoint(x,y):
    global points
    i = '%d,%d' % (x,y)
    if i in points.keys():
        points[i] += 1
    else:
        points[i] = 1


def markFromLine(x1, y1, x2, y2):
    if x1 == x2:  # vertical
        if y1 > y2:
            st = y2
            end = y1
        else:
            st = y1
            end = y2
        for i in range(st, end+1):
            incrPoint(x1, i)
    elif y1 == y2:  # horizonal
        if x1 > x2:
            st = x2
            end = x1
        else:
            st = x1
            end = x2
        for i in range(st, end+1):
            incrPoint(i, y1)
        pass
    else:  # diagonal
        incrPoint(x1,y1)
        debug("diag from %d,%d to %d,%d" % (x1,y1,x2,y2))
        while x1 != x2:  # it must match if conditions are as prescribed
            if x1 < x2:
                x1 += 1
            else:
                x1 -= 1
            if y1 < y2:
                y1 += 1
            else:
                y1 -= 1
            debug("computing diag point %d,%d" % (x1, y1))
            incrPoint(x1,y1)


def countOfMultiples():
    global points
    return sum([ 1 for val in points.values() if val > 1])


def puz(infile, beVerbose=False):
    global verbose
    verbose = beVerbose

    resetPoints()

    with open(infile, 'r') as infile:
        line_pattern_expr = r'(?P<x1>\d+),(?P<y1>\d+) -> (?P<x2>\d+),(?P<y2>\d+)'
        line_pat = re.compile(line_pattern_expr)
        for line in infile:
            line = line.strip()
            match = line_pat.match(line)
            x1,y1,x2,y2 = [ int(i) for i in list(match.groups()) ]
            markFromLine(x1,y1,x2,y2)
        global points
        debug({ 'points': points })
        print({ 'count': countOfMultiples() })

    return


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
