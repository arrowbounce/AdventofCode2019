pos = []
vel = []
steps = 1000
stuff = {}
changes = []
with open("Day12") as f:
    for line in f:
        hold = line.strip()
        hold = hold[1:-1]
        hold = hold.split(", ")
        x = int(hold[0][2:])
        y = int(hold[1][2:])
        z = int(hold[2][2:])
        pos.append([x,y,z])
        vel.append((0,0,0))
init = [pos[:], vel[:]]

for i in range(steps):
    cur = []
    for a in range(4):
        change = [0, 0, 0]
        for b in range(4):
            if a != b:
                for c in range(3):
                    if pos[a][c] > pos[b][c]:
                        change[c] -= 1
                    elif pos[a][c] < pos[b][c]:
                        change[c] += 1
        vel[a] = (vel[a][0] + change[0], vel[a][1] + change[1], vel[a][2] + change[2])
        cur.append(change)
    for a in range(4):
        pos[a] = (pos[a][0] + vel[a][0], pos[a][1] + vel[a][1],pos[a][2] + vel[a][2])
    changes.append(cur)
    if i == 100:
        print pos
        print vel
print pos
print vel
tot = 0
for a in range(4):
    s1 = 0
    s2 = 0
    for c in pos[a]:
        s1 += abs(c)
    for c in vel[a]:
        s2 += abs(c)
    tot += s1*s2
print tot
pos = init[0]

for i in range(4):
    pos[i].extend([0]*3)

contx = False
conty = False
contz = False
seenx = {}
seeny = {}
seenz = {}
i = 0
while True:
    if contx and conty and contz:
        break
    for a in range(4):
        for b in range(4):
            if a != b:
                if pos[a][0] < pos[b][0]:
                    pos[a][3] += 1
                elif pos[a][0] > pos[b][0]:
                    pos[a][3] -= 1
                if pos[a][1] < pos[b][1]:
                    pos[a][4] += 1
                elif pos[a][1] > pos[b][1]:
                    pos[a][4] -= 1
                if pos[a][2] < pos[b][2]:
                    pos[a][5] += 1
                elif pos[a][2] > pos[b][2]:
                    pos[a][5] -= 1
    for a in range(4):
        pos[a][0] += pos[a][3]
        pos[a][1] += pos[a][4]
        pos[a][2] += pos[a][5]
    if not contx:
        temp = str([[x[0], x[3]] for x in pos])
        if temp in seenx:
            contx = True
            countx = i
        else:
            seenx[temp] = None
    if not conty:
        temp = str([[x[1], x[4]] for x in pos])
        if temp in seeny:
            conty = True
            county = i
        else:
            seeny[temp] = None
    if not contz:
        temp = str([[x[2], x[5]] for x in pos])
        if temp in seenz:
            contz = True
            countz = i
        else:
            seenz[temp] = None
    if i == 60000:
        print conty
    i += 1
print countx
print county
print countz