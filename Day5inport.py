import intcode
f = open("Day5", "r")
cells = [int(i) for i in f.read().split(',')]
inputs = [5]
outputs = []
code = intcode.intcode(cells)
outputs = code.run(inputs)
print outputs
