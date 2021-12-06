from queue import PriorityQueue

from lib import read_input_list_single_line

def part1(data):
    fish = []
    for x in data:
        fish.append(int(x))
    for i in range(0,80):
        for j,x in enumerate(fish):
            if x == 0:
                fish[j] = 6
                fish.append(9)
            else:
                fish[j] -= 1
    return len(fish)

def part2(data):
    lengths = [0] * 9
    for x in data:
        lengths[int(x)] += 1
    for i in range(0,256):
        done_fish = lengths[0]
        lengths.pop(0)
        lengths.append(done_fish)
        lengths[6] += done_fish
    return sum(lengths)


if __name__ == '__main__':
    print(part1(read_input_list_single_line("day6.txt")))
    print(part2(read_input_list_single_line("day6.txt")))