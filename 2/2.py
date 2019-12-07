from itertools import combinations
import sys

l = [int(x) for x in list(input().split(","))]

def works(noun, verb):
    li = l[:]
    li[1] = noun
    li[2] = verb
    i = 0
    while i < len(li):
        if li[i] == 1:
            #add
            try:
                li[li[i+3]] = li[li[i+1]] + li[li[i+2]]
            except IndexError:
                li[0] = -1
                break
            i += 4
        elif li[i] == 2:
            #mul
            try:
                li[li[i+3]] = li[li[i+1]] * li[li[i+2]]
            except IndexError:
                li[0] = -1
                break
            i += 4
        elif li[i] == 99:
            #halt
            break
        else:
            print("no can do")
            break
    if li[0] == 19690720:
        return True
    else:
        return False
    


for a, b in combinations(range(100), 2):
    if works(a, b):
        print(a*100+b)
        sys.exit(0)
    if works(b, a):
        print(b*100+a)
        sys.exit(0)

print("no res")
        
    
