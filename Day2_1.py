f = open("inputs/Day2.txt", "r")

horiz = 0
depth = 0

for i in f:
    tmp = i.strip("\n").split(" ")
    if tmp[0] == "forward":
        horiz += int(tmp[1])
    elif tmp[0] == "down":
        depth += int(tmp[1])
    elif tmp[0] == "up":
        depth -= int(tmp[1])

print(depth)
print(horiz)

print(depth*horiz)

f.close()
