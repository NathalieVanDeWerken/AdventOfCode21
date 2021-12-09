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

        segment_maps_to_a = next(iter(set(find_digit_with_len_n(x, 3))
                                      - set(find_digit_with_len_n(x, 2))))
        segment_maps_to_b = find_char_with_n_occurrences(all_characters, 6)
        segment_maps_to_c = next(iter(set(find_char_with_n_occurrences_multiple(all_characters, 8))
                                      - set(segment_maps_to_a)))
        segment_maps_to_e = find_char_with_n_occurrences(all_characters, 4)
        segment_maps_to_f = find_char_with_n_occurrences(all_characters, 9)
        segment_maps_to_d = next(iter(set(find_digit_with_len_n(x, 4))
                                      - {segment_maps_to_b, segment_maps_to_c, segment_maps_to_f}))
        segment_maps_to_g = next(iter(set(find_char_with_n_occurrences_multiple(all_characters, 7))
                                      - set(segment_maps_to_d)))

        mappings[segment_maps_to_a] = 'a'
        mappings[segment_maps_to_b] = 'b'
        mappings[segment_maps_to_c] = 'c'
        mappings[segment_maps_to_d] = 'd'
        mappings[segment_maps_to_e] = 'e'
        mappings[segment_maps_to_f] = 'f'
        mappings[segment_maps_to_g] = 'g'

        code = ""
        for y in output[ind]:
            code += decipher(y, mappings)
        result += int(code)
    return result


def find_char_with_n_occurrences(data, n):
    for char in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
        if data.count(char) == n:
            return char


def find_digit_with_len_n(data, n):
    for digit in data:
        if len(digit) == n:
            return list(digit)


def find_char_with_n_occurrences_multiple(data, n):
    result = []
    for char in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
        if data.count(char) == n:
            result.append(char)
    return result


def decipher(digit, mappings):
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
    elif all_correct_lines == {'b', 'c', 'd', 'f'}:
        return "4"
    elif all_correct_lines == {'a', 'b', 'd', 'f', 'g'}:
        return "5"
    elif all_correct_lines == {'a', 'b', 'd', 'e', 'f', 'g'}:
        return "6"
    elif all_correct_lines == {'a', 'c', 'f'}:
        return "7"
    elif all_correct_lines == {'a', 'b', 'c', 'd', 'e', 'f', 'g'}:
        return "8"
    else:
        return "9"


if __name__ == '__main__':
    print(part1(read_input_digits("day08.txt")[1]))
    print(part2(read_input_digits("day08.txt")[0], read_input_digits("day08.txt")[1]))
