"""
Advent of Code 2022 - Day 8: Treetop Tree House
Author: kimerikal <kimerikal.games@gmail.com>
"""
import sys
from itertools import chain
from math import prod

Grid = list[list[int]]


def main() -> int:
    grid: Grid = [list(map(int, line.rstrip())) for line in sys.stdin]
    rows, cols = len(grid), len(grid[0])

    print("Part 1:", part1(rows, cols, grid))
    print("Part 2:", part2(rows, cols, grid))

    return 0


def part1(rows: int, cols: int, grid: Grid) -> int:
    visible = [[False] * cols for _ in range(rows)]

    # From left
    for row in range(rows):
        h = -1
        for col in range(cols):
            if grid[row][col] > h:
                h = grid[row][col]
                visible[row][col] = True

    # From right
    for row in range(rows):
        h = -1
        for col in range(cols - 1, -1, -1):
            if grid[row][col] > h:
                h = grid[row][col]
                visible[row][col] = True

    # From top
    for col in range(cols):
        h = -1
        for row in range(rows):
            if grid[row][col] > h:
                h = grid[row][col]
                visible[row][col] = True

    # From bottom
    for col in range(cols):
        h = -1
        for row in range(rows - 1, -1, -1):
            if grid[row][col] > h:
                h = grid[row][col]
                visible[row][col] = True

    return sum(chain.from_iterable(visible))


def part2(rows: int, cols: int, grid: Grid) -> int:
    max_score = 0

    for row in range(rows):
        for col in range(cols):
            h = grid[row][col]
            views = [0, 0, 0, 0]

            # To top
            for r in range(row - 1, -1, -1):
                views[0] += 1
                if grid[r][col] >= h:
                    break

            # To bottom
            for r in range(row + 1, rows):
                views[1] += 1
                if grid[r][col] >= h:
                    break

            # To left
            for c in range(col - 1, -1, -1):
                views[2] += 1
                if grid[row][c] >= h:
                    break

            # To right
            for c in range(col + 1, cols):
                views[3] += 1
                if grid[row][c] >= h:
                    break

            score = prod(views)
            if score > max_score:
                max_score = score

    return max_score


if __name__ == "__main__":
    sys.exit(main())
