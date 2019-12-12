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

def apply(list, delta):
    for i in range(len(list)):
        list[i] += delta[i]

moons = [list(getxyz()) for i in range(4)]
velocities = [[0,0,0] for i in range(4)]

print("After 0 steps:")
for m in range(len(moons)):
        print("pos=<%d, %d, %d>, vel=<%d, %d, %d>" % (
            moons[m][0], moons[m][1], moons[m][2],
            velocities[m][0], velocities[m][1], velocities[m][2]
        ))

steps = 0
while steps < 1000:
    for i in range(len(moons)): # apply gravity
        for j in range(i+1, len(moons)):
            gr = gravity(moons[i], moons[j])
            apply(velocities[i], gr[0])
            apply(velocities[j], gr[1])
    for i in range(len(moons)): # apply velocities
        for p in range(3):
            moons[i][p] += velocities[i][p]
    steps += 1
    print("After %d steps:" % steps)
    for m in range(len(moons)):
        print("pos=<%d, %d, %d>, vel=<%d, %d, %d>" % (
            moons[m][0], moons[m][1], moons[m][2],
            velocities[m][0], velocities[m][1], velocities[m][2]
        ))

pots = [sum(abs(moon[p]) for p in range(3)) for moon in moons]
kins = [sum(abs(vel[p]) for p in range(3)) for vel in velocities]
tots = [pots[i]*kins[i] for i in range(len(pots))]
#print("potential energy: %d" % sum(pots))
#print("kinetic energy: %d" % sum(kins))
print("total energy: %d" % (sum(tots)))