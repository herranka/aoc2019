start, stop = [int(x) for x in input().split("-")]

sum = 0
for n in range(start, stop+1):
    doubles = False
    increasing = True
    st = str(n)
    for i in range(len(st)-1):
        if st[i] == st[i+1]:
            doubles = True
        if st[i] > st[i+1]:
            increasing = False
            continue
    if doubles and increasing and len(st) == 6:
        sum += 1
print(sum)

#p2
sum = 0
for n in range(start, stop+1):
    doubles = None
    increasing = True
    st = str(n)
    ch, chcount = 0, 0
    for i in range(len(st)-1):
        if st[i] == st[i+1]:
            try:
                b1 = st[i-1] == st[i]
            except: b1 = false
            try: 
                b2 = st[i+1] == st[i+2]
            except: b2 = False
            if not b1 and not b2:
                doubles = True
        if st[i] > st[i+1]:
            increasing = False
            continue
    if doubles and increasing and len(st) == 6:
        sum += 1
print(sum)