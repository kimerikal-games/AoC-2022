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
    __slots__ = ("items", "operation_s", "boring", "test_value", "truthy", "falsy", "cnt_inspect")

    def __init__(self, items: list[int], operation_s: str, test_value: int, truthy: int, falsy: int):
        self.items = deque(items)
        self.operation_s = operation_s
        self.boring: bool
        self.test_value = test_value
        self.truthy = truthy
        self.falsy = falsy
        self.cnt_inspect = 0

    def inspect(self):
        while self.items:
            self.cnt_inspect += 1
            item = self.items.popleft()
            item = eval(self.operation_s.replace("old", str(item)))
            if self.boring:
                item //= item
            to = self.truthy if item % self.test_value == 0 else self.falsy
            yield to, item

    def add_item(self, item: int) -> None:
        self.items.append(item)


def main() -> int:
    monkeys = preprocess()

    print("Part 1:", part1(monkeys))
    print("Part 2:", part2(monkeys))

    return 0


def preprocess() -> list[Monkey]:
    input = sys.stdin.readline

    monkeys: list[Monkey] = []
    while True:
        lines = [input() for _ in range(7)]
        if (parsed := parse_lines(lines)) is None:
            break
        starting_items, operation_s, test_value, truthy, falsy = parsed
        monkey = Monkey(starting_items, operation_s, test_value, truthy, falsy)
        monkeys.append(monkey)

    return monkeys


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


def part2(monkeys: list[Monkey]) -> int:
    return solve(monkeys, False, 10000)


def solve(monkeys: list[Monkey], boring: bool, rounds: int) -> int:
    monkeys = deepcopy(monkeys)
    mod = lcm(*(monkey.test_value for monkey in monkeys))

    for monkey in monkeys:
        monkey.boring = boring

    for _ in range(rounds):
        for monkey in monkeys:
            for to, item in monkey.inspect():
                item %= mod
                monkeys[to].add_item(item)

    counter = [monkey.cnt_inspect for monkey in monkeys]
    c1, c2 = sorted(counter)[-2:]
    monkey_business = c1 * c2

    return monkey_business


if __name__ == "__main__":
    sys.exit(main())
