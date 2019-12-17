import intcode


f = open("Day17", "r")
cells = [int(i) for i in f.read().split(',')]
a = intcode.intcode(cells[:])

out = a.run()

p = ""
for i in out[0]:
    p = p + chr(i)
print p

hold = []
temp = []
for i in p:
    if i == "\n":
        hold.append(temp)
        temp = []
    elif i == "#":
        temp.append(1)
    else:
        temp.append(0)
total = 0
hold = hold[:-1]
for i in range(1, len(hold) - 1, 1):
    for j in range(1, len(hold[i]) -1, 1):
        if hold[i][j] == 1:
            if hold[i+1][j] == 1:
                if hold[i-1][j] == 1:
                    if hold[i][j+1] == 1:
                        if hold[i][j-1] == 1:
                            total += i*j
print total

cells[0] = 2
b = intcode.intcode(cells)
inp = [65, 44, 66, 44, 65, 44, 66, 44, 65, 44, 67, 44, 65, 44, 67, 44, 66, 44, 67, 10]
A = [82, 44, 54, 44, 76, 44, 49, 48, 44, 82, 44, 49, 48, 44, 82, 44, 49, 48, 10]
B = [76, 44, 49, 48, 44, 76, 44, 49, 50, 44, 82, 44, 49, 48, 10]
C = [82, 44, 54, 44, 76, 44, 49, 50, 44, 76, 44, 49, 48, 10]
inp.extend(A)
inp.extend(B)
inp.extend(C)
inp.extend([110, 10])
b.addinputs(inp)
out = b.run()
print out
print b.inputs