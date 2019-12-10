li = [int(x) for x in list(input().split(","))]

#restore state
li[1] = 12
li[2] = 2

print(li)

i = 0
while i < len(li):
    if li[i] == 1:
        #add
        li[li[i+3]] = li[li[i+1]] + li[li[i+2]]
        i += 4
    elif li[i] == 2:
        #mul
        li[li[i+3]] = li[li[i+1]] * li[li[i+2]]
        i += 4
    elif li[i] == 99:
        #halt
        break
    else:
        print("no can do")
        break

print(li[0])