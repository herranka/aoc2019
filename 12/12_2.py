import math

def getxyz():
    x, y, z = [int(st[2:]) for st in input().replace("<", "").replace(">", "").split(", ")]
    #print(x, y, z)
    return x, y, z

def gravity(moon1, moon2):
    deltavel1 = [0 for i in range(3)]
    deltavel2 = [0 for i in range(3)]
    for m in range(len(moon1)):
        diff = moon2[m]-moon1[m]
        deltavel1[m] = diff//abs(diff) if diff != 0 else 0
    for m in range(len(moon2)):
        diff = moon2[m]-moon1[m]
        deltavel2[m] = (-diff)//abs(diff) if diff != 0 else 0
    return deltavel1, deltavel2

def gravity1(moon1, moon2, p):
    diff = moon2[p] - moon1[p]
    deltavel1 = diff//abs(diff) if diff != 0 else 0
    deltavel2 = (-diff)//abs(diff) if diff != 0 else 0
    return deltavel1, deltavel2

def apply(list, delta):
    for i in range(len(list)):
        list[i] += delta[i]

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

def lcm3(a,b,c):
    ab = lcm(a,b)
    res = lcm(ab, c)
    return res

moons = [list(getxyz()) for i in range(4)]
res = []

for s in range(3): # for every axis
    velocities = [0 for i in range(4)]
    steps = 0
    while True:
        for i in range(len(moons)): # apply gravity
            for j in range(i+1, len(moons)):
                gr = gravity1(moons[i], moons[j], s)
                velocities[i] += gr[0]
                velocities[j] += gr[1]
        for i in range(len(moons)): # apply velocities
            moons[i][s] += velocities[i]
        steps += 1
        if all(vel == 0 for vel in velocities):
            break
    res.append(steps)

for s in res: print(s)

print(2*lcm3(*res))
