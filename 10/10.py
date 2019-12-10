import sys
from itertools import chain
import math

comets = [line.strip() for line in sys.stdin.readlines()]
height = len(comets)
width = len(comets[0])

board = [[0 for c in range(width)] for r in range(height)]

def on_board(r, c, board):
    if r >= len(board) or c >= len(board[0]) or r < 0 or c < 0:
        return False
    return True

def recadd(r, c, dr, dc, comets, board):
    r += dr
    c += dc
    if not on_board(r, c, board) or comets[r][c] == "#" :
        return
    board[r][c] += 1
    recadd(r, c, dr, dc, comets, board)

def simpdir(direc):
    dx, dy = direc
    gcd = math.gcd(dx, dy)
    if (dx, dy) == (0, 0):
        return (0,0)
    elif gcd == 1:
        return direc
    else:
        return (dx // gcd, dy // gcd)

for r in range(height):
    for c in range(width):
        if comets[r][c] != "#":
            continue
        # increment one when direct line of sight
        handleddirs = []
        for r2 in range(height):
            for c2 in range(width):
                direc = simpdir((r2-r, c2-c))
                if direc in handleddirs or direc == (0,0):
                    continue
                handleddirs.append(direc)
                recadd(r, c, direc[0], direc[1], comets, board)

# find pos with max comets in direct line of sight
maxx = -1
maxy = -1
maxval = -1
for r in range(height):
    for c in range(width):
        val = board[r][c]
        if val > maxval:
            maxval = val
            maxx = r
            maxy = c
print("%d: (%d, %d)" % (maxval, maxx, maxy))