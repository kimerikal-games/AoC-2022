"""
Advent of Code 2022 - Day 4: Camp Cleanup
Author: kimerikal <kimerikal.games@gmail.com>
"""
import re
import sys
from typing import List, Tuple

SectionPair = Tuple[int, int, int, int]


def main() -> int:
    p = re.compile(r"^(\d+)-(\d+),(\d+)-(\d+)")
    section_pairs: List[SectionPair] = [
        tuple(map(int, m.groups()))
        for line in sys.stdin
        if (m := p.match(line))
    ]

    print("Part 1:", part1(section_pairs))
    print("Part 2:", part2(section_pairs))

    return 0


def part1(section_pairs: List[SectionPair]) -> int:
    return sum(
        a <= c and b >= d or c <= a and d >= b
        for a, b, c, d in section_pairs
    )


def part2(section_pairs: List[SectionPair]) -> int:
    return sum(
        b >= c and d >= a
        for a, b, c, d in section_pairs
    )


if __name__ == "__main__":
    sys.exit(main())
