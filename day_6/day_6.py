with open("input.txt", "r") as file:
    lines = file.readline()

print("Day 6")
print("Part 1")

fish = [int(age) for age in lines.split(",")]

combo = [0, 0, 0, 0, 0, 0, 0]
age8 = 0
age7 = 0
for f in fish:
    combo[f] += 1


for i in range(256):
    print("combo:", combo, "t", age7, "tt", age8)
    new_fish = combo[0]
    combo = combo[1:] + [combo[0]]
    combo[6] += age7
    age7 = age8
    age8 = new_fish

print(sum(combo) + age8 + age7)