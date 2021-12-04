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

def read_input_bingo(path):
    path = os.path.dirname(os.getcwd()) + "/input/" + path
    f = open(path)
    numbers = [int(i) for i in list(f.readline().strip().split(","))]
    f.readline()
    cards = []
    currentCard = []
    for line in f:
        if line == "\n":
            cards.append(currentCard)
            currentCard = []
        else:
            currentCard.append(list([int(i) for i in list(line.lstrip().strip("\n").split())]))
    cards.append(currentCard)
    return numbers, cards
