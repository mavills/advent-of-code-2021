import numpy as np

with open("input.txt", "r") as file:
    lines = file.readlines()

print("Day 5")
print("Part 1")


def points_between(p1, p2, diagonal=False):
    horizontal = 1 if p1[0] < p2[0] else -1
    vertical = 1 if p1[1] < p2[1] else -1
    h_diff = abs(p1[0] - p2[0]) + 1
    v_diff = abs(p1[1] - p2[1]) + 1
    if p1[0] == p2[0]:  # vertical
        return [(p1[0], p1[1] + i*vertical) for i in range(v_diff)]
    if p1[1] == p2[1]:  # horizontal
        return [(p1[0] + i*horizontal, p1[1]) for i in range(h_diff)]
    if diagonal:
        return [(p1[0] + i*horizontal, p1[1] + i*vertical) for i in range(h_diff)]
    else:
        return []


points = []
for line in lines:
    if line == '\n':
        continue
    line = line.strip()
    split = line.split(" -> ")
    cp1 = split[0].split(',')
    cp1 = (int(cp1[0]), int(cp1[1]))
    cp2 = split[1].split(',')
    cp2 = (int(cp2[0]), int(cp2[1]))
    points += points_between(cp1, cp2)

counts = {}
for p in points:
    counts[p] = counts.get(p, 0) + 1
print(len(points))
print("Crossing vents (answer):", len([v for v in counts.values() if v > 1]))  # 7468

print()
print("Part 2")

points = []
for line in lines:
    if line == '\n':
        continue
    line = line.strip()
    split = line.split(" -> ")
    cp1 = split[0].split(',')
    cp1 = (int(cp1[0]), int(cp1[1]))
    cp2 = split[1].split(',')
    cp2 = (int(cp2[0]), int(cp2[1]))
    points += points_between(cp1, cp2, True)


counts = {}
for p in points:
    counts[p] = counts.get(p, 0) + 1
print(len(points))
print("Crossing vents (answer):", len([v for v in counts.values() if v > 1]))  # 22364
