import intcode
f = open("Day13", "r")
cells = [int(i) for i in f.read().split(',')]
a = intcode.intcode(cells)
a.cells[0] =2
out = [None, 0]
screen = [[" " for i in range(37)] for j in range(22)]
scores = []
tiles = {
    0: " ",
    1: "|",
    2: "#",
    3: "-",
    4: "*"
}
while out[1] != 99:
    out = a.run()
    hold = out[0]
    lastdire = 1
    dire = 0
    for i in range(0, len(hold), 3):
        if hold[i] == -1 and hold[i+1] == 0:
            score = hold[i+2]
            scores.append(score)
            #print scores
        else:
            screen[hold[i+1]][hold[i]] = tiles[hold[i+2]]
            if hold[i+2] == 4:
                ballx = hold[i]
            if hold[i+2] == 3:
                paddlex = hold[i]
    for line in screen:
        pass
        #print str(line)
    if ballx < paddlex:
        dire = -1
        lastdire = -1
    elif ballx > paddlex:
        dire = 1
        lastdire = 1
    else:
        dire = 0
    a.addinputs([dire])
print score