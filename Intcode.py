#version 3.0. Day 7.

#Usage:
#Initialize with intcode(cells), where cells is a list representing the intcode memory
#Add inputs using addinputs(inputs), where inputs is a list of inputs to add
#Run the the machien with run(). Machine will stop on either an input command without an input or a halt command.

class intcode:
    oplen = {1: 3,2: 3,3: 1,4: 1,5: 2,6: 2,7: 3,8: 3,99: 0}
    outs = [1, 2, 3, 7, 8]
    def __init__(self, cells):
        self.cells = cells
        self.inputs = []
        self.lastpos = 0
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
            mode = 1
            if nums[i] == 0:
                if i == len(nums) - 1:
                    if nums[0] in self.outs:
                        mode = 2
            else:
                mode = 2
            if mode == 1:
                out.append(self.cells[self.cells[start+i]])
            else:
                out.append(self.cells[start+i])
        return out
    def addinputs(self, inputs):
        self.inputs.extend(inputs)
    def run(self):
        outputs = []
        while True:
            value = self.cells[self.lastpos]
            value = self.interp(value)
            args = self.getargs(self.lastpos, value)
            if value[0] == 1:
                self.cells[args[3]] = args[1] + args[2]
                self.lastpos+= 4
            elif value[0] == 2:
                self.cells[args[3]] = args[1] * args[2]
                self.lastpos+=4
            elif value[0] == 3:
                if len(self.inputs) == 0:
                    break
                self.cells[args[1]] = self.inputs.pop(0)
                self.lastpos+=2
            elif value[0] == 4:
                outputs.append(args[1])
                self.lastpos+=2
            elif value[0] == 5:
                if args[1] != 0:
                    self.lastpos = args[2]
                else:
                    self.lastpos+= 3
            elif value[0] == 6:
                if args[1] == 0:
                    self.lastpos = args[2]
                else:
                    self.lastpos+= 3
            elif value[0] == 7:
                if args[1] < args[2]:
                    self.cells[args[3]] = 1
                else:
                    self.cells[args[3]] = 0
                self.lastpos+= 4
            elif value[0] == 8:
                if args[1] == args[2]:
                    self.cells[args[3]] = 1
                else:
                    self.cells[args[3]] = 0
                self.lastpos+= 4
            elif value[0] == 99:
                break
            else:
                print value[0]
                print "Error"
                break
        return (outputs, value[0])