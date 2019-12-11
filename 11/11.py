li = [int(x) for x in list(input().split(","))]

for i in range(1000):
    li.append(0) # add empty memory

def digit(number, n):
    return number // 10**n % 10

def firstsecond(li, mode, rel):
    if mode[0] == 0:
        first = li[li[i+1]]
    elif mode[0] == 1:
        first = li[i+1]
    elif mode[0] == 2:
        first = li[li[i+1] + rel]
    if mode[1] == 0:
        second = li[li[i+2]]
    elif mode[1] == 1:
        second = li[i+2]
    elif mode[1] == 2:
        second = li[li[i+2] + rel]
    
    return (first, second)

def onearg(li, mode, rel, index):
    if mode[index] == 0:
        first = li[li[i+1]]
    elif mode[index] == 1:
        first = li[i+1]
    elif mode[index] == 2:
        first = li[li[i+1] + rel]
    return first

direcs = (
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1)
)

def right(direc):
    return direcs[(direcs.index(direc)+1) % len(direcs)]

def left(direc):
    return direcs[(direcs.index(direc)-1) % len(direcs)]

def move(pr, pc, direc):
    dr, dc = direc
    return (pr + dr, pc + dc)    

N = 10000
board = [[0 for c in range(N)] for r in range(N)]
pr = len(board)//2
pc = len(board[0])//2
visited = set()
direc = (-1, 0)
printc = 0
i = 0
rel = 0
while i < len(li):
    mode = [0,0,0]
    for j in range(2,5):
        mode[j-2] = digit(li[i], j)
    if 10*digit(li[i], 1) + digit(li[i], 0) == 99:
        op = 99
    else:
        op = digit(li[i], 0)
    print("%d : %d : %d, %d" % (i, li[i], op, rel))
    if op == 1:
        #add
        first, second = firstsecond(li, mode, rel)
        if mode[2] == 0:
            li[li[i+3]] = first + second
        elif mode[2] == 2:
            li[li[i+3]+rel] = first + second
        i += 4
    elif op == 2:
        #mul
        first, second = firstsecond(li, mode, rel)
        if mode[2] == 0:
            li[li[i+3]] = first * second
        elif mode[2] == 2:
            li[li[i+3]+rel] = first * second
        i += 4
    elif op == 3:
        # input
        val = board[pr][pc]
        if mode[0] == 0:
            li[li[i+1]] = val
        elif mode[0] == 2:
            li[li[i+1]+rel] = val
        i += 2
    elif op == 4:
        # print
        if printc % 2 == 0:
            color = onearg(li, mode, rel, 0)
            board[pr][pc] = color
            visited.add((pr, pc)) # count afterwards
        else:
            newdir = onearg(li, mode, rel, 0)
            direc = left(direc) if newdir == 0 else right(direc)
            pr, pc = move(pr, pc, direc)
        printc += 1
        i += 2
    elif op == 5:
        # jump if true
        first, second = firstsecond(li, mode, rel)
        if first != 0:
            i = second
        else:
            i += 3
    elif op == 6:
        # jump if false
        first, second = firstsecond(li, mode, rel)
        if first == 0:
            i = second
        else:
            i += 3
    elif op == 7:
        # less than
        first, second = firstsecond(li, mode, rel)
        if mode[2] == 0:
            li[li[i+3]] = 1 if first < second else 0
        elif mode[2] == 2:
            li[li[i+3]+rel] = 1 if first < second else 0
        i += 4
    elif op == 8:
        # eq
        first, second = firstsecond(li, mode, rel)
        if mode[2] == 0:
            li[li[i+3]] = 1 if first == second else 0
        elif mode[2] == 2:
            li[li[i+3]+rel] = 1 if first == second else 0
        i += 4
    elif op == 9:
        # add to rel
        first = onearg(li, mode, rel, 0)
        rel += first
        i += 2
    elif op == 99:
        #halt
        break
    else:
        print("no can do")
        break

print(len(visited))