#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import sys
from util import *


def main(args):

    #puzA('input/test8a.txt', True)
    #puzA('input/input8.txt')
    # Got it:
    # 237

    puzB('input/test8a.txt', True, True)
    puzB('input/test8b.txt')

    puzB('input/input8.txt')
    return 0


def puzA(input_filename, verbose=False):
    set_verbose(verbose)
    print("## Running puzzle, part A")

    with open(input_filename, 'r') as infile:
        tot = 0
        for line in infile.readlines():
            digits_str = line.split('|')[1]
            debug(f'digits_str: {digits_str}')
            tot += len([ word for word in digits_str.split() if len(word) in (2, 3, 4, 7)])
    print(tot)

    return


def puzB(input_filename, only_first=False, verbose=False):
    set_verbose(verbose)
    print("## Running puzzle, part B")

    # Step 1: Input and parse data..
    line_values = []
    with open(input_filename, 'r') as infile:
        total = 0
        for line in infile.readlines():
            signals_str, digits_str = line.strip().split('|')
            signals = signals_str.split()
            digitPatterns = digits_str.split()
            debug(f"input: {line.strip()}")
            debug(f"signals: {signals}")
            debug(f"digitPatterns: {digitPatterns}")
            p2d = getPatternToDigitMapping(signals)
            debug(f"segmentPatternMap: {p2d}")
            line_val_str = ''
            for pat in digitPatterns:
                debug(f"looking up digit for pattern '{pat}'")
                segments = list(pat)
                segments.sort()
                debug(f"segments: {segments}")
                word = ''.join(segments)
                digit = p2d[word]
                debug(f"digit: {digit}")
                line_val_str += str(digit)
            line_value = int(line_val_str, 10)
            print(f"Found line value: {line_value}")
            line_values.append(line_value)

        print(f"Total sum: {bolded(str(sum(line_values)))}")

def getPatternToDigitMapping(signals):

    # Start building association..
    digitMap = {
        1: [s for s in signals if len(s) == 2][0],
        4: [s for s in signals if len(s) == 4][0],
        7: [s for s in signals if len(s) == 3][0],
        8: [s for s in signals if len(s) == 7][0],
    }
    debug(digitMap)

    sigSegs = {}  # map of signals to known possible segments
    for sig in 'abcdefg':
        sigSegs[sig] = list('abcdefg')

    def showDebugInfo():
        debug(f"sigSegs:\n{outMap(sigSegs)}")
        debug(f"digitMap:\n{outMap(digitMap)}")

    showDebugInfo()

    # Reduce using known '1' digit, the known signals can only be 'c' or 'f':
    for sig in digitMap[1]:
        sigSegs[sig] = list('cf')

    # ditto using '4'
    for sig in digitMap[4]:
        sigSegs[sig] = list('bd')

    sig4a = [sig for sig in digitMap[7] if sig not in digitMap[1]][0]
    debug(f"digitMap[7]: {digitMap[7]}, digitMap[1]: {digitMap[1]}, so sig4a: {sig4a}")
    sigSegs[sig4a] = list('a',)

    # Which is the '9'?  0, 6, 9 are missing one segment.. they all have 'a' (which we know)
    # 1,3,4,5,7,9 are missing 'e'
    # but we know 1,4,7 .. 3,5,9 left.. len(3):5, len(5):5, len(9):6

    # 6 digits: 0, 6, 9.   0 and 9 have both c, f .. so we can figure out which is 6 .. A. 6 digits, B. it has only one of c,f
    # plus figuring out 6 tells us which signal is for 'f', and hence 'c'
    cf_sigs = digitMap[1]
    patterns = [sig for sig in signals if len(sig) == 6]
    for pattern in patterns:
        debug(f"Considering '{pattern}' for 6..  digitMap[1]: {digitMap[1]}")
        if not (cf_sigs[0] in pattern and cf_sigs[1] in pattern):
            debug(f" found '{pattern}'")
            digitMap[6] = pattern

    if cf_sigs[0] in list(digitMap[6]):  # f in '6', c not in '6'
        sig4f = cf_sigs[0]
        sig4c = cf_sigs[1]
    else:
        sig4f = cf_sigs[1]
        sig4c = cf_sigs[0]

    sigSegs[sig4f] = list('f')
    sigSegs[sig4c] = list('c')

    showDebugInfo()

    def getSigs(segs):
        keys = []
        for key in sigSegs.keys():
            if sigSegs[key] == segs:
                keys.append(key)
        debug(f"getSigs({segs}): {keys}")
        return keys

    # of 0 and 9, both are 6 digits, but 0 has only one .. same approach
    bd_sigs = [sig for sig in digitMap[4] if sig not in (sig4f, sig4c)]
    patterns = [sig for sig in signals if len(sig) == 6 and sig != digitMap[6]]
    for pattern in patterns:
        debug(f"Considering '{pattern}' for 0 and 9.. bd_sigs: {bd_sigs}")
        if bd_sigs[0] in pattern and bd_sigs[1] in pattern:
            debug(f" found '{pattern}' as '9'")
            digitMap[9] = pattern
        else:
            debug(f" found '{pattern}' as '0'")
            digitMap[0] = pattern

    debug(f"So, we can deduce 'b' and 'd' as well.. bd_sigs: {bd_sigs}, digitMap[0]: {digitMap[0]}")

    if bd_sigs[0] in digitMap[0]:
        sig4b = bd_sigs[0]
        sig4d = bd_sigs[1]
    else:
        sig4b = bd_sigs[1]
        sig4d = bd_sigs[0]

    sigSegs[sig4b] = ['b',]
    sigSegs[sig4d] = ['d',]

    showDebugInfo()

    # We can determine '2'; it has 5 digits, and does not have sig for seg 'f'
    debug("Determining '2'.. (doesn't have sig for 'f')")
    #sig4f = getSigs('f')[0]
    debug(f"sig4f: {sig4f}")
    patt2 = [sig for sig in signals if len(sig) == 5 and sig4f not in sig][0]
    debug(f"found digit 2: {patt2}")
    digitMap[2] = patt2

    # And we know 'c', so (2 and) 3 has it, 5 doesn't
    debug("Determining '5' .. doesn't have sig for 'c'")
    #sig4c = getSigs('c')[0]
    digitMap[5] = [sig for sig in signals if len(sig) == 5 and sig4c not in sig][0]

    showDebugInfo()

    debug("So the remaining 5 digit is '3'")
    digitMap[3] = [sig for sig in signals if len(sig) == 5 and sig != digitMap[2] and sig != digitMap[5]][0]

    showDebugInfo()

    print("## Should have the digit mapping...")

    pat2digits = {}
    # reverse the map.. and sort it!
    for digit in digitMap.keys():
        segments = list(digitMap[digit])
        segments.sort()
        pat2digits[''.join(segments)] = digit;

    print(f"Segments pattern to digit mapping:\n{pat2digits}")

    return pat2digits


def outMap(digitMap: dict) -> str:
    output = ''
    for key in digitMap.keys():
        value = digitMap[key]
        output += f"    [{bolded(str(key))}]: {value}\n"
    return output


if __name__ == '__main__':
    sys.exit(main(sys.argv))
