"""
Advent of Code 2022 - Day 5: Supply Stacks
Author: kimerikal <kimerikal.games@gmail.com>
"""
import re
import sys
from collections import defaultdict, deque
from copy import deepcopy


def main() -> int:
    input = sys.stdin.readline
    crates = defaultdict(deque)
    while True:
        line = input().rstrip("\n")
        if "[" not in line:
            break
        for crate_id, i in enumerate(range(1, len(line), 4)):
            crate = line[i]
            if crate != " ":
                crates[crate_id + 1].appendleft(crate)
    input()

    p = re.compile(r"^move (\d+) from (\d+) to (\d+)")
    moves = []
    while True:
        line = input()
        if match := p.match(line):
            moves.append(tuple(map(int, match.groups())))
        else:
            break

    print("Part 1:", part1(crates, moves))
    print("Part 2:", part2(crates, moves))

    return 0


def part1(crates, moves) -> str:
    crates = deepcopy(crates)
    for count, from_id, to_id in moves:
        for _ in range(count):
            crates[to_id].append(crates[from_id].pop())
    tops = []
    for key in sorted(crates):
        tops.append(crates[key][-1])
    return "".join(tops)


def part2(crates, moves) -> str:
    crates = deepcopy(crates)
    temp = []
    for count, from_id, to_id in moves:
        for _ in range(count):
            temp.append(crates[from_id].pop())
        for _ in range(count):
            crates[to_id].append(temp.pop())
    tops = []
    for key in sorted(crates):
        tops.append(crates[key][-1])
    return "".join(tops)


if __name__ == "__main__":
    sys.exit(main())
