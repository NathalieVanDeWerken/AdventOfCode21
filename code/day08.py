import collections
from collections import defaultdict

from lib import read_input_digits


def part1(output):
    result = 0
    for x in output:
        for y in x:
            if len(y) == 2 or len(y) == 4 or len(y) == 3 or len(y) == 7:
                result += 1
    return result

def part2(data, output):
    result = 0
    for ind, x in enumerate(data):
        all_characters = [char for digit in x for char in digit]
        mappings = defaultdict()
        correct_a = next(iter(set(find_correct_length(x, 3)) - set(find_correct_length(x, 2))))
        mappings[correct_a] = 'a'
        mappings[next(iter(set(find_correct_number_multiple(all_characters, 8)) - set(correct_a)))] = 'c'
        correct_b = find_correct_number(all_characters, 6)
        correct_c = next(iter(set(find_correct_number_multiple(all_characters, 8)) - set(correct_a)))
        correct_f = find_correct_number(all_characters, 9)
        mappings[find_correct_number(all_characters, 6)] = 'b'
        mappings[find_correct_number(all_characters, 4)] = 'e'
        mappings[find_correct_number(all_characters, 9)] = 'f'

        correct_d = next(iter(set(find_correct_length(x, 4)) - set([correct_b, correct_c, correct_f])))
        mappings[next(iter(set(find_correct_length(x, 4)) - set([correct_b, correct_c, correct_f])))] = 'd'
        right_now = mappings.keys()
        mappings[next(iter(set(find_correct_number_multiple(all_characters, 7)) - set(correct_d)))] = 'g'

        code = ""
        for y in output[ind]:
          code += decyfer(y, mappings)
        print(code)
        result += int(code)
    return result

def find_correct_number(data, n):
    for char in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
        if data.count(char) == n:
            return char
    return 'z'

def find_correct_length(data, n):
    for digit in data:
        if len(digit) == n:
            return list(digit)

def find_correct_number_multiple(data, n):
    result = []
    for char in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
        if data.count(char) == n:
            result.append(char)
    return result

def decyfer(digit, mappings):
    all_correct_lines = set()
    for x in digit:
        all_correct_lines.add(mappings.get(x))
    if all_correct_lines == {'a', 'b', 'c', 'e', 'f', 'g'}:
        return "0"
    elif all_correct_lines == {'c', 'f'}:
        return "1"
    elif all_correct_lines == {'a', 'c', 'd', 'e', 'g'}:
        return "2"
    elif all_correct_lines == {'a', 'c', 'd', 'f', 'g'}:
        return "3"
    elif all_correct_lines == { 'b', 'c', 'd', 'f'}:
        return "4"
    elif all_correct_lines == {'a', 'b', 'd', 'f', 'g'}:
        return "5"
    elif all_correct_lines == {'a', 'b', 'd', 'e', 'f', 'g'}:
        return "6"
    elif all_correct_lines == {'a', 'c', 'f'}:
        return "7"
    elif all_correct_lines == {'a', 'b', 'c', 'd', 'e', 'f', 'g'}:
        return "8"
    else: return "9"

if __name__ == '__main__':
    print(part1(read_input_digits("day08.txt")[1]))
    print(part2(read_input_digits("day08.txt")[0], read_input_digits("day08.txt")[1]))
