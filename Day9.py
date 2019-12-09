import intcode
f = open("Day9", "r")
cells = [int(i) for i in f.read().split(',')]
a = intcode.intcode(cells)
a.addinputs([2])
out = a.run()
print out