import re

import numpy as np

from lib import read_input_list_line


def part1(data):
    grid = load_in_data(data, False)
    return count_number_of_2s_or_more(grid)


def load_in_data(data, diagonal):
    grid = np.zeros(1000000).reshape(1000, 1000)
    for line in data:
        line = [int(x) for x in re.split(' -> |,', line)]
        if (line[0] == line[2]):
            if line[1] < line[3]:
                grid[line[0], line[1]:line[3] + 1] += 1
            else:
                grid[line[0], line[3]:line[1] + 1] += 1
        elif line[1] == line[3]:
            if line[0] < line[2]:
                grid[line[0]:line[2] + 1, line[1]] += 1
            else:
                grid[line[2]:line[0] + 1, line[1]] += 1
        elif(diagonal):
            x1 = line[0]
            y1 = line[1]
            x2 = line[2]
            y2 = line[3]
            if (x1 < x2 and y1 < y2) or (x1 > x2 and y1 > y2):
                for i in range(0, max(x1, x2) - min(x1,x2) + 1):
                    grid[min(x1,x2) + i, min(y1,y2) + i] += 1
            else:
                for i in range(0, max(x1, x2) - min(x1,x2) + 1):
                    grid[min(x1,x2) + i, max(y1,y2) - i] += 1

    return grid


def count_number_of_2s_or_more(grid):
    result = 0
    for x in np.nditer(grid):
        if x >= 2:
            result += 1
    return result


def part2(data):
    grid = load_in_data(data, True)
    return count_number_of_2s_or_more(grid)


if __name__ == '__main__':
    print(part1(read_input_list_line("day5.txt")))
    print(part2(read_input_list_line("day5.txt")))
