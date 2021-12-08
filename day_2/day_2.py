with open("input.txt", "r") as file:
    lines = file.readlines()

horizontal = 0
depth = 0

# part 1
print("Part 1")
for line in lines:
    direction = line.split(" ")[0]
    amount = int(line.split(" ")[1])

    if direction == 'forward':
        horizontal += amount
    if direction == 'down':
        depth += amount
    if direction == 'up':
        depth -= amount

print("h: ", horizontal)
print("d: ", depth)
print("answer: ", horizontal*depth)

# part 2
print("Part 2")
aim = 0
horizontal = 0
depth = 0

for line in lines:
    direction = line.split(" ")[0]
    amount = int(line.split(" ")[1])

    if direction == 'forward':
        horizontal += amount
        depth += aim*amount
    if direction == 'down':
        aim += amount
    if direction == 'up':
        aim -= amount

print("aim: ", aim)
print("h: ", horizontal)
print("d: ", depth)
print("answer: ", horizontal*depth)

