#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from util import do_switch

def main(args):
    print("Hello!")
    print("args: %(args)s" % locals())

    product = get_product('input/input2.txt')
    print("The computed product is: %(product)s" % locals())
    return 0  # fini


def get_product(infile_name):

    global horiz, aim, depth
    horiz, aim, depth = 0, 0, 0

    def case_up(args):
        global aim
        aim -= args[0]
    def case_down(args):
        global aim
        aim += args[0]
    def case_forward(args):
        global horiz, depth
        horiz += args[0]
        depth += (aim * args[0])
    def case_default(args):
        print("ERROR IN IF-ELSE BLOCK; got args '%s'" % (args,))

    operations = []
    with open(infile_name, 'r') as infile:
        for line in infile:
            cmd, val = line.split(' ')
            operations.append((cmd, int(val)))

    for cmd, val in operations:
        do_switch(locals(), cmd, (val,))

    product = horiz * depth
    return product

####################

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

# fini doSwitch
# 
