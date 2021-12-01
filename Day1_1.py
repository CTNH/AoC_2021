f = open("inputs/Day1.txt", "r")

old = int(f.readline())
increase = 0

for i in f:
    if old < int(i):
        increase += 1
    old = int(i)

print("Total: " + str(increase))
f.close()
