#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main(args):
    print("Hello!")
    print("args: %(args)s" % locals())

    print("meth3: %d" % (meth3()))
    print("windows1: %d" % (windows1()))
    print("windows2: %d" % (windows2()))


def meth3():
    increases = 0
    vals = []
    with open('input1.txt', 'r') as infile:
        for line in infile:
            vals.append(int(line))

    for i in range(1, len(vals)):
        delta = vals[i] - vals[i-1]
        if delta > 0:
            increases += 1

    return increases


def windows1():
    increases = 0
    vals = []
    with open('input1.txt', 'r') as infile:
        for line in infile:
            vals.append(int(line))

    for i in range(3, len(vals)):
        delta = ( vals[i] + vals[i-1] + vals[i-2] ) - \
                 ( vals[i-1] + vals[i-2] + vals[i-3] )
        if delta > 0:
            increases += 1

    return increases

def windows2():
    increases = 0
    vals = []
    with open('input1.txt', 'r') as infile:
        for line in infile:
            vals.append(int(line))

    for i in range(3, len(vals)):
        delta = vals[i] - vals[i-3]
        if delta > 0:
            increases += 1

    return increases


## Q. Can I do this in a parallel way?
# Load the data into a list, split up the list up (determine indicies),
# get each thread to work on a shared array (potentially saving in another array)
# and return their counts at the end

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
