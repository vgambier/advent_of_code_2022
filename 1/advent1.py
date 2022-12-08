#!/usr/bin/env python

def parse_input():
    calories = [0]
    i = 0
    with open('input.txt', 'r') as f:
        for line in f:
            if line != '\n':
                calories[i] += int(line.strip('\n'))
            else:
                i += 1
                calories.append(0)
    return calories

if __name__ == '__main__':
    # Part 1
    calories = parse_input()
    print(f"Maximum colories is {max(calories)}")
    # Part 2
    calories.sort(reverse=True)
    top3 = calories[0] + calories[1] + calories[2]
    print(f"Top 3 elves carry {top3}")