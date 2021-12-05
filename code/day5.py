import re

import numpy as np

from lib import read_input_list_line


def part1(data):
    return (fill_grid(data, False) >= 2).sum()


def part2(data):
    return (fill_grid(data, True) >= 2).sum()


def fill_grid(data, diagonal):
    grid = np.zeros(1000000).reshape(1000, 1000)
    for line in data:
        line = [int(x) for x in re.split(' -> |,', line)]
        x1 = line[0]
        y1 = line[1]
        x2 = line[2]
        y2 = line[3]
        if x1 == x2:
            grid[x1, min(y1, y2): max(y1, y2) + 1] += 1
        elif y1 == y2:
            grid[min(x1, x2): max(x1, x2) + 1, y1] += 1
        elif diagonal:
            if (x1 < x2 and y1 < y2) or (x1 > x2 and y1 > y2):
                for i in range(0, max(x1, x2) - min(x1, x2) + 1):
                    grid[min(x1, x2) + i, min(y1, y2) + i] += 1
            else:
                for i in range(0, max(x1, x2) - min(x1, x2) + 1):
                    grid[min(x1, x2) + i, max(y1, y2) - i] += 1
    return grid


if __name__ == '__main__':
    print(part1(read_input_list_line("day5.txt")))
    print(part2(read_input_list_line("day5.txt")))
