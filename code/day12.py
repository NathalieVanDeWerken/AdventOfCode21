from lib import read_input_graphs


def part1(data):
    return find_paths(data, 'start', ['start'])


def find_paths(data, node, current_path):
    result = 0
    edges = data[node]
    for x in edges:
        if x == "end":
            result += 1
            continue
        if x.islower() and x in current_path:
            continue
        current_path.append(x)
        result += find_paths(data, x, current_path)
        current_path.remove(x)
    return result


def part2(data):
    print(data)
    return find_paths_2(data, 'start', ['start'], False)


def find_paths_2(data, node, current_path, bool):
    result = 0
    edges = data[node]
    for x in edges:
        if x == node:
            continue
        if x == "end":
            result += 1
            continue
        if x == "start":
            continue
        if x.islower() and x in current_path and bool:
            continue
        if x.islower() and x in current_path and not bool:
            current_path.append(x)
            result += find_paths_2(data, x, current_path, True)
            current_path.remove(x)
        else:
            current_path.append(x)
            result += find_paths_2(data, x, current_path, bool)
            current_path.remove(x)
    return result

if __name__ == '__main__':
    print(part1(read_input_graphs("day12.txt")))
    print(part2(read_input_graphs("day12.txt")))
