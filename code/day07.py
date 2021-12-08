import statistics
import sys

from lib import read_input_list_single_line


def part1(data):
    minimal_result = sys.maxsize
    for height in range(min(data), max(data) + 1):
        result = 0
        for crab in data:
            result += abs(crab - height)
        minimal_result = min(result, minimal_result)
    return minimal_result


def part1_optimized(data):
    median = statistics.median(data)
    result = 0
    for crab in data:
        result += int(abs(crab - median))
    return result


def part1_oneliner(data):
    return min(sum(abs(x - height) for x in data) for height in range(min(data), max(data)))


def part2_oneliner(data):
    return min(sum(abs(x - h) * (abs(x - h) + 1) // 2 for x in data) for h in range(min(data), max(data)))


def part2(data):
    minimal_result = sys.maxsize
    for height in range(min(data), max(data) + 1):
        result = 0
        for crab in data:
            result += int((abs(crab - height) * (abs(crab - height) + 1)) / 2)
        minimal_result = min(result, minimal_result)
    return minimal_result


if __name__ == '__main__':
    print(part1_oneliner(read_input_list_single_line("day07.txt")))
    print(part2_oneliner(read_input_list_single_line("day07.txt")))
