"""
Advent of Code 2022 - Day 13: Distress Signal
Author: kimerikal <kimerikal.games@gmail.com>
"""
import sys
from functools import cmp_to_key
from itertools import zip_longest
from typing import Literal


def main() -> int:
    input = sys.stdin.readline

    pairs = []

    while True:
        left = input().strip()
        right = input().strip()
        input()
        if not left:
            break

        pair = (eval(left), eval(right))
        pairs.append(pair)

    print("Part 1:", part1(pairs))
    print("Part 2:", part2(pairs))

    return 0


def part1(pairs: list) -> int:
    result = 0

    for index, (left, right) in enumerate(pairs, start=1):
        if compare(left, right) < 0:
            result += index

    return result


def part2(pairs: list) -> int:
    packets = []

    for left, right in pairs:
        packets.append(left)
        packets.append(right)

    packets.append(divider1 := [[2]])
    packets.append(divider2 := [[6]])

    packets.sort(key=cmp_to_key(compare))

    index1 = packets.index(divider1) + 1
    index2 = packets.index(divider2) + 1

    signal = index1 * index2
    return signal


def compare(left: int | list, right: int | list) -> Literal[-1, 0, 1]:
    if isinstance(left, int) and isinstance(right, int):
        return (left > right) - (left < right)

    if isinstance(left, int):
        left = [left]
    if isinstance(right, int):
        right = [right]

    for l, r in zip_longest(left, right):
        if l is None:
            return -1
        elif r is None:
            return 1
        elif (v := compare(l, r)) != 0:
            return v
    return 0


if __name__ == "__main__":
    sys.exit(main())
