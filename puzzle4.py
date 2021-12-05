#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main(args):
    puzA_test('test4.txt', True)
    puzA('input4.txt')

    return 0

def debug(myobj):
    global verbose
    if verbose:
        print(str(myobj))

def bold(s):
    return '\u001b[1m' + s + '\u001b[0m'

def markBoards(num, evenIfWon=True):
    global boardMarks, boards, lastDraw
    for i in range(0, len(boards)):
        board = boards[i]
        for j in range(0, len(board)):
            boardline = board[j]
            for k in range(0, len(boardline)):
                if int(boardline[k], 10) == int(num, 10):
                    if (not bingos[i]) or evenIfWon:
                        debug({'_msg': 'got one!', num:num, i: i, j: j, k: k})
                        boardMarks[i][j][k] = '0'
    lastDraw = num


def showBoards():
    global boardMarks, boards, bingos, winningDraws
    output = ''
    for i in range(0, len(boards)):
        if bingos[i]:
            output += 'board %d:\n' % (i,)
        else:
            output += 'board %d: won via %s, winningDraw: %s\n' % (i, bingos[i], winningDraws[i])

        for j in range(0, len(boards[i])):
            for k in range(0, len(boards[i][j])):
                val = int(boards[i][j][k], 10)
                if boardMarks[i][j][k] == '1':
                    output += ' %02d' % val
                else:
                    output += bold(' %02d' % val)
            output += '\n'
        output += '\n'
    print(output)


def initDataUsingBoards():
    global boards, boardMarks, bingos, winningDraws, winners
    boardMarks = []
    bingos = []
    winningDraws = []
    winners = []

    for i in range(0, len(boards)):
        boardMarks.append([])
        bingos.append('')
        winningDraws.append('')
        for j in range(0, len(boards[i])):
            boardMarks[i].append([])
            for k in range(0, len(boards[i][j])):
                boardMarks[i][j].append('1')


def checkBoards():
    global boardMarks, boards, bingos, lastDraw, winningDraws, winners
    someoneWon = False
    for i in range(0, len(boards)):
        for j in range(0, len(boards[i])):
            for k in range(0, len(boards[i][j])):
                if boardMarks[i][j][k] == '1':
                    break
                elif k == (len(boards[i][j]) - 1):
                    if bingos[i] == '':  # or bingos[i] == 'col':
                        # got to the last mark on this row!
                        print({'_msg': 'BINGO!', 'i': i, 'j': j, 'k': k})
                        bingos[i] += 'row'
                        winningDraws[i] = lastDraw
                        winners.append(i)
                        someoneWon = True

    for i in range(0, len(boards)):
        for k in range(0, len(boards[i][0])):
            for j in range(0, len(boards[i])):
                if boardMarks[i][j][k] == '1':
                    break
                elif j == (len(boards[i]) - 1):
                    if bingos[i] == '':  # or bingos[i] == 'row':
                        # got to the last mark on this column!
                        print({'_msg': 'BINGO!', 'i': i, 'j': j, 'k': k})
                        bingos[i] += 'col'
                        winningDraws[i] = lastDraw
                        winners.append(i)
                        someoneWon = True
    return someoneWon


def getBoardSums():
    boardSums = []
    for i in range(0, len(boards)):
        boardSums.append(0)
        for j in range(0, len(boards[i])):
            for k in range(0, len(boards[i][j])):
                boardSums[i] += int(boards[i][j][k], 10) * int(boardMarks[i][j][k], 10)
    return boardSums


def showScores():
    global lastDraw, boards, winningDraws
    boardSums = getBoardSums()
    print({'boardSums': boardSums})
    for i in range(0, len(boards)):
        if bingos[i] != '':
            score = boardSums[i] * int(winningDraws[i], 10)
            print("Winning board #%d, score: %d" % (i, score))


def puzA(infile, beVerbose=False):

    global verbose
    verbose = beVerbose

    global boards, boardMarks, bingos, lastDraw, winningDraws, winners
    boards = []

    with open(infile, 'r') as infile:
        draws = infile.readline().strip().split(',')
        debug(str({"draws": draws}))
        infile.readline()
        i = 0
        nextline = infile.readline()
        while nextline:
            boards.append([])
            for j in range(0,5):
                boards[i].append(nextline.strip().split())
                nextline = infile.readline()
            nextline = infile.readline() # remove extra newline .. expected
            i += 1

    initDataUsingBoards()

    debug(str({"boards": boards}))

    showBoards()

    debug({"at": "before"})

    for i in range(0, len(draws)):
        print("drawing ... %s" % draws[i])
        markBoards(draws[i], evenIfWon=False)
        if checkBoards():
            showBoards()
            showScores()

    showScores()
    print("Winning draws: " + str(winningDraws))
    print("Winners order: " + str(winners))
    return


def puzA_test(infile, beVerbose=False):
    global verbose
    verbose = beVerbose

    global boards, boardMarks, bingos, lastDraw, winningDraws, winners
    boards = []

    with open(infile, 'r') as infile:
        draws = infile.readline().strip().split(',')
        debug(str({"draws": draws}))
        infile.readline()
        i = 0
        nextline = infile.readline()
        while nextline:
            boards.append([])
            for j in range(0, 5):
                boards[i].append(nextline.strip().split())
                nextline = infile.readline()
            nextline = infile.readline()  # remove extra newline .. expected
            i += 1

    initDataUsingBoards()

    debug(str({"boards": boards}))

    showBoards()

    debug({"at": "before"})

    # First test case
    for i in range(0, 5):
        markBoards(draws[i])
        checkBoards()

    debug({"at": "after 5"})
    showBoards()

    # Second test case
    for i in range(5, 11):
        markBoards(draws[i])
        checkBoards()

    debug({"at": "after 11"})
    showBoards()

    # Third test case
    for i in range(11, 12):
        markBoards(draws[i])
        checkBoards()

    debug({"at": "after 12"})
    showBoards()

    showScores()
    print("Winners: " + str(winners))
    # for i in range(12, len(draws)):
    #     markBoards(draws[i])
    #     checkBoards()
    #
    # debug({"at": "after the end"})
    # print(showBoards())

    return


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
