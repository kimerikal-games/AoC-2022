"""
Advent of Code 2022 - Day 6: Tuning Trouble
Author: kimerikal <kimerikal.games@gmail.com>
"""
import sys
from collections import deque
from typing import Deque


def main() -> int:
    stream = sys.stdin.readline().rstrip()

    print("Part 1:", part1(stream))
    print("Part 2:", part2(stream))

    return 0


def part1(stream: str) -> int:
    return solve(stream, 4)


def part2(stream: str) -> int:
    return solve(stream, 14)


def solve(stream: str, k: int) -> int:
    buffer: Deque[str] = deque(maxlen=k)
    for i, c in enumerate(stream):
        buffer.append(c)
        if len(set(buffer)) == k:
            return i + 1
    return -1


if __name__ == "__main__":
    sys.exit(main())
