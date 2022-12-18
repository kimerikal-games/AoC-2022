"""
Advent of Code 2022 - Day 17: Pyroclastic Flow
Author: kimerikal <kimerikal.games@gmail.com>
"""
import sys
from typing import List

Stack = List[List[bool]]
Rock = List[List[bool]]

R, _ = True, False
rocks = [
    [[R, R, R, R]],
    [[_, R, _], [R, R, R], [_, R, _]],
    [[_, _, R], [_, _, R], [R, R, R]],
    [[R], [R], [R], [R]],
    [[R, R], [R, R]],
]
del R, _


def main() -> None:
    jets = sys.stdin.read().strip()
    dxs = [1 if jet == ">" else -1 for jet in jets]

    print("Part 1:", part1(dxs))
    print("Part 2:", part2(dxs))


def part1(dxs: List[int]) -> int:
    stack_height = 5000
    stack_width = 7
    init_y_offset = 3
    init_x_offset = 2

    stack = [[False] * stack_width for _ in range(stack_height)]
    top_y = -1

    rock_i = 0
    dx_i = 0

    for _ in range(2022):
        rock = rocks[rock_i]
        rock_i = (rock_i + 1) % len(rocks)
        rock_height = len(rock)

        y = top_y + rock_height + init_y_offset
        x = init_x_offset

        while True:
            dx = dxs[dx_i]
            dx_i = (dx_i + 1) % len(dxs)
            if check(stack, rock, y, x + dx):
                x += dx
            if check(stack, rock, y - 1, x):
                y -= 1
            else:
                break

        top_y = max(top_y, y)
        commit(stack, rock, y, x)

    return top_y + 1  # to 1-indexed


def part2(dxs: List[int]) -> int:
    stack_height = 5000
    stack_width = 7
    init_y_offset = 3
    init_x_offset = 2

    stack = [[False] * stack_width for _ in range(stack_height)]
    top_ys: List[int] = []
    top_y = -1

    rock_i = 0
    dx_i = 0

    while True:
        rock = rocks[rock_i]
        rock_i = (rock_i + 1) % len(rocks)
        rock_height = len(rock)

        y = top_y + rock_height + init_y_offset
        x = init_x_offset

        if y > stack_height:
            break

        while True:
            dx = dxs[dx_i]
            dx_i = (dx_i + 1) % len(dxs)
            if check(stack, rock, y, x + dx):
                x += dx
            if check(stack, rock, y - 1, x):
                y -= 1
            else:
                break

        top_y = max(top_y, y)
        top_ys.append(top_y)
        commit(stack, rock, y, x)

    total_length = 1000000000000
    delta_ys = [top_ys[i] - top_ys[i - 1] for i in range(1, len(top_ys))]
    # HACK: Find the cycle from converted string. Works since each delta_y < 4.
    s = "".join(map(str, delta_ys))
    cycle_end = len(s) // 5 * 4
    cycle_start = s.index(s[cycle_end:])

    cycle_length = cycle_end - cycle_start
    cycle_count = (total_length - cycle_start) // cycle_length
    tail_length = (total_length - cycle_start) % cycle_length

    head = sum(delta_ys[:cycle_start])
    cycle = sum(delta_ys[cycle_start : cycle_start + cycle_length])
    tail = sum(delta_ys[cycle_start : cycle_start + tail_length])

    return head + cycle_count * cycle + tail


def check(stack: Stack, rock: Rock, y: int, x: int) -> bool:
    stack_height = len(stack)
    stack_width = len(stack[0])
    rock_height = len(rock)
    rock_width = len(rock[0])

    for dy in range(rock_height):
        for dx in range(rock_width):
            if rock[dy][dx]:
                if not (0 <= y - dy < stack_height and 0 <= x + dx < stack_width):
                    return False
                if stack[y - dy][x + dx]:
                    return False

    return True


def commit(stack: Stack, rock: Rock, y: int, x: int) -> None:
    rock_height = len(rock)
    rock_width = len(rock[0])

    for dy in range(rock_height):
        for dx in range(rock_width):
            if rock[dy][dx]:
                stack[y - dy][x + dx] = True


if __name__ == "__main__":
    sys.exit(main())  # type: ignore[func-returns-value]
