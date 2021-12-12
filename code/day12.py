from lib import read_input_graphs


def part1(data):
    return find_paths(data, 'start', ['start'], True)


def part2(data):
    return find_paths(data, 'start', ['start'], False)


def find_paths(data, node, current_path, threshold_met):
    result = 0
    edges = data[node]
    for x in edges:
        if x == "end":
            result += 1
            continue
        if x == "start":
            continue
        if x.islower() and x in current_path and threshold_met:
            continue
        if x.islower() and x in current_path and not threshold_met:
            current_path.append(x)
            result += find_paths(data, x, current_path, True)
        else:
            current_path.append(x)
            result += find_paths(data, x, current_path, threshold_met)
        current_path.pop()
    return result


if __name__ == '__main__':
    print(part1(read_input_graphs("day12.txt")))
    print(part2(read_input_graphs("day12.txt")))
