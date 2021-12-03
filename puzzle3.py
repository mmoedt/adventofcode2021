#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main(args):
    print("Hello!")
    print("args: %(args)s" % locals())

    product = puzB('input3.txt')
    #product = puzB('test3.txt')
    print("puz: { life: %(product)d }" % locals())


def puz(infile):
    horiz, depth, aim = 0, 0, 0

    counts = []
    first = True
    with open(infile, 'r') as infile:
        for line in infile:
            if first:
                first = False
                for i in range(0, len(line) - 1):
                    counts.append(0)
            for i in range(0, len(line) - 1):
                if line[i] == '1':
                    counts[i] += 1
                else:
                    counts[i] -= 1

    print("counts: %(counts)s", locals())
    gamma_str = ''
    epsilon_str = ''
    for i in range(0, len(counts)):
        digit1 = '1' if counts[i] >= 0 else '0'
        digit2 = '0' if counts[i] >= 0 else '1'
        gamma_str += digit1
        epsilon_str += digit2

    print("gamma: %(gamma_str)s" % locals())
    print("epsil: %(epsilon_str)s" % locals())
    gamma = int(gamma_str, 2)
    epsilon = int(epsilon_str, 2)

    # print("final locals: %s" % (locals(),))
    product = gamma * epsilon
    return product

def puzB(infile):
    horiz, depth, aim = 0, 0, 0

    oxies = []
    scrubs = []
    with open(infile, 'r') as infile:
        for line in infile:
            oxies.append(line)
            scrubs.append(line)

    def count(lines):
        first = True

        counts = []
        for line in lines:
            if first:
                first = False
                for i in range(0, len(line) - 1):
                    counts.append(0)
            for i in range(0, len(line) - 1):
                if line[i] == '1':
                    counts[i] += 1
                else:
                    counts[i] -= 1
        return counts

    i = 0

    while len(oxies) > 1 and i < 12:
        counts = count(oxies)
        print("---------------------------------")
        print("oxies len: %s, i: %d" % (len(oxies), i))
        if len(oxies) < 12:
            print("oxies: %s" % '\n' + ''.join(oxies))
            print("counts: %s" % (counts, ))
        oxies2 = []
        if counts[i] >= 0:  # 1 is most common or equal
            if len(oxies) < 12:
                print('1 is more common or equal, count-val: %d' % (counts[i],))
            for val in oxies:
                if val[i] == '1':
                    oxies2.append(val)
        else:  # 0 is most common
            if len(oxies) < 12:
                print('0 is more common, count-val: %d' % (counts[i],))
            for val in oxies:
                if val[i] == '0':
                    oxies2.append(val)
        oxies = oxies2[:]
        i += 1


    i = 0
    while len(scrubs) > 1 and i < 12:
        counts = count(scrubs)
        print("---------------------------------")
        print("scrubs len: %s, i: %d" % (len(scrubs), i))
        if len(scrubs) < 12:
            print("scrubs: %s" % '\n' + ''.join(scrubs))
            print("counts: %s" % (counts, ))
        scrubs2 = []
        if counts[i] >= 0:  # 1 is most common, or equal
            if len(scrubs) < 12:
                print('1 is more common or equal, count-val: %d' % (counts[i],))
            for val in scrubs:
                if val[i] == '0':
                    scrubs2.append(val)
        else:  # 0 is most common
            if len(scrubs) < 12:
                print('0 is most common or equal, count-val: %d' % (counts[i],))
            for val in scrubs:
                if val[i] == '1':
                    scrubs2.append(val)
        scrubs = scrubs2[:]
        i += 1


    print("oxies: %(oxies)s, scrubs: %(scrubs)s" % locals())

    oxy = int(oxies[0], 2)
    scrub = int(scrubs[0], 2)

    # print("final locals: %s" % (locals(),))
    product = oxy * scrub
    return product

# Q. Can I do this in a parallel way?
# Load the data into a list, split up the list up (determine indicies),
# get each thread to work on a shared array (potentially saving in another array)
# and return their counts at the end


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
