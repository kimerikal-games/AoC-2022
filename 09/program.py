"""
Advent of Code 2022 - Day 9: Rope Bridge
Author: kimerikal <kimerikal.games@gmail.com>
"""
import sys

Point = tuple[int, int]


def main() -> int:
    moves: list[tuple[str, int]] = []
    for line in sys.stdin:
        direction, amount = line.split()
        moves.append((direction, int(amount)))

    print("Part 1:", part1(moves))
    print("Part 2:", part2(moves))

    return 0


def part1(moves: list[tuple[str, int]]) -> int:
    head = (0, 0)
    tail = (0, 0)
    visited: set[Point] = set()
    visited.add(tail)

    for direction, amount in moves:
        for _ in range(amount):
            head = move(head, direction)
            tail = follow(head, tail)
            visited.add(tail)

    return len(visited)


def part2(moves: list[tuple[str, int]]) -> int:
    points: list[Point] = [(0, 0)] * 10
    visited: set[Point] = set()
    visited.add((0, 0))

    for direction, amount in moves:
        for _ in range(amount):
            points[0] = move(points[0], direction)
            for i in range(1, len(points)):
                points[i] = follow(points[i - 1], points[i])
            visited.add(points[-1])

    return len(visited)


def move(point: Point, direction: str) -> Point:
    deltas = {"U": (1, 0), "D": (-1, 0), "L": (0, -1), "R": (0, 1)}
    dy, dx = deltas[direction]
    y, x = point
    return (y + dy, x + dx)


def follow(head: Point, tail: Point) -> Point:
    hy, hx = head
    ty, tx = tail
    dy = hy - ty
    dx = hx - tx
    if max(abs(dy), abs(dx)) >= 2:
        tx -= (dx < 0) - (dx > 0)
        ty -= (dy < 0) - (dy > 0)
    return (ty, tx)


if __name__ == "__main__":
    sys.exit(main())
