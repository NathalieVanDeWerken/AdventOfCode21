import os


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
