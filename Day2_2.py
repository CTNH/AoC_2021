f = open("inputs/Day2.txt", "r")

horiz = 0
depth = 0
aim = 0

for i in f:
    tmp = i.strip("\n").split(" ")
    if tmp[0] == "forward":
        horiz += int(tmp[1])
        depth += aim * int(tmp[1])
    elif tmp[0] == "down":
        aim += int(tmp[1])
    elif tmp[0] == "up":
        aim -= int(tmp[1])

print(depth)
print(horiz)
print(aim)

print(depth*horiz)

f.close()
