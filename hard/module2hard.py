key = int(input())

result = []

for i in range(1, 21):
    for j in range(1, 21):
        if key % (j + i) == 0 and j > i:
            result.append(i)
            result.append(j)

print(''.join(map(str, result)))
