import re

import numpy as np

with open("input.txt", "r") as file:
    drawstring = file.readline()
    file.readline()
    lines = file.readlines()

print("Day 4")
print("Part 1")


class Board:
    def __init__(self, numbers):
        self.numbers = numbers
        self.marked = np.array([
            np.array([0, 0, 0, 0, 0]),
            np.array([0, 0, 0, 0, 0]),
            np.array([0, 0, 0, 0, 0]),
            np.array([0, 0, 0, 0, 0]),
            np.array([0, 0, 0, 0, 0]),
        ]
        )

    def bingo(self):

        return np.any(np.sum(self.marked, axis=0) == 5) or np.any(np.sum(self.marked, axis=1) == 5)

    def mark(self, number):
        to_mark = np.where(self.numbers == number)
        for i in range(len(to_mark[0])):
            self.marked[to_mark[0][i]][to_mark[1][i]] = 1

    def print(self):
        for i, row in enumerate(self.numbers):
            for j, cell in enumerate(row):
                print(str(cell) + ("_" if self.marked[i][j] else ""), end="\t")
            print("")

    def score(self, last_draw):
        return np.sum(self.numbers[np.where(self.marked == 0)]) * last_draw


boards = []
produce_board = []
for line in lines:
    if line == "\n":
        boards.append(Board(np.array(produce_board)))
        produce_board = []
    else:
        items = re.findall('[0-9]+', line)
        produce_board.append(np.array([int(x) for x in items]))

draws = drawstring.split(",")

bingo = False
for s in draws:
    draw = int(s)
    for board in boards:
        board.mark(draw)
        if board.bingo():
            board.print()
            print("winning score (answer):", board.score(draw))
            bingo = True
            break
    if bingo:
        break

print("")
print("Part 2")

won_boards = 0
for s in draws:
    draw = int(s)
    for board in boards:
        board.mark(draw)
    if len(boards) != 1:
        boards = [b for b in boards if not b.bingo()]
    if len(boards) == 1 and boards[0].bingo():
        boards[0].print()
        print("Losing score (anser):", boards[0].score(draw))
        break
