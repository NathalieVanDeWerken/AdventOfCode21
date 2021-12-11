from lib import read_input_2d_array


def part1(data):
    result = 0
    for i in range(0, 100):
        result += update_flashes(data)
    return result


def part2(data):
    i = 0
    while True:
        i += 1
        if update_flashes(data) == 100:
            return i


def update_flashes(data):
    flashes = []
    having_flashed = set()
    for y, row in enumerate(data):
        for x, number in enumerate(row):
            data[y][x] += 1
            if number + 1 == 10:
                flashes.append((x, y))
                having_flashed.add((x, y))

    while flashes:
        x, y = flashes.pop()
        for x_new in range(max(0, x - 1), min(len(data) - 1, x + 1) + 1):
            for y_new in range(max(0, y - 1), min(len(data) - 1, y + 1) + 1):
                data[y_new][x_new] += 1
                if (data[y_new][x_new] >= 10) and (x_new, y_new) not in having_flashed:
                    flashes.append((x_new, y_new))
                    having_flashed.add((x_new, y_new))

    for x, y in having_flashed:
        data[y][x] = 0

    return len(having_flashed)


if __name__ == '__main__':
    print(part1(read_input_2d_array("day11.txt")))
    print(part2(read_input_2d_array("day11.txt")))
