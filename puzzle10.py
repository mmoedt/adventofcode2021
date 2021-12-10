#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import sys
from util import *


def main(args):

    test_find_corruption()

    puz_data = read_parse_data('input/input10.txt')
    puz_a(puz_data)

    puz_data = read_parse_data('input/input10.txt')
    puz_b(puz_data)
    return 0


def test_find_corruption():
    test_cases = [
        ("{([(<{}[<>[]}>{[]{[(<()>", "]", "}"),
        ("[[<[([]))<([[{}[[()]]]", "]", ")"),
        ("[{[{({}]{}}([{[{{{}}([]", ")", "]"),
        ("[<(<(<(<{}))><([]([]()", ">", ")"),
        ("<{([([[(<>()){}]>(<<{{", "]", ">"),
    ]
    for pattern, expected, result in test_cases:
        right, wrong = find_corruption(pattern)
        expect(right, expected, pattern)
        expect(wrong, result, pattern)


def find_corruption(pattern):
    char_stack = [list(pattern)[0]]
    open_enders = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>',
    }
    for char in list(pattern)[1:]:
        if char in open_enders.keys():
            char_stack.append(char)
        elif char not in open_enders.values():
            raise Exception("Got a non-closing character!?")
        else:
            top_char = char_stack[-1:][0]
            debug(f"Got closing char '{char}', top_char: '{top_char}', Stack: {char_stack}")
            expected = open_enders[top_char]
            if char == expected:
                char_stack.pop()
            else:
                debug(f"Invalid char!  Got closing char '{char}', top_char: '{top_char}', expect '{expected}', Stack: {char_stack}")
                return expected, char

    return '', ''  # signifies it's okay


def find_missing(pattern):
    char_stack = [list(pattern)[0]]
    open_enders = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>',
    }
    for char in list(pattern)[1:]:
        if char in open_enders.keys():
            char_stack.append(char)
        elif char not in open_enders.values():
            raise Exception("Got a non-closing character!?")
        else:
            top_char = char_stack[-1:][0]
            expected = open_enders[top_char]
            if char == expected:
                char_stack.pop()
            else:
                raise Exception(f"Invalid char!  Got closing char '{char}', top_char: '{top_char}', expect '{expected}', Stack: {char_stack}")

    char_stack.reverse()
    needed_end = [open_enders[c] for c in char_stack]
    return needed_end


def get_points_a(c):
    point_map = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }
    if c in point_map.keys():
        return point_map[c]
    else:
        print(f"Not in point map! c: {c}")


def get_points_b(c):
    point_map = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4,
    }
    if c in point_map.keys():
        return point_map[c]
    else:
        print(f"Not in point map! c: {c}")


def read_parse_data(filename, beVerbose=False):
    set_verbose(beVerbose)
    data = []

    with open(filename, 'r') as infile:
        for line in infile.readlines():
            data.append(line.strip())
            debug(f"input: {line.strip()}")

    return data


def puz_a(data, verbose=False):
    set_verbose(verbose)

    print("## Running puzzle, part A")

    points = 0
    for pattern in data:
        right, wrong = find_corruption(pattern)
        if right != '':
            points += get_points_a(wrong)

    print(f"Total points: {points}")

    return


def puz_b(data, verbose=False):
    set_verbose(verbose)

    print("## Running puzzle, part B")

    okay_lines = []
    for pattern in data:
        right, wrong = find_corruption(pattern)
        if right == '':
            okay_lines.append(pattern)
        else:
            pass  # ignore corrupted ones

    # debug(f"Okay lines: {okay_lines}")

    all_points = []
    for line in okay_lines:
        missing = find_missing(line)
        # debug(f"missing: {missing}")
        points = 0
        for char in list(missing):
            points *= 5
            points += get_points_b(char)
        # debug(f"  so points: {points}")
        all_points.append(points)

    all_points.sort()
    mid_idx = int(len(all_points) / 2)
    debug(f"all_points: {all_points}, mid_idx: {mid_idx}")
    middle = all_points[mid_idx]
    print(f"Middle points: {middle}")

    return


if __name__ == '__main__':
    sys.exit(main(sys.argv))
