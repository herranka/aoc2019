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

def print_fuel_components(fuelreaction):
    nums = {}
    for comp in fuelreaction.components:
        ty = comp.type
        am = comp.amount
        if ty in nums:
            nums[ty] += am
        else:
            nums[ty] = am
    print(nums)

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
oreresulttypes = [o.result.type for o in orereactions]
print(fuelreaction)
#print(orereactions)
#print(oreresulttypes)

def weight(component, reactions):
    if component.type == "ORE":
        return 0 # 0 distance from ore
    else:
        return max([weight(c, reactions) for c in find_reaction(reactions, component.type).components]) + 1

# define weights
weights = {} # type -> weight
for reaction in reactions:
    for comp in reaction.components:
        if comp.type not in weights:
            weights[comp.type] = weight(comp, reactions)

print("weights : " + str(weights))

def max_weighted(components, weights):
    maxweight = max([weights[c.type] for c in components])
    return [comp for comp in components if weights[comp.type] == maxweight]

while not all(c.type == "ORE" for c in fuelreaction.components):
    # change all components to their components if not already of type ore
    newcomps = []
    for c in fuelreaction.components:
        if c in max_weighted(fuelreaction.components, weights):
            if c.type != "ORE":
                # change to its components
                am = c.amount
                re = find_reaction(reactions, c.type)
                for c2 in re.components:
                    c2.amount *= math.ceil(am / re.result.amount)
                    newcomps.append(c2)
            else:
                newcomps.append(c)
        else:
            newcomps.append(c)
    print(newcomps)
    # fuse identical component types
    newcomps2 = []
    for i in range(len(newcomps)):
        do_add = True
        for j in range(i+1, len(newcomps)):
            if newcomps[i].type == newcomps[j].type:
                newcomps[j].amount += newcomps[i].amount
                do_add = False
                break
        if do_add:
            newcomps2.append(newcomps[i])
    fuelreaction.components = newcomps2
    print(newcomps2)
    #print_fuel_components(fuelreaction)