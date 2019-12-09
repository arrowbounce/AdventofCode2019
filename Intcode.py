#version 3.0. Day 7.

#Usage:
#Initialize with intcode(cells), whereself.cells is a list representing the intcode memory
#Add inputs using addinputs(inputs), where inputs is a list of inputs to add
#Run the the machien with run(). Machine will stop on either an input command without an input or a halt command.

class intcode:
    oplen = {1: 3,2: 3,3: 1,4: 1,5: 2,6: 2,7: 3,8: 3,9:1,99: 0}
    outs = [1, 2, 3, 7, 8]
    def __init__(self, cells):
        self.cells = cells[:]
        self.inputs = []
        self.lastpos = 0
        self.revbase = 0
    def interp(self, num):
        out = []
        code = num%100
        out.append(code)
        rem = num//100
        for i in str(rem)[::-1]:
            out.append(int(i))
        while len(out)<=self.oplen[code]:
            out.append(0)
        return out
    def getargs(self, start, nums):
        out = [0]
        for i in range(1, self.oplen[nums[0]] + 1):
            mode = 0
            if nums[i] == 0:
                if i == len(nums) - 1:
                    if nums[0] in self.outs:
                        mode = 1
            else:
                if nums[i] == 2:
                    if nums[0] in self.outs:
                        mode = 3
                    else:
                        mode = 2
                else:
                    mode = 1
            if start+i >= len(self.cells):
                self.cells.extend([0 for i in range(start+i - len(self.cells) + 10)])
            if mode < 2:
                offset = 0
            else:
                offset = self.revbase
            if mode%2 == 0:
                if offset + self.cells[start+i] >= len(self.cells):
                    self.cells.extend([0 for j in range(offset + self.cells[start+i] - len(self.cells) + 10)])
                out.append(self.cells[self.cells[start+i] + offset])
            else:
                if nums[0] in self.outs:
                    if i == len(nums) - 1:
                        if self.cells[start+i] + offset >= len(self.cells):
                            self.cells.extend([0 for i in range(self.cells[start+i] - len(self.cells) + 10)])
                out.append(self.cells[start+i] + offset)
        return out
    def addinputs(self, inputs):
        self.inputs.extend(inputs)
    def run(self):
        outputs = []
        while True:
            value = self.cells[self.lastpos]
            value = self.interp(value)
            # args = self.getargs(self.lastpos, value)
            if len(self.cells) <= self.lastpos + 5:
                self.cells.extend([0 for j in range(self.lastpos - len(self.cells) + 10)])
            a =self.cells[self.lastpos+1]
            b =self.cells[self.lastpos+2]
            c =self.cells[self.lastpos+3]
            if value[0] == 1:
                if value[1] == 0:
                    if len(self.cells) <= a:
                        self.cells.extend([0 for j in range(a - len(self.cells) + 10)])
                    a =self.cells[a]
                elif value[1] == 2:
                    if len(self.cells) <= a + self.revbase:
                        self.cells.extend([0 for j in range(a + self.revbase - len(self.cells) + 10)])
                    a =self.cells[a + self.revbase] 
                if value[2] == 0:
                    if len(self.cells) <= b:
                        self.cells.extend([0 for j in range(b - len(self.cells) + 10)])
                    b =self.cells[b]
                elif value[2] == 2:
                    if len(self.cells) <= a + self.revbase:
                        self.cells.extend([0 for j in range(b + self.revbase - len(self.cells) + 10)])
                    b =self.cells[b + self.revbase]  
                if value[3] == 2:
                    c = c + self.revbase
                if len(self.cells) <= c:
                    self.cells.extend([0 for j in range(c - len(self.cells) + 10)])
                self.cells[c] = a + b
                self.lastpos+= 4
            elif value[0] == 2:
                if value[1] == 0:
                    if len(self.cells) <= a:
                        self.cells.extend([0 for j in range(a - len(self.cells) + 10)])
                    a =self.cells[a]
                elif value[1] == 2:
                    if len(self.cells) <= a + self.revbase:
                        self.cells.extend([0 for j in range(a + self.revbase - len(self.cells) + 10)])
                    a =self.cells[a + self.revbase] 
                if value[2] == 0:
                    if len(self.cells) <= b:
                        self.cells.extend([0 for j in range(b - len(self.cells) + 10)])
                    b =self.cells[b]
                elif value[2] == 2:
                    if len(self.cells) <= a + self.revbase:
                        self.cells.extend([0 for j in range(b + self.revbase - len(self.cells) + 10)])
                    b =self.cells[b + self.revbase]  
                if value[3] == 2:
                    c = c + self.revbase
                if len(self.cells) <= c:
                    self.cells.extend([0 for j in range(c - len(self.cells) + 10)])
                self.cells[c] = a * b
                self.lastpos+=4
            elif value[0] == 3:
                if len(self.inputs) == 0:
                    break
                if value[1] == 2:
                    a = a + self.revbase
                if len(self.cells) <= a:
                    self.cells.extend([0 for j in range(a - len(self.cells) + 10)])
                self.cells[a] = self.inputs.pop(0)
                self.lastpos+=2
            elif value[0] == 4:
                if value[1] == 0:
                    if len(self.cells) <= a:
                        self.cells.extend([0 for j in range(a - len(self.cells) + 10)])
                    a =self.cells[a]
                elif value[1] == 2:
                    if len(self.cells) <= a + self.revbase:
                        self.cells.extend([0 for j in range(a + self.revbase - len(self.cells) + 10)])
                    a = self.cells[a + self.revbase] 
                outputs.append(a)
                self.lastpos+=2
            elif value[0] == 5:
                if value[1] == 0:
                    if len(self.cells) <= a:
                        self.cells.extend([0 for j in range(a - len(self.cells) + 10)])
                    a =self.cells[a]
                elif value[1] == 2:
                    if len(self.cells) <= a + self.revbase:
                        self.cells.extend([0 for j in range(a + self.revbase - len(self.cells) + 10)])
                    a =self.cells[a + self.revbase] 
                if value[2] == 0:
                    if len(self.cells) <= b:
                        self.cells.extend([0 for j in range(b - len(self.cells) + 10)])
                    b =self.cells[b]
                elif value[2] == 2:
                    if len(self.cells) <= a + self.revbase:
                        self.cells.extend([0 for j in range(b + self.revbase - len(self.cells) + 10)])
                    b =self.cells[b + self.revbase]  
                if a != 0:
                    self.lastpos = b
                else:
                    self.lastpos+= 3
            elif value[0] == 6:
                if value[1] == 0:
                    if len(self.cells) <= a:
                        self.cells.extend([0 for j in range(a - len(self.cells) + 10)])
                    a =self.cells[a]
                elif value[1] == 2:
                    if len(self.cells) <= a + self.revbase:
                        self.cells.extend([0 for j in range(a + self.revbase - len(self.cells) + 10)])
                    a =self.cells[a + self.revbase] 
                if value[2] == 0:
                    if len(self.cells) <= b:
                        self.cells.extend([0 for j in range(b - len(self.cells) + 10)])
                    b =self.cells[b]
                elif value[2] == 2:
                    if len(self.cells) <= a + self.revbase:
                        self.cells.extend([0 for j in range(b + self.revbase - len(self.cells) + 10)])
                    b =self.cells[b + self.revbase]  
                if a == 0:
                    self.lastpos = b
                else:
                    self.lastpos+= 3
            elif value[0] == 7:
                if value[1] == 0:
                    if len(self.cells) <= a:
                        self.cells.extend([0 for j in range(a - len(self.cells) + 10)])
                    a =self.cells[a]
                elif value[1] == 2:
                    if len(self.cells) <= a + self.revbase:
                        self.cells.extend([0 for j in range(a + self.revbase - len(self.cells) + 10)])
                    a =self.cells[a + self.revbase] 
                if value[2] == 0:
                    if len(self.cells) <= b:
                        self.cells.extend([0 for j in range(b - len(self.cells) + 10)])
                    b =self.cells[b]
                elif value[2] == 2:
                    if len(self.cells) <= a + self.revbase:
                        self.cells.extend([0 for j in range(b + self.revbase - len(self.cells) + 10)])
                    b =self.cells[b + self.revbase]  
                if value[3] == 2:
                    c = c + self.revbase
                if len(self.cells) <= c:
                    self.cells.extend([0 for j in range(c - len(self.cells) + 10)])
                if a < b:
                    self.cells[c] = 1
                else:
                    self.cells[c] = 0
                self.lastpos+= 4
            elif value[0] == 8:
                if value[1] == 0:
                    if len(self.cells) <= a:
                        self.cells.extend([0 for j in range(a - len(self.cells) + 10)])
                    a =self.cells[a]
                elif value[1] == 2:
                    if len(self.cells) <= a + self.revbase:
                        self.cells.extend([0 for j in range(a + self.revbase - len(self.cells) + 10)])
                    a =self.cells[a + self.revbase] 
                if value[2] == 0:
                    if len(self.cells) <= b:
                        self.cells.extend([0 for j in range(b - len(self.cells) + 10)])
                    b =self.cells[b]
                elif value[2] == 2:
                    if len(self.cells) <= a + self.revbase:
                        self.cells.extend([0 for j in range(b + self.revbase - len(self.cells) + 10)])
                    b =self.cells[b + self.revbase]  
                if value[3] == 2:
                    c = c + self.revbase
                if len(self.cells) <= c:
                    self.cells.extend([0 for j in range(c - len(self.cells) + 10)])
                if a == b:
                    self.cells[c] = 1
                else:
                    self.cells[c] = 0
                self.lastpos+= 4
            elif value[0] == 9:
                if value[1] == 0:
                    if len(self.cells) <= a:
                        self.cells.extend([0 for j in range(a - len(self.cells) + 10)])
                    a =self.cells[a]
                elif value[1] == 2:
                    if len(self.cells) <= a + self.revbase:
                        self.cells.extend([0 for j in range(a + self.revbase - len(self.cells) + 10)])
                    a =self.cells[a + self.revbase] 
                self.revbase += a
                self.lastpos+=2
            elif value[0] == 99:
                break
            else:
                print value[0]
                print "Error"
                break
        return [outputs, value[0]]