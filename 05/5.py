li = [int(x) for x in list(input().split(","))]

def digit(number, n):
    return number // 10**n % 10

ID = 5

i = 0
while i < len(li):
    #print(i)
    mode = [0,0,0]
    for j in range(2,5):
        mode[j-2] = digit(li[i], j)
    if 10*digit(li[i], 1) + digit(li[i], 0) == 99:
        op = 99
    else:
        op = digit(li[i], 0)
    if op == 1:
        #add
        if mode[2] == 0:
            first = li[li[i+1]] if mode[0] == 0 else li[i+1]
            second = li[li[i+2]] if mode[1] == 0 else li[i+2]
            li[li[i+3]] = first + second
            i += 4
    elif op == 2:
        #mul
        if mode[2] == 0:
            first = li[li[i+1]] if mode[0] == 0 else li[i+1]
            second = li[li[i+2]] if mode[1] == 0 else li[i+2]
            li[li[i+3]] = first * second
            i += 4
    elif op == 3:
        val = ID
        if mode[0] == 0:
            li[li[i+1]] = val
        i += 2
    elif op == 4:
        # print
        if mode[0] == 0:
            print(li[li[i+1]])
        else:
            print(li[i+1])
        i += 2
    elif op == 5:
        # jump if true
        first = li[li[i+1]] if mode[0] == 0 else li[i+1]
        second = li[li[i+2]] if mode[1] == 0 else li[i+2]
        if first != 0:
            i = second
        else:
            i += 3
    elif op == 6:
        # jump if false
        first = li[li[i+1]] if mode[0] == 0 else li[i+1]
        second = li[li[i+2]] if mode[1] == 0 else li[i+2]
        if first == 0:
            i = second
        else:
            i += 3
    elif op == 7:
        # less than
        if mode[2] == 0:
            first = li[li[i+1]] if mode[0] == 0 else li[i+1]
            second = li[li[i+2]] if mode[1] == 0 else li[i+2]
            li[li[i+3]] = 1 if first < second else 0
        i += 4
    elif op == 8:
        # eq
        if mode[2] == 0:
            first = li[li[i+1]] if mode[0] == 0 else li[i+1]
            second = li[li[i+2]] if mode[1] == 0 else li[i+2]
            li[li[i+3]] = 1 if first == second else 0
        i += 4
    elif op == 99:
        #halt
        break
    else:
        print("no can do")
        break
