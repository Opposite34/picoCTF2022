arr = [128,63,131,198,262,110,309,73,276,285,316,161,151,73,219,150,145,217,103,226,41,255]
moddedArr = []

for num in arr:
    moddedArr.append(pow(num, -1, 41))

print(moddedArr)

decoded = ""

for num in moddedArr:
    if num < 27:
        num += 64

    elif num < 37:
        num += 21

    else:
        num = 95

    decoded += chr(num)

print(decoded)