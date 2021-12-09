with open("input.txt", "r") as file:
    lines = file.readlines()
    lines = [s.strip() for s in lines]

with open("output.txt", "w") as file:
    for line in lines:
        file.write("".join(["0" if s == "9" else "." for s in line]))
        file.write("\n")

print("Day 9")
print("Part 1")

import numpy as np

height_map = np.array([np.array([int(d) for d in line]) for line in lines])

low_points = []
risk_levels = []
for x in range(len(height_map)):
    for y in range(len(height_map[0])):
        if y < len(height_map[0]) - 1 and not height_map[x][y] < height_map[x][y + 1]:
            continue
        if y > 0 and not height_map[x][y] < height_map[x][y - 1]:
            continue
        if x < len(height_map) - 1 and not height_map[x][y] < height_map[x + 1][y]:
            continue
        if x > 0 and not height_map[x][y] < height_map[x - 1][y]:
            continue
        risk_levels.append(height_map[x][y] + 1)
        low_points.append((x, y))

print("Total risk (answer):", sum(risk_levels))  # 448

print("")
print("Part 2")


class Basin:
    def __init__(self, low_point):
        self.uncovered_points = [low_point]
        self.discovered_points = []

    def uncover(self, height):
        while self.uncovered_points:
            point = self.uncovered_points.pop()
            self.discovered_points.append(point)
            if point[0] > 0:  # left
                p = (point[0]-1, point[1])
                left = height[point[0]-1][point[1]]
                if left != 9 and p not in self.discovered_points and p not in self.uncovered_points:
                    self.uncovered_points.append(p)
            if point[0] < len(height)-1:  # right
                p = (point[0]+1, point[1])
                right = height[p[0]][p[1]]
                if right != 9 and p not in self.discovered_points and p not in self.uncovered_points:
                    self.uncovered_points.append(p)
            if point[1] > 0:  # up
                p = (point[0], point[1]-1)
                up = height[p[0]][p[1]]
                if (up != 9) and (p not in self.discovered_points) and (p not in self.uncovered_points):
                    self.uncovered_points.append(p)
            if point[1] < len(height[0])-1:  # down
                p = (point[0], point[1]+1)
                down = height[p[0]][p[1]]
                if down != 9 and p not in self.discovered_points and p not in self.uncovered_points:
                    self.uncovered_points.append(p)

    def size(self):
        return len(self.discovered_points)


basins = [Basin(p) for p in low_points]

sizes = []
for basin in basins:
    basin.uncover(height_map)
    sizes.append(basin.size())

print("Product of 3 largest cave sizes (answer):", np.prod(sorted(sizes, reverse=True)[:3]))  # 1417248
