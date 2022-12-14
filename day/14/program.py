"""
Advent of Code 2022 - Day 14: Regolith Reservoir
Author: kimerikal <kimerikal.games@gmail.com>
"""
import sys
from copy import deepcopy
from itertools import chain
from typing import Literal

try:
    from itertools import pairwise
except ImportError:
    from itertools import tee

    def pairwise(iterable):
        a, b = tee(iterable)
        next(b, None)
        return zip(a, b)


inf = sys.maxsize
source = (0, 500)

Coord = tuple[int, int]
Path = list[Coord]
Grid = list[list[Literal[".", "#", "o"]]]


def main() -> int:
    paths: list[Path] = []
    for line in sys.stdin:
        path: Path = []
        coords = line.split(" -> ")
        for coord in coords:
            x, y = map(int, coord.split(","))
            path.append((y, x))
        paths.append(path)

    grid, ymin, xmin = preprocess(paths)

    print("Part 1:", part1(grid, ymin, xmin))
    print("Part 2:", part2(grid, ymin, xmin))

    return 0


def preprocess(paths: list[Path]) -> tuple[Grid, int, int]:
    ymin = ymax = source[0]

    for y, x in chain.from_iterable(paths):
        ymin = min(ymin, y)
        ymax = max(ymax, y)

    rows = ymax - ymin + 1

    xmin = source[1] - rows - 10
    xmax = source[1] + rows + 10

    cols = xmax - xmin + 1

    grid = [["."] * cols for _ in range(rows)]

    for path in paths:
        for (y1, x1), (y2, x2) in pairwise(path):
            sy, ey = min(y1, y2) - ymin, max(y1, y2) - ymin
            sx, ex = min(x1, x2) - xmin, max(x1, x2) - xmin
            for y in range(sy, ey + 1):
                for x in range(sx, ex + 1):
                    grid[y][x] = "#"

    return grid, ymin, xmin


def part1(grid: Grid, ymin: int, xmin: int) -> int:
    grid = deepcopy(grid)
    sy, sx = (source[0] - ymin, source[1] - xmin)

    count = 0

    while True:
        y, x = sy, sx

        while y + 1 < len(grid):
            if grid[y + 1][x] == ".":
                y, x = y + 1, x
            elif grid[y + 1][x - 1] == ".":
                y, x = y + 1, x - 1
            elif grid[y + 1][x + 1] == ".":
                y, x = y + 1, x + 1
            else:
                grid[y][x] = "o"
                break
        else:
            break

        count += 1

    return count


def part2(grid: Grid, ymin: int, xmin: int) -> int:
    grid = deepcopy(grid)
    grid.append(["."] * len(grid[0]))
    grid.append(["#"] * len(grid[0]))

    sy, sx = (source[0] - ymin, source[1] - xmin)

    count = 0

    while grid[sy][sx] == ".":
        y, x = sy, sx

        while y + 1 < len(grid):
            if grid[y + 1][x] == ".":
                y, x = y + 1, x
            elif grid[y + 1][x - 1] == ".":
                y, x = y + 1, x - 1
            elif grid[y + 1][x + 1] == ".":
                y, x = y + 1, x + 1
            else:
                grid[y][x] = "o"
                break
        else:
            raise RuntimeError("Sand fell below the infinite horizon.")

        count += 1

    return count


if __name__ == "__main__":
    sys.exit(main())
