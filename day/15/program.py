"""
Advent of Code 2022 - Day 15: Beacon Exclusion Zone
Author: kimerikal <kimerikal.games@gmail.com>
"""
import re
import sys
from typing import Iterator, List, Tuple

Sensor = Tuple[int, int, int]
Interval = Tuple[int, int]


def main() -> int:
    sensors: List[Sensor] = []
    for line in sys.stdin:
        if m := re.findall(r"(-?\d+)", line):
            sx, sy, bx, by = map(int, m)
            sensors.append((sx, sy, distance(sx, sy, bx, by)))

    print("Part 1:", part1(sensors))
    print("Part 2:", part2(sensors))

    return 0


def part1(sensors: List[Sensor]) -> int:
    intervals: List[Interval] = []

    for sx, sy, size in sensors:
        dist_foot = abs(2_000_000 - sy)
        half = size - dist_foot
        if half < 0:
            continue
        intervals.append((sx - half, sx + half))

    intervals.sort()

    total = 0
    last = -sys.maxsize
    for start, end in intervals:
        if start > last:
            total += end - start
            last = end
        elif end > last:
            total += end - last
            last = end

    return total


def part2(sensors: List[Sensor]) -> int:
    for sx, sy, size in sensors:
        for x, y in edges(sx, sy, size):
            if not (0 <= x <= 4_000_000 and 0 <= y <= 4_000_000):
                continue
            for tx, ty, tsize in sensors:
                # NOTE: Inlined for performance
                # if distance(tx, ty, x, y) <= tsize:
                dx = x - tx if x > tx else tx - x
                dy = y - ty if y > ty else ty - y
                if dx + dy <= tsize:
                    break
            else:
                return frequency(x, y)

    raise ValueError("No solution found")


def distance(ax: int, ay: int, bx: int, by: int) -> int:
    return abs(bx - ax) + abs(by - ay)


def edges(sx: int, sy: int, size: int) -> Iterator[tuple[int, int]]:
    for i in range(size + 1):
        yield sx + size + 1 - i, sy + i
        yield sx - i, sy + size + 1 - i
        yield sx - size - 1 + i, sy - i
        yield sx + i, sy - size - 1 + i


def frequency(x: int, y: int) -> int:
    return x * 4_000_000 + y


if __name__ == "__main__":
    sys.exit(main())
