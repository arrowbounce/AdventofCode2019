import math
with open("Day8") as f:
    for line in f:
        hold = line
few = 999999
out = 0
i = 0
size = 25 * 6
while i < len(hold):
    cur = hold[i:i+size]
    if few > cur.count('0'):
        few = cur.count('0')
        out = cur.count('1') * cur.count('2')
    i += size
print out

out = list(hold[0:size])
out = []
for pixel in range(size):
    i = 0
    while True:
        if size*i+pixel >= len(hold):
            out.append('2')
            break
        if hold[size*i+pixel] != '2':
            out.append(hold[size*i+pixel])
            break
        i+=1
i = 0
while i < len(out):
    s = ""
    for l in out[i:i+25]:
        if l == "1":
            s += "*"
        else:
            s += " "
    print s
    i+= 25
