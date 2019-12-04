def legal(i):
    for x in range(0, 10):
        if str(i).count(str(x)) == 2:
            prev = 0
            for x in str(i):
                if x < prev:
                    return False
                prev = x
            return True
    return False

a = 172851
b = 675869
total = 0
for i in range(a, b+1):
    if legal(i):
        total += 1
print total