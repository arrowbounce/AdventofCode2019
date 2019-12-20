import intcode


f = open("Day19", "r")
cells = [int(i) for i in f.read().split(',')]
pull = 0
for i in range(50):
    for j in range(50):
        a =intcode.intcode(cells[:])
        a.addinputs([i, j])
        out = a.run()
        if out[0][0] == 1:
            print i,j
            pull += 1
print pull

miny = 0
x = 3
y = 4
first = True
while True:
    print x, y, miny
    a = intcode.intcode(cells[:])
    a.addinputs([x, y])
    out = a.run()
    a = intcode.intcode(cells[:])
    a.addinputs([x+99,y])
    out2 = a.run()
    a = intcode.intcode(cells[:])
    a.addinputs([x,y+99])
    out3 = a.run()
    a = intcode.intcode(cells[:])
    a.addinputs([x+99,y+99])
    out4 = a.run()
    if first == True:
        print out
        if out[0][0] == 1:
            miny = y
            first = False
    if out[0][0] == out2[0][0]== out3[0][0]==out4[0][0] ==1:
        print x*y
        break
    y += 1
    if first == False:
        if out[0][0] == 0:
            x += 1
            y = miny
            first = True