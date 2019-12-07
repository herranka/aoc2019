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

def is_child(parent, child):
    if len(parent.sats) == 0:
        return False
    if child in parent.sats:
        return True
    return any(is_child(par, child) for par in parent.sats)

def min_root(ids, sat1, sat2):
    min = None
    minsum = 2**20
    for root in ids.values():
        sum = recadd(root, 0)
        if sum < minsum and is_child(root, sat1) and is_child(root, sat2):
            min = root
            minsum = sum
    return min

#print(list(x.id for x in ids["C"].sats))
#print(list(x.id for x in ids["G"].sats))
#print(list(x.id for x in ids["D"].sats))
def recadd(orb, dist):
    #print(orb.id)
    if len(orb.sats) == 0:
        return dist
    return sum(list(recadd(sat, dist+1) for sat in orb.sats)) + dist
    #print(s)

def dist(root, child):
    if len(root.sats) == 0:
        return 2**10
    if child in root.sats:
        return 1
    else:
        return min([dist(sat, child) for sat in root.sats]) + 1

#print(is_child(ids["E"], ids["G"]))
#print(min_root(ids, ids["L"], ids["F"]).id)
#print(dist(ids["E"], ids["L"]))


you = ids["YOU"]
san = ids["SAN"]
mr = min_root(ids, you, san)
print(mr)
if mr != None:
    print(is_child(mr,san), is_child(mr, you))
    print(dist(mr, you) + dist(mr, san) - 2)
