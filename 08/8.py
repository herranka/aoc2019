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

print(nl)
for i in range(nl):
    layers.append(inp[i*size:(i+1)*size])
print(layers)

minzero = 2**256
min = None

for layer in layers:
    z = layer.count("0")
    if z < minzero:
        minzero = z
        min = layer

print(min.count("1")*min.count("2"))