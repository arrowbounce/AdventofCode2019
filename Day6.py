import sys
sys.setrecursionlimit(20000)

class map:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.parent = None
    def getorbits(self, orbs):
        out = 0
        for child in self.children:
            out += 1 + orbs[child].getorbits(orbs)
        return out
orbits = {}
with open("Day6") as f:
    for line in f:
        hold = line.split(")")
        ob1 = hold[0].strip()
        ob2 = hold[1].strip()
        if ob1 not in orbits:
            orbits[ob1] = map(ob1)
        if ob2 not in orbits:
            orbits[ob2] = map(ob2)
        orbits[ob1].children.append(ob2)
        orbits[ob2].parent = ob1
stuff = [["COM", 0]]
print orbits["HXD"].children
total = 0
while len(stuff) > 0:
    thing = stuff.pop(0)
    for child in orbits[thing[0]].children:
        total += 1 + thing[1]
        stuff.append([child, 1+thing[1]])
print total

ob1 = "YOU"
ob2 = "SAN"

list1= []
list2 = []
ob1 = orbits[ob1].parent
while ob1 is not None:
    list1.append(ob1)
    ob1 = orbits[ob1].parent
ob2 = orbits[ob2].parent
while ob2 is not None:
    list2.append(ob2)
    ob2 = orbits[ob2].parent
print len(list1)
print len(list2)
list3 = [x for x in list1 if x in list2]
print len(list3)
print(len(list1) + len(list2) - 2*len(list3))