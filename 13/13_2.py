from itertools import chain

li = [int(x) for x in list(input().split(","))]

li[0] = 2 # insert coin

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

def getdir(x, paddx):
    diff = x-paddx
    if diff == 0:
        return 0
    else:
        return diff//abs(diff)

outc = 0
x = -1
y = -1
board = [[0 for c in range(50)] for r in range(50)]
joyst = 0
paddx = 19
paddy = 19
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
    #print("%d : %d : %d, %d" % (i, li[i], op, rel))
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
        joystick = getdir(x, paddx)
        paddx += joystick
        val = joystick
        if mode[0] == 0:
            li[li[i+1]] = val
        elif mode[0] == 2:
            li[li[i+1]+rel] = val
        i += 2
    elif op == 4:
        # print
        first = onearg(li, mode, rel, 0)
        if outc % 3 == 0:
            x = first
        elif outc % 3 == 1:
            y = first
        elif outc % 3 == 2:
            #board[y][x] = first
            print("x: %d, y: %d" % (x, y))
            score = first
            print("score %d" % score)
        outc += 1
        #print(first)
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

numblocks = list(chain(*board)).count(2)
print("numblocks: %d" % numblocks)

print(score)