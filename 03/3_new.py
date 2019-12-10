import sys

def man(p1, p2):
    dx = abs(p2[0] - p1[0])
    dy = abs(p2[1] - p1[1])
    return dx + dy

def intersects(l1, l2):
    l1x = range(min(l1[0][0], l1[1][0]), max(l1[0][0], l1[1][0]) + 1)
    l1y = range(min(l1[0][1], l1[1][1]), max(l1[0][1], l1[1][1]) + 1)
    l2x = range(min(l2[0][0], l2[1][0]), max(l2[0][0], l2[1][0]) + 1)
    l2y = range(min(l2[0][1], l2[1][1]), max(l2[0][1], l2[1][1]) + 1)

    xi = range(max(l1x[0], l2x[0]), min(l1x[-1], l2x[-1]) + 1)
    yi = range(max(l1y[0], l2y[0]), min(l1y[-1], l2y[-1]) + 1)

    #print(l1, l2, xi, len(xi), yi, len(yi))

    return len(xi) != 0 and len(yi) != 0

def horiz(li):
    return li[0][0] == li[1][0]

def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       return None

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    if int(x) == x and int(y) == y:
        return int(x), int(y)
    else:
        return None

def intersect(l1, l2): # return point
    if not intersects(l1, l2) or horiz(l1)==horiz(l2): # maybe loads of points intersections
        return None
    return line_intersection(l1, l2)

def to_line(move, r, c):
    if move[0] == "R":
        return ((r, c), (r, c + move[1]))
    elif move[0] == "D":
        return ((r, c), (r + move[1], c))
    elif move[0] == "L":
        return ((r, c), (r, c - move[1]))
    elif move[0] == "U":
        return ((r, c), (r - move[1], c))
    else:
        print("wtf move: " + str(move))
        sys.exit()

inp1 = input().split(",")
pss1 = [(x[0], int(x[1:])) for x in inp1]
inp2 = input().split(",")
pss2 = [(x[0], int(x[1:])) for x in inp2]

ori = (0,0)
lines1 = []
lines2 = []
ipoints = {} # intersecting points on certain line

def push(m, line1, line2, point):
    if line1 in m:
        m[line1].append(point)
    else:
        m[line1] = [point]
    if line2 in m:
        m[line2].append(point)
    else:
        m[line2] = [point]


def p1():
    minman = 10000000000000
    last_x, last_y = (0,0)
    for move in pss1:
        l1 = to_line(move, last_x, last_y)
        lines1.append(l1)
        last_x, last_y = l1[1]
    
    last_x, last_y = (0,0)
    for move in pss2:
        l1 = to_line(move, last_x, last_y)
        for l2 in lines1:
            ip = intersect(l1, l2)
            if ip != None and ip != (0,0):
                #print(ip, man(ip, ori), "m" if man(ip, ori) < minman else "", l1, l2)
                push(ipoints, l1, l2, ip) # for p2
                m = man(ori, ip)
                if m < minman:
                    minman = m
        lines2.append(l1)
        last_x, last_y = l1[1]
    
    print(minman)

def pushps(ps, p, s, i): # i is whether first or second wire
    if p in ps:
        if s  < ps[p][i]:
            ps[p][i] = s
    else:
        ps[p] = [10000000000000, 10000000000000000]
        ps[p][i] = s

def p2():
    pointsteps = {} # point -> [sum1, sum2], sum1, sum2 lowest for 1,2 resp.
    minsteps = 10000000000
    steps = 0
    last_x, last_y = (0,0)

    for move in pss1:
        l1 = to_line(move, last_x, last_y)
        if l1 in ipoints:
            p = ipoints[l1][0]
            s = steps + man(l1[0], p)
            pushps(pointsteps, p, s, 0)
        last_x, last_y = l1[1]
        steps += man(l1[0], l1[1])
    steps = 0
    last_x, last_y = (0,0)
    for move in pss2:
        l1 = to_line(move, last_x, last_y)
        #print(l1, ipoints[l1] if l1 in ipoints else "None")
        if l1 in ipoints:
            p = ipoints[l1][0]
            s = steps + man(l1[0], p)
            pushps(pointsteps, p, s, 1)
        last_x, last_y = l1[1]
        steps += man(l1[0], l1[1])
    #print(ipoints)
    points = [pointsteps[key] for key in pointsteps]
    points = [sum(p) for p in points]
    points.sort()
    print(points[0])

p1()
p2()