with open("input.txt", "r") as file:
    lines = file.readline()

print("Day 7")
print("Part 1")

import numpy as np

positions = sorted([int(h) for h in lines.split(",")])
positions = np.array(positions)

min_fuel = -1
for i in range(positions[0], positions[-1]+1):
    movements = np.abs(positions - i)
    fuel = np.sum(movements)
    if min_fuel == -1 or fuel < min_fuel:
        min_fuel = fuel
        print(i)

print("minimum fuel (answer):", min_fuel)
print()
print("Part 2")

min_fuel = -1
for i in range(positions[0], positions[-1]+1):
    movements = np.abs(positions - i)
    fuel = np.sum([sum(range(0, m+1)) for m in movements])
    if min_fuel == -1 or fuel < min_fuel:
        min_fuel = fuel

print("minimum fuel (answer):", min_fuel)
