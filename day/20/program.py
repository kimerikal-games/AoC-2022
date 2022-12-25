"""
Advent of Code 2022 - Day 20: Grove Positioning System
Author: kimerikal <kimerikal.games@gmail.com>
"""
import sys
from typing import Callable, List, TypeVar

T = TypeVar("T")


def main() -> None:
    arr = list(map(int, sys.stdin))

    print("Part 1:", part1(arr))
    print("Part 2:", part2(arr))


def part1(arr: List[int]) -> int:
    return solve(arr, lambda a: a, 1)


def part2(arr: List[int]) -> int:
    return solve(arr, lambda a: a * 811589153, 10)


def solve(arr: List[int], key_fn: Callable[[int], int], iterations: int) -> int:
    indexed = [(key_fn(a), i) for i, a in enumerate(arr)]
    mixed = indexed.copy()

    for _ in range(iterations):
        for pair in indexed:
            mix(mixed, pair, pair[0])

    return grove([a for a, _ in mixed])


def mix(arr: List[T], item: T, offset: int) -> None:
    i = arr.index(item)
    arr.insert((i + offset) % (len(arr) - 1), arr.pop(i))


def grove(arr: List[int]) -> int:
    i = arr.index(0)
    return sum(arr[(i + offset) % len(arr)] for offset in [1000, 2000, 3000])


if __name__ == "__main__":
    sys.exit(main())  # type: ignore[func-returns-value]
