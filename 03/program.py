"""
Advent of Code 2022 - Day 3: Rucksack Reorganization
Author: kimerikal <kimerikal.games@gmail.com>
"""
import sys
from typing import List, Iterable


def main() -> int:
    lines = [line.strip() for line in sys.stdin]

    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))

    return 0


def part1(lines: List[str]) -> int:
    total_value = 0
    for line in lines:
        left = line[: len(line) // 2]
        right = line[len(line) // 2 :]
        share = (set(left) & set(right)).pop()
        value = get_value(share)
        total_value += value
    return total_value


def part2(lines: List[str]) -> int:
    total_value = 0
    for l1, l2, l3 in grouper(lines, 3):
        share = (set(l1) & set(l2) & set(l3)).pop()
        value = get_value(share)
        total_value += value
    return total_value


def get_value(share):
    if "a" <= share <= "z":
        value = ord(share) - ord("a") + 1
    else:
        value = ord(share) - ord("A") + 27
    return value


def grouper(iterable: Iterable, n: int):
    args = [iter(iterable)] * n
    return zip(*args)


if __name__ == "__main__":
    sys.exit(main())
