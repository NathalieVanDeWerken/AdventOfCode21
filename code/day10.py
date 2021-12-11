import statistics

from lib import read_input_list_line


def part1(data):
    return score(data)[0]


def score(data):
    opening_chars = {'(', '[', '{', '<'}
    stack = []
    score_corrupt_lines = 0
    scores_incomplete_lines = []
    for x in data:
        for y in x:
            if y in opening_chars:
                stack.append(y)

            else:
                prev = stack.pop()
                if y == ')' and prev != '(':
                    score_corrupt_lines += 3
                    stack = []
                    break
                if y == ']' and prev != '[':
                    score_corrupt_lines += 57
                    stack = []
                    break
                if y == '}' and prev != '{':
                    score_corrupt_lines += 1197
                    stack = []
                    break
                if y == '>' and prev != '<':
                    score_corrupt_lines += 25137
                    stack = []
                    break

        score_current_line = 0

        while stack:
            score_current_line *= 5
            el = stack.pop()
            if el == '(':
                score_current_line += 1
            if el == '[':
                score_current_line += 2
            if el == '{':
                score_current_line += 3
            if el == '<':
                score_current_line += 4

        if score_current_line != 0:
            scores_incomplete_lines.append(score_current_line)

    return score_corrupt_lines, statistics.median(scores_incomplete_lines)


def part2(data):
    return score(data)[1]


if __name__ == '__main__':
    print(part1(read_input_list_line("day10_small.txt")))
    print(part2(read_input_list_line("day10.txt")))
