import math
sum = 0
with open("day1") as f:
	for line in f:
		hold = math.floor(int(line)/3) - 2
		while hold >= 0:
			sum += hold
			hold = math.floor(hold/3) - 2
print sum