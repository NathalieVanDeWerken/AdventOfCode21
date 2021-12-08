from lib import read_input_bingo


def part1(numbers, cards):
    for number in numbers:
        update_cards(cards, number)
        bingo_or_not, ind = check_bingo(cards)
        if bingo_or_not:
            return number * sum(list(filter(lambda x: x != -1, [num for row in cards[ind] for num in row])))

    return 0


def part2(numbers, cards):
    for number in numbers:
        update_cards(cards, number)
        bingo_or_not, ind = check_bingo(cards)
        while bingo_or_not and len(cards) > 1:
            cards.pop(ind)
            bingo_or_not, ind = check_bingo(cards)

        if bingo_or_not and len(cards) == 1:
            return number * sum(list(filter(lambda x: x != -1, [num for row in cards[ind] for num in row])))

    return 0


def update_cards(cards, current_number):
    for ind, card in enumerate(cards):
        for ind2, row in enumerate(card):
            for ind3, bingo_number in enumerate(row):
                if bingo_number == current_number:
                    cards[ind][ind2][ind3] = -1


def check_bingo(cards):
    for ind, card in enumerate(cards):
        for row in card:
            if all(elem == -1 for elem in row):
                return True, ind
        for i in range(0, 4):
            bingo = True
            for j in range(0, 4):
                if card[j][i] != -1:
                    bingo = False
            if bingo:
                return True, ind
    return False, 0


if __name__ == '__main__':
    print(part1(read_input_bingo("day04.txt")[0], read_input_bingo("day04.txt")[1]))
    print(part2(read_input_bingo("day04.txt")[0], read_input_bingo("day04.txt")[1]))
