from lib import read_input_heights


def part1(data):
    return sum(data[x[0]][x[1]] for x in find_all_lows(data)) + len(find_all_lows(data))


def part2(data):
    lows = find_all_lows(data)
    sizes = [find_size(x[0], x[1], data) for x in lows]
    sizes.sort(reverse=True)
    return sizes[0] * sizes[1] * sizes[2]


def find_all_lows(data):
    result = []
    for indy, row in enumerate(data):
        for indx, number in enumerate(row):
            absolute_min = True
            if (indy - 1) >= 0 and data[indy - 1][indx] <= number:
                absolute_min = False
            if (indx - 1) >= 0 and data[indy][indx - 1] <= number:
                absolute_min = False
            if (indx + 1) < len(row) and data[indy][indx + 1] <= number:
                absolute_min = False
            if (indy + 1) < len(data) and data[indy + 1][indx] <= number:
                absolute_min = False
            if absolute_min:
                result.append((indy, indx))
    return result


def find_size(i, j, data):
    result = 1
    queue = []
    visited = {(i, j)}
    if i < len(data) - 1:
        queue.append((i + 1, j))
    if i > 0:
        queue.append((i - 1, j))
    if j < len(data[0]) - 1:
        queue.append((i, j + 1))
    if j > 0:
        queue.append((i, j - 1))
    while queue:
        element = queue.pop()
        x = element[0]
        y = element[1]
        if element in visited:
            continue
        visited.add(element)
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
