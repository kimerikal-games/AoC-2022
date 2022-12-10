"""
Advent of Code 2022 - Day 10: Cathode-Ray Tube
Author: kimerikal <kimerikal.games@gmail.com>
"""
import sys

rows, cols = 6, 40


def main() -> int:
    insts = [line.split() for line in sys.stdin]

    history = preprocess(insts)
    print("Part 1:", part1(history))
    print("Part 2:", part2(history), sep="\n")

    return 0


def preprocess(insts: list[list[str]]) -> list[int]:
    register = 1
    history = [1]

    for inst in insts:
        match inst:
            case ["addx", imm]:
                history.append(register)
                history.append(register)
                register += int(imm)
            case ["noop"]:
                history.append(register)

    return history


def part1(history: list[int]) -> int:
    return sum([cycle * register for cycle, register in enumerate(history)][20::40])


def part2(history: list[int]) -> str:
    lits = [abs((cycle - 1) % cols - register) <= 1 for cycle, register in enumerate(history)]
    return "\n".join("".join("#" if cell else "." for cell in lits[cols * i + 1 : cols * (i + 1) + 1]) for i in range(rows))


if __name__ == "__main__":
    sys.exit(main())
