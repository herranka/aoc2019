import itertools

li = [int(x) for x in list(input().split(","))]

def digit(number, n):
    return number // 10**n % 10

perms = list(itertools.permutations([0,1,2,3,4], 5))
max_prev = -2*20

for p_i, perm in enumerate(perms):
    print(perm)
    previous = 0
    for a_i in range(5): # 5 amplifiers
        i = 0
        i_perm = 0
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
                # input
                if i_perm == 0: 
                    val = perm[a_i] ## holdup
                    i_perm += 1
                elif i_perm == 1:
                    # input output from previous
                    val = previous
                else:
                    print("got input more than once")
                    sys.exit(-1)
                if mode[0] == 0:
                    li[li[i+1]] = val
                i += 2
            elif op == 4:
                # print (output signal)
                if mode[0] == 0:
                    val = li[li[i+1]]
                else:
                    val = li[i+1]
                #print(val)
                previous = val # output to next amplifier
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
    if previous > max_prev:
        max_prev = previous
print(max_prev)