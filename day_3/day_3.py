with open("input.txt", "r") as file:
    lines = file.readlines()

print("Day 3")
print("Part 1")

import numpy as np

values = [int(x, 2) for x in lines]
l = np.array([[int(k) for k in list(f)[:-1]] for f in lines])
l = np.transpose(l)

sums = np.sum(l, axis=1)
binary = np.where(sums > 500, 1, 0)
res = int("".join([str(i) for i in binary]), 2)
print("sums: ", sums)
print("binary: ", binary)
print("gamma: ", res)

answer = res * (res ^ (2 ** len(lines[0][:-1]) - 1))
print("power consumption (answer): ", answer)

print("")
print("Part 2")

oxygen = np.transpose(l)

for h in range(len(lines[0]) - 1):
    bits = np.transpose(oxygen)
    percent = sum(bits[h]) / len(bits[h])
    if percent >= 0.5:
        most_common = 1
    else:
        most_common = 0
    oxygen = oxygen[np.where(bits[h] == most_common)]
    if len(oxygen) == 1:
        break
oxygen_res = int("".join([str(x) for x in oxygen[0].tolist()]), 2)
print("oxygen:", oxygen_res)

co2 = np.transpose(l)

for h in range(len(lines[0]) - 1):
    bits = np.transpose(co2)
    percent = sum(bits[h]) / len(bits[h])
    if percent >= 0.5:
        least_common = 0
    else:
        least_common = 1
    co2 = co2[np.where(bits[h] == least_common)]
    if len(co2) == 1:
        break

co2_res = int("".join([str(x) for x in co2[0].tolist()]), 2)
print("CO2:", co2_res)
print("Life support rating (answer):", co2_res * oxygen_res)  # 5736383
