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
        data.append(line)
    return data


