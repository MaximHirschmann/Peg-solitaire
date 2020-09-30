from copy import deepcopy
from time import time

def solve1():
    def toTuple(l):
        return tuple(map(tuple, l))
        
    # 0: empty
    # 1: pin
    # 2: not on board
    board0 = [
        [2, 2, 1, 1, 1, 2, 2],
        [2, 2, 1, 1, 1, 2, 2],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [2, 2, 1, 1, 1, 2, 2],
        [2, 2, 1, 1, 1, 2, 2]
    ]
    l = len(board0)
    
    boards = [[(0, board0)]]
    count = 0
    while True:
        start = time()
        print(count, len(boards[-1]))
        alreadyFound = {}
        new = []
        for i1, board in enumerate(boards[-1]):
            board = board[1]
            countPins = 0
            for i in range(l):
                for j in range(l):
                    if board[i][j] == 1:
                        countPins += 1
                        directions = ((0, 1), (1, 0), (-1, 0), (0, -1))
                        for y, x in directions:
                            if 0 <= i + 2*y < l and 0 <= j + 2*x < l:
                                if board[i + y][j + x] == 1:
                                    if board[i + 2*y][j + 2*x] == 0:
                                        newBoard = deepcopy(board)
                                        newBoard[i][j] = 0
                                        newBoard[i + y][j + x] = 0
                                        newBoard[i + 2*y][j + 2*x] = 1
                                        if newBoard[1][3] == 0 and newBoard[3][1] == 0 and newBoard[3][5] == 0 and newBoard[5][3] == 0:
                                            break

                                        t = toTuple(newBoard)
                                        if alreadyFound.get(t):
                                            continue
                                        t1 = tuple(zip(*t[::-1]))
                                        if alreadyFound.get(t1):
                                            continue
                                        t2 = tuple(zip(*t1[::-1]))
                                        if alreadyFound.get(t2):
                                            continue
                                        t3 = tuple(zip(*t2[::-1]))
                                        if alreadyFound.get(t3):
                                            continue
                                        t4 = t[::-1]
                                        if alreadyFound.get(t4):
                                            continue
                                        t5 = tuple(k[::-1] for k in t)
                                        if alreadyFound.get(t5):
                                            continue

                                        new.append((i1, newBoard))
                                        for k in [t, t1, t2, t3, t4, t5]:
                                            alreadyFound[k] = True
        print(round(time()-start, 3), "s")
        if len(new) == 0:
            break
        boards.append(new)
        count += 1

    paths = []
    for finalBoard in boards[-1]:
        path = [finalBoard[1]]
        index = finalBoard[0]
        i = len(boards)-2
        while i >= 0:
            index, board = boards[i][index]
            path.append(board)
            i -= 1
        paths.append(path)
    
    s = ""
    for i in paths:
        s += "-----------------------------"
        s += "\n"
        for j in i:
            for k in j:
                s += str(k) + "\n"
            s += "\n"
        
    with open("C://Users//Maxim//Desktop//Python//Solitär//save.txt", "w+") as f:
        f.write(s)

def solve2():
    # 0: empty
    # 1: pin
    # 2: not on board
    board0 = [
        [2, 2, 0, 0, 0, 2, 2], 
        [2, 2, 0, 0, 0, 2, 2], 
        [0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 1, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0], 
        [2, 2, 0, 0, 0, 2, 2], 
        [2, 2, 0, 0, 0, 2, 2]
    ]
    solveRecursive(board0)

def solveRecursive(board):
    if board == [
        [2, 2, 1, 1, 1, 2, 2],
        [2, 2, 1, 1, 1, 2, 2],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [2, 2, 1, 1, 1, 2, 2],
        [2, 2, 1, 1, 1, 2, 2]]:
        return True
    for i in range(7):
        for j in range(7):
            if board[i][j] == 0:
                if i+1 < 7 and board[i+1][j] == 0:
                    if i-1 >= 0 and board[i-1][j] == 1:
                        d = deepcopy(board)
                        d[i][j] = 1
                        d[i+1][j] = 1
                        d[i-1][j] = 0
                        if solveRecursive(d):
                            print((i-1, j), (i+1, j))
                            return True
                    if i+2 < 7 and board[i+2][j] == 1:
                        d = deepcopy(board)
                        d[i][j] = 1
                        d[i+1][j] = 1
                        d[i+2][j] = 0
                        if solveRecursive(d):
                            print((i, j), (i+2, j))
                            return True
                if j+1 < 7 and board[i][j+1] == 0:
                    if j-1 >= 0 and board[i][j-1] == 1:
                        d = deepcopy(board)
                        d[i][j] = 1
                        d[i][j+1] = 1
                        d[i][j-1] = 0
                        if solveRecursive(d):
                            print((i, j-1), (i, j+1))
                            return True
                    if j+2 < 7 and board[i][j+2] == 1:
                        d = deepcopy(board)
                        d[i][j] = 1
                        d[i][j+1] = 1
                        d[i][j+2] = 0
                        if solveRecursive(d):
                            print((i, j), (i, j+2))
                            return True
    return False

def solve3():
    board = (
        (2, 2, 1, 1, 1, 2, 2),
        (2, 2, 1, 1, 1, 2, 2),
        (1, 1, 1, 1, 1, 1, 1),
        (1, 1, 1, 0, 1, 1, 1),
        (1, 1, 1, 1, 1, 1, 1),
        (2, 2, 1, 1, 1, 2, 2),
        (2, 2, 1, 1, 1, 2, 2),
    )
    start = time()
    solveRecursive2(board)
    print(time()-start)

import functools

@functools.lru_cache(maxsize=None)
def solveRecursive2(board):
    if board == (
        (2, 2, 0, 0, 0, 2, 2),
        (2, 2, 0, 0, 0, 2, 2),
        (0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 1, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 0),
        (2, 2, 0, 0, 0, 2, 2),
        (2, 2, 0, 0, 0, 2, 2),
    ):
        res.append(board[:])
        print("Found")
        return True
    directions = ((0, 1), (1, 0), (-1, 0), (0, -1))
    l = len(board)
    for i in range(l):
        for j in range(l):
            if board[i][j] == 1:
                for direction in directions:
                    if 0 <= i + 2*direction[0] < l and 0 <= j + 2*direction[1] < l:
                        if board[i+direction[0]][j+direction[1]] == 1 and board[i+2*direction[0]][j+2*direction[1]] == 0:
                            values = {
                                (i, j): 0, 
                                (i+direction[0], j+direction[1]): 0, 
                                (i+2*direction[0], j+2*direction[1]):1
                            }
                            d = tuple(tuple(values.get((i, j), board[i][j]) for j in range(l)) for i in range(l))
                            if solveRecursive2(d):
                                res.append(d)
                                return True
    return False

res = []
start = (
        (2, 2, 1, 1, 1, 2, 2),
        (2, 2, 1, 1, 1, 2, 2),
        (1, 1, 1, 1, 1, 1, 1),
        (1, 1, 1, 0, 1, 1, 1),
        (1, 1, 1, 1, 1, 1, 1),
        (2, 2, 1, 1, 1, 2, 2),
        (2, 2, 1, 1, 1, 2, 2),
    )
last = start

solve3()

for i in reversed(res[1:]):
    s = ""
    for j in range(len(i)):
        if i[j] == last[j]:
            s += str(i[j])
        else:
            start = None
            for k in range(len(i[j])):
                if i[j][k] == last[j][k]:
                    if start != None:
                        end = k
                        break
                else:
                    if start == None:
                        start = k
            start = 1+start*3
            end = 1 + end*3
            s2 = str(i[j])
            s += s2[:start] + '\033[93m' + s2[start:end] + '\033[0m' + s2[end:]
        s += "\n"
    print(s)
    last = i[:]
