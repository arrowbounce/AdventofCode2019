import intcode


f = open("Day15", "r")
cells = [int(i) for i in f.read().split(',')]
a = intcode.intcode(cells)

location = [25, 25]
curpath = []
result = 0
home = None

seen = False
area = [[0 for x in range(50)] for y in range(50)]
area[location[0]][location[1]] = 1
while True:
    if area[location[0]+1][location[1]] == 0:
        a.addinputs([1])
        result = a.run()
        if result[0][0] == 0:
            area[location[0]+1][location[1]] = 1
        else:
            curpath.append(2)
            area[location[0]+1][location[1]] = 2
            location[0] += 1
            if result[0][0] == 2:
                home = location[:]
                print home
    elif area[location[0]][location[1]+1] == 0:
        a.addinputs([3])
        result = a.run()
        if result[0][0] == 0:
            area[location[0]][location[1]+1] = 1
        else:
            area[location[0]][location[1]+1] = 2
            curpath.append(4)
            location[1] +=1
            if result[0][0] == 2:
                home = location[:]
                print home
    elif area[location[0]-1][location[1]] == 0:
        a.addinputs([2])
        result = a.run()
        if result[0][0] == 0:
            area[location[0]-1][location[1]] = 1
        else:
            area[location[0]-1][location[1]] = 2
            curpath.append(1)
            location[0] -= 1
            if result[0][0] == 2:
                home = location[:]
                print home
    elif area[location[0]][location[1]-1] == 0:
        a.addinputs([4])
        result = a.run()
        if result[0][0] == 0:
            area[location[0]][location[1]-1] = 1
        else:
            area[location[0]][location[1]-1] = 2
            curpath.append(3)
            location[1] -= 1
            if result[0][0] == 2:
                home = location[:]
                print home
    elif len(curpath) == 0:
        break
    else:
        nex = curpath.pop()
        a.addinputs([nex])
        if nex == 1:
            location[0] += 1
        elif nex == 3:
            location[1] += 1
        elif nex == 2:
            location[0] -= 1
        else:
            location[1] -= 1
        a.run()
    if len(area)%1000 == 0:
        print len(area)
    if not seen:
        if home is not None:
            print len(curpath)
            seen = True
area[home[0]][home[1]] = 3
area[25][25] = 4
print home
for x in area:
    out = ""
    for y in x:
        if y == 1:
            out+= "#"
        elif y==2 or y ==0:
            out+=" "
        elif y ==3:
            out+= "*"
        elif y == 4:
            out+="!"
    print out
a = 0
area[25][25] = 2
hold = [(home, 0)]

while len(hold) != 0:
    loc, level = hold.pop(0)
    if area[loc[0]+1][loc[1]] == 2:
        area[loc[0]+1][loc[1]] = 4
        new = [loc[0]+1, loc[1]]
        hold.append((new, level+1))
    if area[loc[0]-1][loc[1]] == 2:
        area[loc[0]-1][loc[1]] = 4
        new = [loc[0]-1, loc[1]]
        hold.append((new, level+1))
    if area[loc[0]][loc[1]+1] == 2:
        area[loc[0]][loc[1]+1] = 4
        new = [loc[0], loc[1]+1]
        hold.append((new, level+1))
    if area[loc[0]][loc[1]-1] == 2:
        area[loc[0]][loc[1]-1] = 4
        new = [loc[0], loc[1]-1]
        hold.append((new, level+1))
print level
for x in area:
    out = ""
    for y in x:
        if y == 1:
            out+= "#"
        elif y==2 or y==0:
            out+=" "
        elif y ==3:
            out+= "*"
        elif y == 4:
            out+="!"
    print out