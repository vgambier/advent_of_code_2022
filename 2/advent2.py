#!/usr/bin/env python

def parse_input():
    parsed_rounds = []
    with open('input.txt', 'r') as f:
        for line in f:
            parsed_rounds.append(line.strip('\n').split())
    return parsed_rounds


if __name__ == '__main__':

    rounds = parse_input()

    scoring = {
        "A": {"X": 4, "Y": 8, "Z": 3},
        "B": {"X": 1, "Y": 5, "Z": 9},
        "C": {"X": 7, "Y": 2, "Z": 6}
    }
    true_scoring = {
        "A": {"X": 3, "Y": 4, "Z": 8},
        "B": {"X": 1, "Y": 5, "Z": 9},
        "C": {"X": 2, "Y": 6, "Z": 7}
    }

    score = 0
    true_score = 0

    for _round in rounds:
        score += scoring[_round[0]][_round[1]]
        true_score += true_scoring[_round[0]][_round[1]]

    assert score == 11906
    assert true_score == 11186

    print(f"Incorrect score is {score}")
    print(f"Correct score is {true_score}")
