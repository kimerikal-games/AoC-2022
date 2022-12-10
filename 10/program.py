"""
Advent of Code 2022 - Day 10: Cathode-Ray Tube
Author: kimerikal <kimerikal.games@gmail.com>
"""
import sys

Instruction = list[str]


def main() -> int:
    insts = [line.split() for line in sys.stdin]

    print("Part 1:", part1(insts))
    print("Part 2:")
    part2(insts)

    return 0


def part1(insts: list[Instruction]) -> int:
    cycle = 0
    register = 1
    history = [1]

    for inst in insts:
        match inst:
            case ["addx", x]:
                value = int(x)
                cycle += 1
                history.append(cycle * register)
                cycle += 1
                history.append(cycle * register)
                register += value
            case ["noop"]:
                cycle += 1
                history.append(cycle * register)
            case _:
                raise ValueError(f"Invalid instruction {inst}")

    return sum(history[20::40])


def part2(insts: list[Instruction]) -> None:
    rows = 6
    cols = 40
    crt = [False] * (rows * cols)

    cycle = 0
    register = 1
    plot(cols, crt, cycle, register)

    for inst in insts:
        match inst:
            case ["addx", x]:
                value = int(x)
                cycle += 1
                plot(cols, crt, cycle, register)
                cycle += 1
                plot(cols, crt, cycle, register)
                register += value
            case ["noop"]:
                cycle += 1
                plot(cols, crt, cycle, register)
            case _:
                raise ValueError(f"Invalid instruction {inst}")

    for row in range(rows):
        for col in range(cols):
            print(".#"[crt[row * cols + col]], end="")
        print()


def plot(cols: int, crt: list[bool], cycle: int, register: int):
    if register - 1 <= (cycle - 1) % cols <= register + 1:
        crt[cycle - 1] = True


if __name__ == "__main__":
    sys.exit(main())
