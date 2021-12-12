import os
from collections import defaultdict


def read_input_list_int(path):
    path = os.path.dirname(os.getcwd()) + "/input/" + path
    f = open(path)
    data = []
    for line in f:
        data.append(int(line))
    return data


def read_input_list_line(path):
    path = os.path.dirname(os.getcwd()) + "/input/" + path
    f = open(path)
    data = []
    for line in f:
        data.append(line.strip("\n"))
    return data


def read_input_list_single_line(path):
    path = os.path.dirname(os.getcwd()) + "/input/" + path
    f = open(path)
    data = [int(x) for x in f.readline().strip("\n").split(',')]
    return data


def read_input_bingo(path):
    path = os.path.dirname(os.getcwd()) + "/input/" + path
    f = open(path)
    numbers = [int(i) for i in list(f.readline().strip().split(","))]
    f.readline()
    cards = []
    current_card = []
    for line in f:
        if line == "\n":
            cards.append(current_card)
            current_card = []
        else:
            current_card.append(list([int(i) for i in list(line.lstrip().strip("\n").split())]))
    cards.append(current_card)
    return numbers, cards


def read_input_digits(path):
    path = os.path.dirname(os.getcwd()) + "/input/" + path
    f = open(path)
    digits = []
    output = []
    for line in f:
        segments = line.split(" | ")
        digits.append(segments[0].split(" "))
        output.append(segments[1].strip("\n").split(" "))
    return digits, output


def read_input_2d_array(path):
    path = os.path.dirname(os.getcwd()) + "/input/" + path
    f = open(path)
    result = []
    for line in f:
        result.append([int(y) for y in line.strip("\n")])
    return result


def read_input_graphs(path):
    path = os.path.dirname(os.getcwd()) + "/input/" + path
    f = open(path)
    result = defaultdict(list)
    for line in f:
        line2 = line.split('-')
        result[line2[0]].append(line2[1].strip("\n"))
        result[line2[1].strip("\n")].append(line2[0])
    return result
