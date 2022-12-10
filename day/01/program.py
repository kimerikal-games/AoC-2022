"""
Advent of Code 2022 - Day 1: Calorie Counting
Author: kimerikal <kimerikal.games@gmail.com>
"""
import sys
from typing import List


def main() -> int:
    raw_packs = sys.stdin.read().split("\n\n")
    packs = [list(map(int, pack.split())) for pack in raw_packs]

    print("Part 1:", part1(packs))
    print("Part 2:", part2(packs))

    return 0


def part1(packs: List[List[int]]) -> int:
    return max(map(sum, packs))


def part2(packs: List[List[int]]):
    return sum(sorted(map(sum, packs))[-3:])


if __name__ == "__main__":
    sys.exit(main())
