#!/usr/bin/env python

def parse_input():
    items = []
    with open('input.txt', 'r') as f:
        for line in f:
            items.append(line.strip('\n'))
    return items


if __name__ == '__main__':

    rucksacks = parse_input()

    # Part 1

    sum_priorities = 0
    for rucksack in rucksacks:

        compartment_size = len(rucksack) // 2

        for item in rucksack[:compartment_size]:  # first compartment
            if item in rucksack[compartment_size:]:  # second compartment
                break

        item_priority = ord(item) - ord('a') + 1 if ord(item) >= ord('a') else ord(item) - ord('A') + 1 + 26
        sum_priorities += item_priority

    assert sum_priorities == 8153
    print(f"Sum of priorities: {sum_priorities}")

    # Part 2

    sum_badge_priorities = 0
    i = 0
    while i < len(rucksacks):

        current_group = rucksacks[i:i + 3]

        for item in rucksacks[i]:
            if item in rucksacks[i + 1] and item in rucksacks[i + 2]:
                break

        badge_priority = ord(item) - ord('a') + 1 if ord(item) >= ord('a') else ord(item) - ord('A') + 1 + 26
        sum_badge_priorities += badge_priority
        i += 3

    assert sum_badge_priorities == 2342
    print(f"Sum of badge priorities: {sum_badge_priorities}")
