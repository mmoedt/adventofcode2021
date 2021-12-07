#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main(args):
    print("Hello!")
    print("args: %(args)s" % locals())

    product = p2b('input/input2.txt')
    print("p2b: { product: %(product)d }" % locals())


def p2b(infile):
    global horiz, depth, aim
    horiz, depth, aim = 0, 0, 0

    def forward(val):
        global horiz, depth
        horiz += val
        depth += (aim * val)

    def down(val):
        global aim
        aim += val

    def up(val):
        global aim
        aim -= val

    # Note: long way to go as an alternative to a switch statement
    opts = {
        'forward': forward,
        'down': down,
        'up': up,
    }

    cmds = []
    vals = []

    with open(infile, 'r') as infile:
        for line in infile:
            cmd, val = line.split(' ')
            cmds.append(cmd)
            vals.append(int(val))

    for i in range(0, len(vals)):
        val = vals[i]
        cmd = cmds[i]

        if cmd not in opts:
            print("ERROR IN IF-ELSE BLOCK; got '%s'" % (cmd,))
        else:
            opts[cmd](val) # instead of a switch statement..

        # print("locals: %s" % (locals(),))
        # if cmds[i] == 'forward':
        #     horiz += val
        #     depth += (aim * val)
        # elif cmds[i] == 'down':
        #     aim += val
        # elif cmds[i] == 'up':
        #     aim -= val
        # else:
        #     print("ERROR IN IF-ELSE BLOCK; got '%s'" % (cmds[i],))

    # print("final locals: %s" % (locals(),))
    product = horiz * depth
    return product

# Q. Can I do this in a parallel way?
# Load the data into a list, split up the list up (determine indicies),
# get each thread to work on a shared array (potentially saving in another array)
# and return their counts at the end


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
