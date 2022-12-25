"""
Advent of Code 2022 - Day 21: Monkey Math
Author: kimerikal <kimerikal.games@gmail.com>
"""
import sys
from typing import Callable, Dict, Literal, NewType, Tuple, Union

Name = NewType("Name", str)
Value = int
OpStr = Literal["+", "-", "*", "/"]
Expr = Union[Value, Tuple[Name, OpStr, Name]]

root = Name("root")
human = Name("humn")

Op = Callable[[Value, Value], Value]
op_map: Dict[OpStr, Op] = {
    "+": lambda left, right: left + right,
    "-": lambda left, right: left - right,
    "*": lambda left, right: left * right,
    "/": lambda left, right: left // right,
}
op_left_map: Dict[OpStr, Op] = {
    "+": lambda result, right: result - right,
    "-": lambda result, right: result + right,
    "*": lambda result, right: result // right,
    "/": lambda result, right: result * right,
}
op_right_map: Dict[OpStr, Op] = {
    "+": lambda result, left: result - left,
    "-": lambda result, left: left - result,
    "*": lambda result, left: result // left,
    "/": lambda result, left: left // result,
}


def main() -> None:
    monkeys: Dict[Name, Expr] = {}
    for line in sys.stdin:
        name, expr = line.strip().split(": ")
        if expr.isnumeric():
            monkeys[Name(name)] = Value(expr)
        else:
            monkeys[Name(name)] = tuple(expr.split(" "))  # type: ignore[assignment]

    print("Part 1:", part1(monkeys))
    print("Part 2:", part2(monkeys))


def part1(monkeys: Dict[Name, Expr]) -> int:
    return evaluate(monkeys, root)


def part2(monkeys: Dict[Name, Expr]) -> int:
    parents: Dict[Name, Name] = {}
    for name, expr in monkeys.items():
        if isinstance(expr, tuple):
            left, _, right = expr
            parents[left] = name
            parents[right] = name

    return request(monkeys, parents, human)


def evaluate(monkeys: Dict[Name, Expr], name: Name) -> Value:
    expr = monkeys[name]
    if isinstance(expr, Value):
        return expr
    else:
        left, op, right = expr
        return op_map[op](evaluate(monkeys, left), evaluate(monkeys, right))


def request(monkeys: Dict[Name, Expr], parents: Dict[Name, Name], name: Name) -> Value:
    parent = parents[name]
    expr = monkeys[parent]
    assert not isinstance(expr, Value)
    left, op, right = expr

    other = left if name == right else right
    value = evaluate(monkeys, other)
    if parent != root:
        op_reverse_map = op_left_map if name == left else op_right_map
        value = op_reverse_map[op](request(monkeys, parents, parent), value)

    return value


if __name__ == "__main__":
    sys.exit(main())  # type: ignore[func-returns-value]
