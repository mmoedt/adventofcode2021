#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main(args):
    print("Hello!")
    print("args: %(args)s" % locals())

    print("meth1: %d" % (meth1()))
    print("meth2: %d" % (meth2()))


def meth1():
    increases = 0
    with open('input1.txt', 'r') as infile:
        last = int(infile.readline())
        nextline = infile.readline()
        while nextline:
            value = int(nextline)
            delta = value - last
            if delta > 0:
                increases += 1
            last = value
            nextline = infile.readline()
    return increases


def meth2():
    increases = 0
    with open('input1.txt', 'r') as infile:
        first = True
        for line in infile:
            if first:
                first = False
                last = int(line)
            else:
                delta = int(line) - last
                last = int(line)
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
