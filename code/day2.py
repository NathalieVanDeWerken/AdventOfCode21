from lib import read_input_list_line

def part1(input):
    depth = 0
    horizontal = 0
    for instruc in input:
        instruc = instruc.split(" ")
        if instruc[0] == "forward":
            horizontal += int(instruc[1])
        elif instruc[0] == "down":
            depth += int(instruc[1])
        else:
            depth -= int(instruc[1])
    return depth * horizontal

def part2(input):
    depth = 0
    horizontal = 0
    aim = 0
    for instruc in input:
        instruc = instruc.split(" ")
        if instruc[0] == "forward":
            horizontal += int(instruc[1])
            depth += aim * int(instruc[1])
        elif instruc[0] == "down":
            aim += int(instruc[1])
        else:
            aim -= int(instruc[1])
    return depth * horizontal


if __name__ == '__main__':
    print(part1(read_input_list_line("day2.txt")))
    print(part2(read_input_list_line("day2.txt")))