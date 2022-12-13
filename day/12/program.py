"""
Advent of Code 2022 - Day 12: Hill Climbing Algorithm
Author: kimerikal <kimerikal.games@gmail.com>
"""
import sys
from collections import deque

inf = sys.maxsize
deltas = [(-1, 0), (0, -1), (0, 1), (1, 0)]


def main() -> int:
    grid = [list(map(ord, line.strip())) for line in sys.stdin]
    rows, cols = len(grid), len(grid[0])

    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == ord("S"):
                sy, sx = i, j
                grid[i][j] = ord("a")
            elif cell == ord("E"):
                ey, ex = i, j
                grid[i][j] = ord("z")

    print("Part 1:", part1(rows, cols, grid, sy, sx, ey, ex))
    print("Part 2:", part2(rows, cols, grid, sy, sx, ey, ex))


def part1(rows: int, cols: int, grid: list[list[int]], sy: int, sx: int, ey: int, ex: int) -> int:
    jobs = deque([(0, sy, sx)])
    distance = [[inf] * cols for _ in range(rows)]
    distance[sy][sx] = 0
    while jobs:
        d, y, x = jobs.popleft()
        nd = d + 1
        for dy, dx in deltas:
            if 0 <= (ny := y + dy) < rows and 0 <= (nx := x + dx) < cols:
                if grid[ny][nx] <= grid[y][x] + 1 and distance[ny][nx] > nd:
                    distance[ny][nx] = nd
                    jobs.append((nd, ny, nx))
                    if ny == ey and nx == ex:
                        return nd


def part2(rows: int, cols: int, grid: list[list[int]], sy: int, sx: int, ey: int, ex: int) -> int:
    jobs = deque([(0, ey, ex)])
    distance = [[inf] * cols for _ in range(rows)]
    distance[ey][ex] = 0
    while jobs:
        d, y, x = jobs.popleft()
        nd = d + 1
        for dy, dx in deltas:
            if 0 <= (ny := y - dy) < rows and 0 <= (nx := x - dx) < cols:
                if grid[ny][nx] >= grid[y][x] - 1 and distance[ny][nx] > nd:
                    distance[ny][nx] = nd
                    jobs.append((nd, ny, nx))
                    if grid[ny][nx] == ord("a"):
                        return nd


if __name__ == "__main__":
    sys.exit(main())
