#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import sys
from util import *


def main(args):

    # tests1()

    # test_data = read_parse_data('input/test9.txt', True)
    # puzA(test_data, True)
    # puz_data = read_parse_data('input/input9.txt')
    # puzA(puz_data)
    # Got it:
    # 425

    # test_data = read_parse_data('input/test9.txt')
    # puzB(test_data, True)
    puz_data = read_parse_data('input/input9.txt')
    puzB(puz_data)
    return 0


def show_map(data):
    global low_spots
    for x in range(0, len(data)):   # NOTE: x and y here are backward compared to convention .. x goes down, y goes across
        out_line = ''
        for y in range(0, len(data[0])):
            if [x, y] in low_spots:
                out_line += bolded(data[x][y])
            else:
                out_line += data[x][y]
        print(out_line)


def show_basin(data, basin):
    global low_spots
    for x in range(0, len(data)):   # NOTE: x and y here are backward compared to convention .. x goes down, y goes across
        out_line = ''
        for y in range(0, len(data[0])):
            if [x, y] in low_spots:
                out_line += bright_redded(data[x][y])
            elif [x, y] in basin:
                out_line += bolded(data[x][y])
            else:
                out_line += data[x][y]
        print(out_line)
    print('-----------------------------------')


def read_parse_data(filename, beVerbose=False):
    set_verbose(beVerbose)
    data = []

    with open(filename, 'r') as infile:
        for line in infile.readlines():
            data.append(list(line.strip()))
            debug(f"input: {line.strip()}")

    debug(f"data: {data}")
    return data


def explore_from(data, spot):
    global travelled
    global low_spots
    if spot in travelled:
        debug(f"Not exploring ({spot[0]}, {spot[1]}), been there already..")
        return  # don't go over again

    debug(f"Exploring: ({spot[0]}, {spot[1]})")
    travelled.append(spot)

    adjacents = get_adjacent(data, [spot[0],spot[1]])
    found_lower = False
    all_equal = True
    for adj in adjacents:
        debug(f"Comparing spot: '{adj}' with spot: '{spot}'")
        if data[adj[0]][adj[1]] != data[spot[0]][spot[1]]:
            all_equal = False
        if data[adj[0]][adj[1]] < data[spot[0]][spot[1]]:
            explore_from(data, adj)
            found_lower = True

    if (not found_lower) and (not all_equal):
        low_spots.append(spot)

    return


def explore_basin_from(data, spot, basin):
    global travelled
    global low_spots
    if spot in travelled:
        debug(f"Not exploring ({spot[0]}, {spot[1]}), been there already..")
        return basin  # don't go over again

    debug(f"Exploring: ({spot[0]}, {spot[1]})")
    travelled.append(spot)

    adjacents = get_adjacent(data, [spot[0],spot[1]])
    for adj in adjacents:
        if data[adj[0]][adj[1]] != '9':  # off-limits, not included
            if adj not in basin:
                basin.append(adj)
            basin = explore_basin_from(data, adj, basin)  # hmmm..

    return basin


def get_adjacent(data, spot):
    max_x = len(data) - 1
    max_y = len(data[0]) - 1
    adjacents = []
    if spot[0] > 0:
        adjacents.append([spot[0]-1, spot[1]])
    if spot[0] < max_x:
        adjacents.append([spot[0] + 1, spot[1]])
    if spot[1] > 0:
        adjacents.append([spot[0], spot[1] - 1])
    if spot[1] < max_y:
        adjacents.append([spot[0], spot[1] + 1])
    return adjacents


def puzA(data, verbose=False):
    set_verbose(verbose)

    print("## Running puzzle, part A")

    global travelled, low_spots
    travelled = []
    low_spots = []

    if verbose:
        show_map(data)

    for x in range(0, len(data)):   # NOTE: x and y here are backward compared to convention .. x goes down, y goes across
        for y in range(0, len(data[0])):
            explore_from(data, [x, y])

    show_map(data)

    print(sum([ int(data[spot[0]][spot[1]], 10) + 1 for spot in low_spots ]))

    return


def puzB(data, verbose=False):
    set_verbose(verbose)
    print("## Running puzzle, part B")

    global travelled, low_spots, basins
    basins = []  # list of lists of points (which are lists of x,y values)
    # puzB depends on puzA running first and getting our low spots
    puzA(data, verbose)

    travelled = []  # re-used
    for point in low_spots:
        basin = explore_basin_from(data, point, [point,])
        basins.append(basin)

    for basin in basins:
        show_basin(data, basin)

    basin_points = [len(basin) for basin in basins]
    basin_points.sort()

    print(f"highest points: {basin_points[-3:]}")
    product = 1
    for val in basin_points[-3:]:
        product *= val
    print(f"product is {product}")

    return


if __name__ == '__main__':
    sys.exit(main(sys.argv))
