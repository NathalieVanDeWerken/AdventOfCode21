import statistics

from lib import read_input_list_line

def part1(data):
    return score(data)[0]

def score(data):
    opening_chars = {'(', '[', '{', '<'}
    stack = []
    score = 0
    score_3 = []
    for x in data:
        for y in x:
            if y in opening_chars:
                stack.append(y)
            else:
                prev = stack.pop()
                if y == ')' and prev != '(':
                    score += 3
                    stack = []
                    break
                if y == ']' and prev != '[':
                    score += 57
                    stack = []
                    break
                if y == '}' and prev != '{':
                    score += 1197
                    stack = []
                    break
                if y == '>' and prev != '<':
                    score += 25137
                    stack = []
                    break
        score_2 = 0
        while stack:
            score_2 *= 5
            el = stack.pop()
            if el == '(':
                score_2 += 1
            if el == '[':
                score_2 += 2
            if el == '{':
                score_2 += 3
            if el == '<':
                score_2 += 4
        if score_2 != 0:
            score_3.append(score_2)
    print(score_3)
    return score, statistics.median(score_3)

def part2(data):
    return score(data)[1]




if __name__ == '__main__':
    print(part1(read_input_list_line("day10_small.txt")))
    print(part2(read_input_list_line("day10.txt")))