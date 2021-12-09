from lib import read_input_heights


def part1(data):
    return sum(data[x][y] + 1 for x, y in find_all_lows(data))


def part2(data):
    lows = find_all_lows(data)
    sizes = [find_size(x[0], x[1], data) for x in lows]
    sizes.sort(reverse=True)
    return sizes[0] * sizes[1] * sizes[2]


def find_all_lows(data):
    result = []

    for indx, row in enumerate(data):
        for indy, number in enumerate(row):
            absolute_min = True

            if (indx - 1) >= 0 and data[indx - 1][indy] <= number:
                absolute_min = False
            if (indy - 1) >= 0 and data[indx][indy - 1] <= number:
                absolute_min = False
            if (indy + 1) < len(row) and data[indx][indy + 1] <= number:
                absolute_min = False
            if (indx + 1) < len(data) and data[indx + 1][indy] <= number:
                absolute_min = False

            if absolute_min:
                result.append((indx, indy))

    return result


def find_size(i, j, data):
    result = 0
    queue = [(i, j)]
    visited = set()
    while queue:
        x, y = queue.pop()

        if (x, y) in visited:
            continue
        visited.add((x, y))
        if data[x][y] == 9:
            continue
        result += 1

        if x > 0 and data[x][y] < data[x - 1][y]:
            queue.append((x - 1, y))
        if y > 0 and data[x][y] < data[x][y - 1]:
            queue.append((x, y - 1))
        if x < len(data) - 1 and data[x][y] < data[x + 1][y]:
            queue.append((x + 1, y))
        if y < len(data[0]) - 1 and data[x][y] < data[x][y + 1]:
            queue.append((x, y + 1))

    return result


if __name__ == '__main__':
    print(part1(read_input_heights("day09.txt")))
    print(part2(read_input_heights("day09.txt")))
