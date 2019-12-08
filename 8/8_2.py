import sys

width =  25
height = 6

#width = 3
#height = 2

layers = []

inp = sys.stdin.read().strip()
length = len(inp)

size = width*height
nl = length//size
if length//size != length / size:
    print("bad dimensions")
    sys.exit()

#print(nl)
for i in range(nl):
    layers.append(inp[i*size:(i+1)*size])
#print(layers)

res = [None for n in range(size)]

for layer in layers:
    for c in range(size):
        if res[c] != None or layer[c] == "2":
            continue
        if layer[c] in ("0", "1"):
            res[c] = layer[c]

#print(''.join(res))
    
res2 = []
for r in range(height):
    line = []
    for c in range(width):
        line.append(res[r*width + c])
    res2.append(line)

for r in range(len(res2)):
    line = []
    for c in range(len(res2[0])):
        if res2[r][c] == "1":
            line.append("X")
        else:
            line.append(" ")
    print(''.join(line))

# image representation of res2:
#   GCPHL