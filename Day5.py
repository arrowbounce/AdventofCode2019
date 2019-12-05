f = open("Day5", "r")
cells = f.read().split(',')
cells = [int(i) for i in cells]
i = 0 

def com(num):
    out = []
    out.append(num%100)
    rem = num//100
    for i in str(rem)[::-1]:
        out.append(int(i))
    while len(out)<=4:
        out.append(0)
    return out
inputs = [5]

while True:
    value = cells[i]
    value = com(value)
    if value[0] == 1:
        if value[1] == 0:
            arg1 = cells[cells[i+1]]
        else:
            arg1 = cells[i+1]
        if value[2] == 0:
            arg2 = cells[cells[i+2]]
        else:
            arg2 = cells[i+2]
        arg3 = cells[i+3]
        cells[arg3] = arg1 + arg2
        i+= 4
    elif value[0] == 2:
        if value[1] == 0:
            arg1 = cells[cells[i+1]]
        else:
            arg1 = cells[i+1]
        if value[2] == 0:
            arg2 = cells[cells[i+2]]
        else:
            arg2 = cells[i+2]
        arg3 = cells[i+3]
        cells[arg3] = arg1 * arg2
        i+=4
    elif value[0] == 3:
        cells[cells[i+1]] = inputs[0]
        del inputs[0]
        i+=2
    elif value[0] == 4:
        if value[1] == 0:
            arg1 = cells[cells[i+1]]
        else:
            arg1 = cells[i+1]
        print arg1
        i+=2
    elif value[0] == 5:
        if value[1] == 0:
            arg1 = cells[cells[i+1]]
        else:
            arg1 = cells[i+1]
        if value[2] == 0:
            arg2 = cells[cells[i+2]]
        else:
            arg2 = cells[i+2]
        if arg1 != 0:
            i = arg2
        else:
            i+= 3
    elif value[0] == 6:
        if value[1] == 0:
            arg1 = cells[cells[i+1]]
        else:
            arg1 = cells[i+1]
        if value[2] == 0:
            arg2 = cells[cells[i+2]]
        else:
            arg2 = cells[i+2]
        if arg1 == 0:
            i = arg2
        else:
            i+= 3
    elif value[0] == 7:
        if value[1] == 0:
            arg1 = cells[cells[i+1]]
        else:
            arg1 = cells[i+1]
        if value[2] == 0:
            arg2 = cells[cells[i+2]]
        else:
            arg2 = cells[i+2]
        arg3 = cells[i+3]
        if arg1 < arg2:
            cells[arg3] = 1
        else:
            cells[arg3] = 0
        i+= 4
    elif value[0] == 8:
        if value[1] == 0:
            arg1 = cells[cells[i+1]]
        else:
            arg1 = cells[i+1]
        if value[2] == 0:
            arg2 = cells[cells[i+2]]
        else:
            arg2 = cells[i+2]
        arg3 = cells[i+3]
        if arg1 == arg2:
            cells[arg3] = 1
        else:
            cells[arg3] = 0
        i+= 4
    elif value[0] == 99:
        break
    else:
        print len(cells)
        print "Error"
        break
