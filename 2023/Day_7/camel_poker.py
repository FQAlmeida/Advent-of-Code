from functools import cmp_to_key
from pathlib import Path


def get_card_strength(card: str):
    if card == "A":
        return 14
    if card == "K":
        return 13
    if card == "Q":
        return 12
    if card == "J":
        return 11
    if card == "T":
        return 10
    return int(card)


def get_hand_by_card(hand1, hand2):
    values1 = map(get_card_strength, hand1)
    values2 = map(get_card_strength, hand2)
    for card1, card2 in zip(values1, values2):
        if card1 > card2:
            return 1
        elif card2 > card1:
            return -1
    return 0


def get_hand_classification(hand: str):
    hand_uniques: dict[str, int] = dict()
    for card in hand:
        hand_uniques[card] = hand_uniques.get(card, 0) + 1
    max_rep = max(hand_uniques.values())
    qtd_unique = len(hand_uniques.keys())
    if qtd_unique == 1:
        return 7
    elif qtd_unique == 2 and max_rep == 4:
        return 6
    elif qtd_unique == 2 and max_rep == 3:
        return 5
    elif qtd_unique == 3 and max_rep == 3:
        return 4
    elif qtd_unique == 3 and max_rep == 2:
        return 3
    elif qtd_unique == 4 and max_rep == 2:
        return 2
    # elif qtd_unique == 5:
    return 1


def get_hand_value(data1: tuple[str, int], data2: tuple[str, int]):
    hand1, _ = data1
    hand2, _ = data2
    if hand1 == hand2:
        return 0
    hand1_class = get_hand_classification(hand1)
    hand2_class = get_hand_classification(hand2)
    if hand1_class != hand2_class:
        return hand1_class - hand2_class

    return get_hand_by_card(hand1, hand2)


def parse_line(line: str):
    hand, bet = line.split(" ")
    bet = int(bet)
    return (hand, bet)


if __name__ == "__main__":
    with Path("2023/Day_7/data/input.txt").open("r") as fd:
        lines = fd.readlines()
    hands = list(map(parse_line, lines))

    hands = sorted(hands, key=cmp_to_key(get_hand_value))
    sums = 0
    for i, (_, bet) in enumerate(hands, 1):
        sums += i * bet
    print(sums)
