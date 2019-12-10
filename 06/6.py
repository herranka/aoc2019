import sys
sys.setrecursionlimit(2**10)

class Node:
    def __init__(self, ID):
        self.sats = []
        self.id = ID
    def append(self, sat):
        self.sats.append(sat)

ids = {}

inp = [x.strip().split(")") for x in sys.stdin.readlines()]
for o, s in inp:
    if not o in ids:
        orb = Node(o)
        ids[o] = orb
    if s not in ids:
        sat = Node(s)
        ids[s] = sat
    sat = ids[s]
    orb = ids[o]
    ids[o].append(sat)

#print(list(x.id for x in ids["C"].sats))
#print(list(x.id for x in ids["G"].sats))
#print(list(x.id for x in ids["D"].sats))
def recadd(orb, dist):
    #print(orb.id)
    if len(orb.sats) == 0:
        return dist
    return sum(list(recadd(sat, dist+1) for sat in orb.sats)) + dist
    #print(s)


print(max([recadd(root, 0) for root in ids.values()]))