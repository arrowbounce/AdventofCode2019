import math
from collections import OrderedDict
hold = {}
elems = {}
class elem:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.parent = []
        self.level = 0
    def addchild(self, name):
        self.children.append(name)

with open("Day14") as f:
    for line in f:
        x = line.replace(',', '')
        x = x.split()
        i = 0
        els = []
        while True:
            if x[i] == "=>":
                break
            name = x[i+1]
            if name not in elems:
                elems[name] = elem(name)
            elems[name].addchild(x[-1])
            els.append([x[i+1], int(x[i])])
            i+=2
        hold[x[i+2]] = [int(x[i+1]), els]
for i in range(2269300, 2269400): #manually did binary search to narrow down, forgot how to implement it off the top of my head
    els = OrderedDict()
    elems["FUEL"] = elem("FUEL")
    els["FUEL"] = ["FUEL", i]
    elems["FUEL"].level = 0
    check = 0
    stuff = ["ORE"]
    while len(stuff) != 0:
        curel = stuff.pop(0)
        for child in elems[curel].children:
            elems[child].level = elems[curel].level + 1
            stuff.append(child)

    while len(els) != 1 or check != 1:
        check = 1
        minlevel = 0
        pull = None
        for thing in els:
            if elems[thing].level > minlevel:
                pull = thing
                minlevel = elems[thing].level
        curel = els.pop(pull)
        find = hold[curel[0]]
        quant = math.ceil(curel[1]/find[0])
        for el in find[1]:
            if el[0] in els:
                els[el[0]][1] += el[1] * quant
            else:
                els[el[0]] = [el[0], el[1] * quant]
    if math.log(els["ORE"][1], 10) >= 12:
        print i
        break
print els 
print math.log(els["ORE"][1], 10)