"""
Advent of Code 2022 - Day 11: Monkey In The Middle
Author: kimerikal <kimerikal.games@gmail.com>
"""
import re
import sys
from collections import deque
from copy import deepcopy
from math import lcm
from typing import Optional


class Monkey:
    __slots__ = ("items", "_operation_s", "boring", "_test_value", "_truthy", "_falsy", "_cnt_inspect")

    def __init__(self, items: list[int], operation_s: str, test_value: int, truthy: int, falsy: int):
        self.items = deque(items)
        self._operation_s = operation_s
        self.boring: bool
        self._test_value = test_value
        self._truthy = truthy
        self._falsy = falsy
        self._cnt_inspect = 0

    def inspect(self):
        while self.items:
            yield from self._inspect_item(self.items.popleft())

    def _inspect_item(self, item: int):
        self._cnt_inspect += 1
        item = eval(self._operation_s.replace("old", str(item)))
        if self.boring:
            item //= item
        to = self._truthy if item % self._test_value == 0 else self._falsy
        yield to, item

    def add_item(self, item: int) -> None:
        self.items.append(item)

    def count_inspect(self) -> int:
        return self._cnt_inspect


def main() -> int:
    mod, monkeys = preprocess()

    print("Part 1:", part1(monkeys))
    print("Part 2:", part2(monkeys, mod))

    return 0


def preprocess() -> tuple[int, list[Monkey]]:
    input = sys.stdin.readline

    mod = 1
    monkeys: list[Monkey] = []
    while True:
        lines = [input() for _ in range(7)]
        if (parsed := parse_lines(lines)) is None:
            break
        starting_items, operation_s, test_value, truthy, falsy = parsed
        monkey = Monkey(starting_items, operation_s, test_value, truthy, falsy)
        mod = lcm(mod, test_value)
        monkeys.append(monkey)

    return mod, monkeys


def parse_lines(lines: list[str]) -> Optional[tuple[list[int], str, int, int, int]]:
    if not lines[0]:
        return None

    starting_items = [int(item) for item in re.findall(r"(\d+)", lines[1])]
    operation_s: str = re.match(r".*? new = (.*?)\s*$", lines[2]).group(1)
    test_value = int(re.match(r".*?(\d+)", lines[3]).group(1))
    truthy = int(re.match(r".*?(\d+)", lines[4]).group(1))
    falsy = int(re.match(r".*?(\d+)", lines[5]).group(1))

    return starting_items, operation_s, test_value, truthy, falsy


def part1(monkeys: list[Monkey]) -> int:
    return solve(monkeys, True, 20)


def part2(monkeys: list[Monkey], mod: int) -> int:
    return solve(monkeys, False, 10000, mod)


def solve(monkeys: list[Monkey], boring: bool, rounds: int, mod: Optional[int] = None) -> int:
    monkeys = deepcopy(monkeys)

    for monkey in monkeys:
        monkey.boring = boring

    for _ in range(rounds):
        for monkey in monkeys:
            for to, item in monkey.inspect():
                if mod is not None:
                    item %= mod
                monkeys[to].add_item(item)

    counter = [monkey.count_inspect() for monkey in monkeys]
    c1, c2 = sorted(counter)[-2:]
    monkey_business = c1 * c2

    return monkey_business


if __name__ == "__main__":
    sys.exit(main())
