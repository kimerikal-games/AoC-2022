"""
Advent of Code 2022 - Day 18: Boiling Boulders
Author: kimerikal <kimerikal.games@gmail.com>
"""
import sys
from typing import List, Set, Tuple

Cube = Tuple[int, int, int]


def main():
    cubes: List[Cube] = [tuple(map(int, line.split(","))) for line in sys.stdin]  # type: ignore

    print("Part 1:", part1(cubes))
    print("Part 2:", part2(cubes))


def part1(cubes: List[Cube]) -> int:
    cube_set = set(cubes)

    exposed = 0
    for cube in cube_set:
        for neighbor in neighbors(cube):
            if neighbor not in cube_set:
                exposed += 1

    return exposed


def part2(cubes: List[Cube]) -> int:
    cube_set = set(cubes)
    visited: Set[Cube] = set()

    exposed = 0
    jobs: List[Cube] = [(0, 0, 0)]
    while jobs:
        cube = jobs.pop()
        if cube in visited:
            continue
        visited.add(cube)

        for neighbor in neighbors(cube):
            x, y, z = neighbor
            if not (-1 <= x <= 21 and -1 <= y <= 21 and -1 <= z <= 21):
                continue
            if neighbor in cube_set:
                exposed += 1
            else:
                jobs.append(neighbor)

    return exposed


def neighbors(cube: Cube) -> List[Cube]:
    x, y, z = cube
    return [
        (x - 1, y, z),
        (x + 1, y, z),
        (x, y - 1, z),
        (x, y + 1, z),
        (x, y, z - 1),
        (x, y, z + 1),
    ]


if __name__ == "__main__":
    sys.exit(main())
