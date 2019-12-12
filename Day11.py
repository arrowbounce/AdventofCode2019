import intcode
f = open("Day11", "r")
cells = [int(i) for i in f.read().split(',')]
a = intcode.intcode(cells)
maps = {(0,0): 1}
curcell = (0, 0)
curdir = 0
while True:
    if curcell not in maps.keys():
        maps[curcell] = 0
    i =[maps[curcell]]
    a.addinputs(i)
    out = a.run()
    maps[curcell] = out[0][0]
    if out[0][1] == 0:
        curdir += 1
    else:
        curdir -= 1
    if curdir == 4:
        curdir = 0
    if curdir == -1:
        curdir = 3
    if curdir == 1:
        curcell = (curcell[0] - 1, curcell[1])
    elif curdir == 2:
        curcell = (curcell[0], curcell[1] - 1)
    elif curdir == 3:
        curcell = (curcell[0] + 1, curcell[1])
    else:
        curcell = (curcell[0], curcell[1] + 1)
    if out[1] == 99:
        print out
        break

for y in range(50, -50, -1):
    out = ""
    for x in range(-50, 50):
        if (x, y) in maps:
            if maps[(x,y)] == 1:
                out += "#"
            else:
                out += " "
        else:
            out += " "
    print out
print len(maps)