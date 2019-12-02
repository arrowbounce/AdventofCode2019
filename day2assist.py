f = open("day2", "r")
cells = f.read().split(',')
cells = [int(i) for i in cells]
i = 0
while i < len(cells):
	print cells[i:i+4]
	i+=4
#initial attempt at trying to figure out pattern, by seeing individual commands.