import sys

def man(p1, p2):
    dx = abs(p2[0] - p1[0])
    dy = abs(p2[1] - p1[1])
    return dx + dy

def p1():
    ori = (0,0)
    shortest = None
    shortest_man = 10000000000

    inp1 = input().split(",")
    pss1 = [(x[0], int(x[1:])) for x in inp1]
    inp2 = input().split(",")
    pss2 = [(x[0], int(x[1:])) for x in inp2]
    
    visited = []
    r = 0
    c = 0
    for move in pss1:
        if move[0] == "R":
            # right
            for i in range(move[1]):
                visited.append((r, c))
                c += 1
        elif move[0] == "D":
            # right
            for i in range(move[1]):
                visited.append((r, c))
                r += 1
        elif move[0] == "L":
            # right
            for i in range(move[1]):
                visited.append((r, c))
                c -= 1
        elif move[0] == "U":
            # right
            for i in range(move[1]):
                visited.append((r, c))
                r -= 1
        else:
            print("wtf d")
        print(visited[-1])
    print("pss2:")
    r = 0
    c = 0
    for move in pss2:
        if move[0] == "R":
            # right
            for i in range(move[1]):
                if (r, c) in visited and not (r==0 and c==0):
                    m = man(ori, (r, c))
                    if m < shortest_man:
                        shortest = (r,c)
                        shortest_man = m
                visited.append((r, c))
                c += 1

        elif move[0] == "D":
            # right
            for i in range(move[1]):
                if (r, c) in visited and not (r==0 and c==0):
                    m = man(ori, (r, c))
                    if m < shortest_man:
                        shortest = (r,c)
                        shortest_man = m
                visited.append((r, c))
                r += 1
        elif move[0] == "L":
            # right
            for i in range(move[1]):
                if (r, c) in visited and not (r==0 and c==0):
                    m = man(ori, (r, c))
                    if m < shortest_man:
                        shortest = (r,c)
                        shortest_man = m
                visited.append((r, c))
                c -= 1
        elif move[0] == "U":
            # right
            for i in range(move[1]):
                if (r, c) in visited and not (r==0 and c==0):
                    m = man(ori, (r, c))
                    if m < shortest_man:
                        shortest = (r,c)
                        shortest_man = m
                visited.append((r, c))
                r -= 1
        else:
            print("wtf d")
        print(visited[-1])
    if (r, c) in visited and not (r==0 and c==0):
                    m = man(ori, (r, c))
                    if m < shortest_man:
                        shortest = (r,c)
                        shortest_man = m

    print(shortest_man)


def p2():
    pass

p1()
p2()

