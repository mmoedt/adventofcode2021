#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main(args):
    print("Hello!")
    print("args: %(args)s" % locals())

    print("m1: %d" % (method1()))
    print("m2: %d" % (method2()))
    print("m3: %d" % (method3()))
    print("windows1: %d" % (windows1()))
    print("windows2: %d" % (windows2()))


def method1():
    increases = 0
    with open('input/input1.txt', 'r') as infile:
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


def method2():
    increases = 0
    with open('input/input1.txt', 'r') as infile:
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


def method3():
    increases = 0
    vals = []
    with open('input/input1.txt', 'r') as infile:
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
    with open('input/input1.txt', 'r') as infile:
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
    with open('input/input1.txt', 'r') as infile:
        for line in infile:
            vals.append(int(line))

    for i in range(3, len(vals)):
        delta = vals[i] - vals[i-3]
        if delta > 0:
            increases += 1

    return increases


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
