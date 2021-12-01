f = open("inputs/Day1.txt", "r")

val = []
old = 0
for i in range(3):
    val.append(f.readline())
    old += int(val[i])

increase = 0
for i in f:
    sum = 0
    val.pop(0)
    val.append(i)
    for i in val:
        sum += int(i)
    if sum > old:
        increase += 1
    old = sum

print(increase)

f.close()
