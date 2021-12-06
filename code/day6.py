from lib import read_input_list_single_line


def part1(data):
    return count_fish(data, 80)


def part2(data):
    return count_fish(data, 256)


def count_fish(data, days):
    number_of_fish = [0] * 9
    for x in data:
        number_of_fish[x] += 1
    for i in range(0, days):
        number_of_timer_done = number_of_fish[0]
        number_of_fish.pop(0)
        number_of_fish.append(number_of_timer_done)
        number_of_fish[6] += number_of_timer_done
    return sum(number_of_fish)


def count_fish_naive(data, days):
    fish = []
    for x in data:
        fish.append(x)
    for i in range(0, days):
        for ind, timer in enumerate(fish):
            if timer == 0:
                fish[ind] = 6
                fish.append(9)
            else:
                fish[timer] -= 1
    return len(fish)


if __name__ == '__main__':
    print(part1(read_input_list_single_line("day6.txt")))
    print(part2(read_input_list_single_line("day6.txt")))
