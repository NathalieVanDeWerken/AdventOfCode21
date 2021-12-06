from lib import read_input_list_line


def part1(data):
    depth = 0
    horizontal = 0
    for instruction in data:
        instruction = instruction.split(" ")
        if instruction[0] == "forward":
            horizontal += int(instruction[1])
        elif instruction[0] == "down":
            depth += int(instruction[1])
        else:
            depth -= int(instruction[1])
    return depth * horizontal


def part2(data):
    depth = 0
    horizontal = 0
    aim = 0
    for instruction in data:
        instruction = instruction.split(" ")
        if instruction[0] == "forward":
            horizontal += int(instruction[1])
            depth += aim * int(instruction[1])
        elif instruction[0] == "down":
            aim += int(instruction[1])
        else:
            aim -= int(instruction[1])
    return depth * horizontal


if __name__ == '__main__':
    print(part1(read_input_list_line("day02.txt")))
    print(part2(read_input_list_line("day02.txt")))
