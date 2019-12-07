import sys

sum = 0

for line in sys.stdin:
    inp = int(line)
    s = 0
    print(inp)
    inp = inp//3 - 2
    while inp > 0:
        print(inp)
        s += inp
        inp = inp//3 - 2
    sum += s

print(sum)
