import math
def gcd(x, y):   
   while(y): 
       x, y = y, x % y 
  
   return x 

def mod(x):
    if x >= math.atan2(0, 1):
        return 2.5 * math.pi - x
    if x <= 0:
        return 1/2 * math.pi - x

cells = []
with open("Day10") as f:
    for line in f:
        cells.append(list(line.strip()))
height = len(cells)
width = len(cells[0])
asts = {}
for a in range(height):
    for b in range(width):
        if cells[a][b] == "#":
            asts[(a,b)] = None
most = 0
maxast = None
for ast1 in asts.keys():
    sees = 0
    dirs = {}
    vert = False
    vert2 = False
    horiz = False
    hor = False
    for ast2 in asts.keys():
        if ast2 == ast1:
            continue
        dirx = ast1[0] - ast2[0]
        diry = ast1[1] - ast2[1]
        if diry == 0:
            dist = dirx
        elif dirx == 0:
            dist = diry
        else:
            dist= abs(gcd(dirx, diry))
        dire = -math.atan2(dirx, diry)
        if dire < 0:
            dire = 2 * math.pi + dire
        if dire not in dirs:
            dirs[dire] = {}
        dirs[dire][dist] = ast2
    sees = len(dirs)
    if vert:
        sees += 1
    if horiz:
        sees += 1
    if vert2:
        sees += 1
    if hor:
        sees += 1
    if sees > most:
        most = sees
        maxast = ast1
        maxdirs = dirs.copy()

print most
print maxast
# hold = maxdirs.keys()
# hold.sort()
# print hold[0]
# print maxdirs[hold[0]]
# print hold[221]
# print maxdirs[hold[221]] #initial try correct answer here? 

def getangle(x, y):
    angle = math.atan2(x, y)
    if angle < 0:
        angle = 2 * math.pi + angle
    return angle

def getcoords(x, y):
    return (y - maxast[0], x - maxast[1])

def check(ast1):
    y = ast1[0]
    x = ast1[1]
    dirx = x - maxast[1]
    diry = y - maxast[0]
    if diry == 0:
        dire = (0, dirx / abs(dirx))
        dist = abs(dirx)
    elif dirx == 0:
        dire = (diry/abs(diry), 0)
        dist = abs(diry)
    else:
        dist = abs(gcd(dirx, diry))
        dire = (diry/dist, dirx/dist)
    for a in range(1, dist):
        if (dire[0] * a + maxast[0], dire[1] * a + maxast[1]) in asts:
            return [False]
    return [True, dire, dist]

angles = []
for ast in asts:
    if ast != maxast:
        res = check(ast)
        if res[0]:
            angles.append((math.atan2(res[1][1],res[1][0]), ast))
angles.sort()
hold = map(lambda a: a[1], angles[::-1])
print hold[199]

# angles = {}
# for ast1 in asts.keys():
#     if ast1 != maxast:
#         hold = getcoords(ast1[1], ast1[0])
#         angle = getangle(hold[0], hold[1])
#         if angle not in angles:
#             angles[angle] = []
#             angles[angle].append(ast1)

# a = angles.keys()
# a.sort()
# print angles[a[199]]
# print angles[a[188]]
# out = []
# print len(angles)
# for b in a:
#     out.append(angles[b])
# print out
# Get angles
# Sort angles
# get 200th angle
