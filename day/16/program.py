"""
Advent of Code 2022 - Day 16: Proboscidea Volcanium
Author: kimerikal <kimerikal.games@gmail.com>
"""
import re
import sys

inf = sys.maxsize

AdjList = list[list[int]]
AdjMat = list[list[int]]
State = tuple[int, ...]


def main() -> int:
    n, neighbors, flows = preprocess()

    print("Part 1:", part1(n, neighbors, flows))
    print("Part 2:", part2(n, neighbors, flows))

    return 0


def preprocess() -> tuple[int, AdjList, list[int]]:
    pattern = re.compile(r"([A-Z]{2}|\d+)")

    nodes_set: set[str] = set()
    neighbors_dict: dict[str, list[str]] = {}
    flows_dict: dict[str, int] = {}

    for line in sys.stdin:
        m = re.findall(pattern, line)

        node = m[0]
        node_neighbors = m[2:]
        flow = int(m[1])

        nodes_set.add(node)
        neighbors_dict[node] = node_neighbors
        flows_dict[node] = flow

    nodes = sorted(nodes_set)
    n = len(nodes)
    neighbors = [[nodes.index(t) for t in neighbors_dict[s]] for s in nodes]
    flows = [flows_dict[node] for node in nodes]
    return n, neighbors, flows


def part1(n: int, neighbors: AdjList, flows: list[int]) -> int:
    def traverse(node: int, path: list[int], time: int) -> int:
        if time <= 0:
            return 0

        state = (time, node, *sorted(path))

        if state in memo:
            return memo[state]

        best_flow = 0

        if node != 0 and node not in path:
            path.append(node)
            best_flow = (time - 1) * flows[node] + traverse(node, path, time - 1)
            path.pop()

        for neighbor, distance in enumerate(graph[node]):
            if neighbor != node and neighbor not in path:
                flow = traverse(neighbor, path, time - distance)
                best_flow = max(best_flow, flow)

        memo[state] = best_flow
        return best_flow

    start = 0
    graph, flows = extract_graph(n, neighbors, flows, start)
    memo: dict[State, int] = {}

    return traverse(start, [], 30)


def part2(n: int, neighbors: AdjList, flows: list[int]) -> int:
    def traverse(node: int, path: list[int], time: int, flow: int) -> None:
        if time <= 0:
            return

        state = (time, node, *sorted(path))

        if memo.get(state, -1) >= flow:
            return

        memo[state] = flow

        if node != 0 and node not in path:
            path.append(node)
            traverse(node, path, time - 1, flow + (time - 1) * flows[node])
            path.pop()

        for neighbor, distance in enumerate(graph[node]):
            if neighbor != node and neighbor not in path:
                traverse(neighbor, path, time - distance, flow)

    start = 0
    graph, flows = extract_graph(n, neighbors, flows, start)
    memo: dict[State, int] = {}

    traverse(start, [], 26, 0)

    pruned: dict[int, int] = {}
    for (_, _, *p1), f1 in memo.items():
        b1 = to_bitset(p1)
        pruned[b1] = max(pruned.get(b1, 0), f1)

    fmax = 0
    for b1, f1 in pruned.items():
        for b2, f2 in pruned.items():
            if not b1 & b2:
                fmax = max(fmax, f1 + f2)

    return fmax


def extract_graph(
    n: int, neighbors: AdjList, flows: list[int], start: int
) -> tuple[AdjMat, list[int]]:
    graph = [[inf] * n for _ in range(n)]

    for s in range(n):
        graph[s][s] = 0
        for t in neighbors[s]:
            graph[s][t] = 1

    for v in range(n):
        for s in range(n):
            for t in range(n):
                graph[s][t] = min(graph[s][t], graph[s][v] + graph[v][t])

    nodes = [u for u, flow in enumerate(flows) if u == start or flow > 0]
    graph = [[graph[s][t] for t in nodes] for s in nodes]
    flows = [flows[u] for u in nodes]

    return graph, flows


def to_bitset(path: list[int]) -> int:
    bitset = 0
    for p in path:
        bitset |= 1 << p
    return bitset


if __name__ == "__main__":
    sys.exit(main())
