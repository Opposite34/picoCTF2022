arr = [350,372,192,354,139,337,67,311,392,338,241,414,180,277,379,294,128,117,250,404,336,350,386]
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