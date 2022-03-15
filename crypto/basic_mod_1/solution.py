arr = [128,63,131,198,262,110,309,73,276,285,316,161,151,73,219,150,145,217,103,226,41,255]
moddedArr = []

for num in arr:
    moddedArr.append(num % 37)

print(moddedArr)

decoded = ""

for num in moddedArr:
    if num < 26:
        num += 65

    elif num < 36:
        num += 22

    else:
        num = 95

    decoded += chr(num)

print(decoded)