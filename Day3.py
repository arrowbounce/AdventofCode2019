def checkInter(start, end, dire, other, path):
	check = path.split(",")
	curx = 0
	cury = 0
	curmin = 999999999
	for seg in check:
		newdir = seg[0]
		amount = int(seg[1:])
		if newdir == 'R':
			if dire == 'U':
				if start <= cury <= end and curx <= other <= curx + amount:
					if curmin is None:
						curmin = abs(cury) + abs(other)
					else:
						curmin = min(curmin, abs(cury) + abs(other))
			elif dire == 'D':
				if end <= cury <= start and curx <= other <= curx + amount:
					if curmin is None:
						curmin = abs(cury) + abs(other)
					else:
						curmin = min(curmin, abs(cury) + abs(other))
			curx += amount
		elif newdir == 'L':
			if dire == 'U':
				if start <= cury <= end and curx - amount <= other <= curx:
					if curmin is None:
						curmin = abs(cury) + abs(other)
					else:
						curmin = min(curmin, abs(cury) + abs(other))
			elif dire == 'D':
				if end <= cury <= start and curx - amount <= other <= curx:
					if curmin is None:
						curmin = abs(cury) + abs(other)
					else:
						curmin = min(curmin, abs(cury) + abs(other))
			curx -= amount
		elif newdir == 'U':
			if dire == 'R':
				if start <= curx <= end and cury <= other <= cury + amount:
					if curmin is None:
						curmin = abs(curx) + abs(other)
					else:
						curmin = min(curmin, abs(curx) + abs(other))
			elif dire == 'L':
				if end <= curx <= start and cury <= other <= cury + amount:
					if curmin is None:
						curmin = abs(curx) + abs(other)
					else:
						curmin = min(curmin, abs(curx) + abs(other))
			cury += amount
		elif newdir == 'D':
			if dire == 'R':
				if start <= curx <= end and cury - amount <= other <= cury:
					if curmin is None:
						curmin = abs(curx) + abs(other)
					else:
						curmin = min(curmin, abs(curx) + abs(other))
			elif dire == 'L':
				if end <= curx <= start and cury - amount <= other <= cury:
					if curmin is None:
						curmin = abs(curx) + abs(other)
					else:
						curmin = min(curmin, abs(curx) + abs(other))
			cury -= amount
		else:
			print newdir
	return curmin

f = []
with open("Day3") as fi:
	for line in fi:
		f.append(line)
	line1 = f[0]
	line2 = f[1]
	curx = 0
	cury = 0
	curmin = None
	line1 = line1.split(",")
	for seg in line1:
		newdir = seg[0]
		amount = int(seg[1:])
		if newdir == 'R':
			if curmin is None:
				curmin = checkInter(curx, curx + amount, 'R', cury, line2)
			else:
				curmin = min(curmin, checkInter(curx, curx + amount, 'R', cury, line2))
			curx = curx + amount
		elif newdir == 'L':
			if curmin is None:
				curmin = checkInter(curx, curx + amount, 'R', cury, line2)
			else:
				curmin = min(curmin, checkInter(curx, curx - amount, 'L', cury, line2))
			curx = curx - amount
		elif newdir == 'U':
			if curmin is None:
				curmin = checkInter(curx, curx + amount, 'R', cury, line2)
			else:
				curmin = min(curmin, checkInter(cury, cury + amount, 'U', curx, line2))
			cury = cury + amount
		elif newdir == 'D':
			if curmin is None:
				curmin = checkInter(curx, curx + amount, 'R', cury, line2)
			else:
				curmin = min(curmin, checkInter(cury, cury - amount, 'D', curx, line2))
			cury = cury - amount
print curmin
