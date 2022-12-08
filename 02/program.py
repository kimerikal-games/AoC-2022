"""
Advent of Code 2022 - Day 2: Rock Paper Scissors
Author: kimerikal <kimerikal.games@gmail.com>
"""
import sys
from typing import List, Tuple


def main() -> int:
    matches = [tuple(line.split()) for line in sys.stdin]

    print("Part 1:", part1(matches))
    print("Part 2:", part2(matches))

    return 0


def part1(matches: List[Tuple[str, str]]) -> int:
    score = 0

    for match in matches:
        if match in [("A", "Y"), ("B", "Z"), ("C", "X")]:
            score += 6
        elif match in [("A", "Z"), ("B", "X"), ("C", "Y")]:
            score += 0
        else:
            score += 3

        player = match[1]
        if player == "X":
            score += 1
        elif player == "Y":
            score += 2
        else:
            score += 3

    return score


def part2(matches: List[Tuple[str, str]]) -> int:
    score = 0

    for opponent, result in matches:
        if result == "X":
            score += 0
            if opponent == "A":
                player = "Z"
            elif opponent == "B":
                player = "X"
            else:
                player = "Y"
        elif result == "Y":
            score += 3
            if opponent == "A":
                player = "X"
            elif opponent == "B":
                player = "Y"
            else:
                player = "Z"
        else:
            score += 6
            if opponent == "A":
                player = "Y"
            elif opponent == "B":
                player = "Z"
            else:
                player = "X"
        if player == "X":
            score += 1
        elif player == "Y":
            score += 2
        else:
            score += 3

    return score


if __name__ == "__main__":
    sys.exit(main())
