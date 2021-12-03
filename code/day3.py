from lib import *


def part1(input):
    res = 0
    count = [0] * len(input[0])
    for x in input:
        z = 0
        for y in x:
            if (y == '1'):
                count[z] += 1
            z += 1


    j = len(input[0]) - 2
    for x in count:
        if x > len(input)/2 :
            res += (2**j)
        j -= 1
    return (2**(len(input[0])- 1) -1 - res) * res

def part2(input):
    index = 0
    input_copy = input.copy()
    while(len(input_copy) > 1):
        mostCommon = [0] * len(input[0])
        for x in input_copy:
            z = 0
            for y in x:
                if (y == '1'):
                    mostCommon[z] += 1
                z += 1
        input_copy = list(filter(lambda x:
                                 ((x[index] == '1' and int(mostCommon[index]) >= len(input_copy) / 2)
                                  or (x[index] == '0' and int(mostCommon[index]) < len(input_copy) / 2)), input_copy))
        index += 1
    oxygen = input_copy[0]

    index = 0
    input_copy = input.copy()
    while(len(input_copy) > 1):
        mostCommon = [0] * len(input[0])
        for x in input_copy:
            z = 0
            for y in x:
                if (y == '1'):
                    mostCommon[z] += 1
                z += 1
        input_copy = list(filter(lambda x:
                                 ((x[index] == '1' and int(mostCommon[index]) < len(input_copy) / 2)
                                  or (x[index] == '0' and int(mostCommon[index]) >= len(input_copy) / 2)), input_copy))
        index += 1
    scrubber = input_copy[0]

    return int(oxygen, 2) * int(scrubber,2)







if __name__ == '__main__':
    print(part1(read_input_list_line("day3.txt")))
    print(part2(read_input_list_line("day3.txt")))
