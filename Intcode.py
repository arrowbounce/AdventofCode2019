f = open("day2", "r")
cells = f.read().split(',')
cells = [int(i) for i in cells]
i = 0
while True:
	value = cells[i]
	if value == 1:
		cells[cells[i+3]] = cells[cells[i+2]] + cells[cells[i+1]]
	elif value == 2:
		cells[cells[i+3]] = cells[cells[i+2]] * cells[cells[i+1]]
	elif value == 99:
		break
	else:
		print "Error"
		break
	i += 4
print cells[0]
