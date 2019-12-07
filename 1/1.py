import sys

sum = 0

for line in sys.stdin:
    val = int(line)
    sum += val//3 - 2

print(sum)
