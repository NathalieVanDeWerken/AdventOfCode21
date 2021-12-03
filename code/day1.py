from lib import read_input_list_int

def part1(input):
    res = 0
    for i in range(0, len(input) - 1):
        if input[i] < input[i+1]:
            res += 1
    return res

def part2(input):
    res = 0
    for i in range(0, len(input) - 3):
        if(input[i] < input[i+3]):
            res += 1
    return res


if __name__ == '__main__':
    print(part1(read_input_list_int("day1.txt")))
    print(part2(read_input_list_int("day1.txt")))