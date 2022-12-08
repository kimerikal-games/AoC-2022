"""
Advent of Code 2022 - Day 7: No Space Left On Device
Author: kimerikal <kimerikal.games@gmail.com>
"""
import sys


def main() -> int:
    commands = sys.stdin.read().split('\n')

    print("Part 1:", part1(commands))
    print("Part 2:", part2(commands))

    return 0


def part1(commands: list[str]) -> int:
    for command in commands:
        print(command)


def part2(commands: list[str]) -> int:
    pass


if __name__ == "__main__":
    sys.exit(main())
