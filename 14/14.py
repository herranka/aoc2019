import sys
import math

class Reaction:
    def __init__(self, components, result):
        self.components = components
        self.result = result # also component
    def __str__(self):
        out = []
        out.append(", ".join([str(x) for x in self.components]))
        out.append(" => " + str(self.result))
        return ''.join(out)
    def __repr__(self):
        return self.__str__()
    
class Component:
    def __init__(self, type, amount):
        self.type = type
        self.amount = amount
    def __str__(self):
        return "%d %s" % (self.amount, self.type)
    def __repr__(self):
        return self.__str__()

def input_to_component(cost):
    amount, name = cost.split(" ")
    amount = int(amount)
    co = Component(name, amount)
    return co

def is_orereaction(reaction):
    return "ORE" in [c.type for c in reaction.components]

def find_reaction(reactions, resulttype):
    return next(r for r in reactions if r.result.type == resulttype)

def totalore(reaction, amount):
    if is_orereaction(reaction):
        ore = next(c for c in reaction.components if c.type == "ORE")
        return math.ceil(amount / reaction.result.amount)*ore.amount
    else:
        return sum([totalore(find_reaction(reactions, c.type), amount) for c in reaction.components])

reactions = set()

for line in [x.strip() for  x in sys.stdin.readlines()]:
    comp, result = line.split(" => ")
    comp = comp.split(", ")
    cos = []
    for c in comp:
        co = input_to_component(c)
        cos.append(co)
    res = input_to_component(result)
    reactions.add(Reaction(cos, res))

fuelreaction = next(r for r in reactions if r.result.type == "FUEL")
orereactions = set([r for r in reactions if is_orereaction(r)])
print(fuelreaction)
print(orereactions)

print(totalore(fuelreaction, 1))