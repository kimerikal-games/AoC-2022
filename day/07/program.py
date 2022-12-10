"""
Advent of Code 2022 - Day 7: No Space Left On Device
Author: kimerikal <kimerikal.games@gmail.com>
"""
import sys
from collections import defaultdict


def main() -> int:
    commands = sys.stdin.read().split("\n")

    print("Part 1:", part1(commands))
    print("Part 2:", part2(commands))

    return 0


def part1(commands: list[str]) -> int:
    dirsizes = solve(commands)
    return sum(x for x in dirsizes.values() if x <= 100000)


def part2(commands: list[str]) -> int:
    dirsizes = solve(commands)
    total_size = dirsizes[""]
    needed_size = 30000000 - (70000000 - total_size)
    return min(x for x in dirsizes.values() if x >= needed_size)


def solve(commands: list[str]) -> dict[str, int]:
    command_no = 0
    wd: list[str] = []
    dirsizes: defaultdict[str, int] = defaultdict(int)

    while command_no < len(commands):
        command = commands[command_no]

        match command.split():
            case ["$", "cd", "/"]:
                wd.clear()
                wd.append("")
            case ["$", "cd", ".."]:
                wd.pop()
            case ["$", "cd", dirname]:
                wd.append(wd[-1] + "/" + dirname)
            case ["$", "ls"]:
                j = command_no
                total_size = 0
                while j + 1 < len(commands) and not commands[j + 1].startswith("$"):
                    j += 1
                    match commands[j].split():
                        case ["dir", dirname]:
                            pass
                        case [size_raw, _]:
                            total_size += int(size_raw)
                for d in wd:
                    dirsizes[d] += total_size
                command_no = j

        command_no += 1
    return dirsizes


if __name__ == "__main__":
    sys.exit(main())
