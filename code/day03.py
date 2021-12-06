from lib import *


def part1(data):
    gamma = ''
    counts = count_ones_per_column(data)

    len(data[0]) - 2
    for digit in counts:
        if digit > len(data) / 2:
            gamma += '1'
        else:
            gamma += '0'
    return int(gamma, 2) * (2 ** (len(data[0])) - 1 - int(gamma, 2))


def part2(data):
    index = 0
    input_copy = data.copy()
    while len(input_copy) > 1:
        ones_per_column = count_ones_per_column(input_copy)
        input_copy = list(filter(lambda x:
                                 ((x[index] == '1' and ones_per_column[index] >= len(input_copy) / 2) or
                                  (x[index] == '0' and ones_per_column[index] < len(input_copy) / 2)), input_copy))
        index += 1
    oxygen = input_copy[0]

    index = 0
    input_copy = data.copy()
    while len(input_copy) > 1:
        ones_per_column = count_ones_per_column(input_copy)
        input_copy = list(filter(lambda x:
                                 ((x[index] == '1' and ones_per_column[index] < len(input_copy) / 2) or
                                  (x[index] == '0' and ones_per_column[index] >= len(input_copy) / 2)), input_copy))
        index += 1
    scrubber = input_copy[0]

    return int(oxygen, 2) * int(scrubber, 2)


def count_ones_per_column(array):
    counts = [0] * len(array[0])
    for string in array:
        index = 0
        for char in string:
            if char == '1':
                counts[index] += 1
            index += 1
    return counts


if __name__ == '__main__':
    print(part1(read_input_list_line("day03.txt")))
    print(part2(read_input_list_line("day03.txt")))
