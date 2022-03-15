modded = [17, 26, 20, 13, 3, 36, 13, 36, 17, 26, 20, 13, 3, 36, 34, 2, 34, 32, 29, 4, 4, 33]
decoded = ""

for num in modded:
    if num < 26:
        num += 65

    elif num < 36:
        num += 22

    else:
        num = 95

    decoded += chr(num)

print(decoded)