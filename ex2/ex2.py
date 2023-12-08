import sys
from collections import defaultdict
from pprint import pprint


Nodes = defaultdict[str, list[str]]


def is_valid(nodes: Nodes, key: str) -> int:
    values = nodes.get(key)
    if values is None:
        return 0
    if len(values) == 1:
        return 0
    return len(nodes.get(values[0], [])) == len(nodes) - 1


def main():
    nodes: Nodes = defaultdict(list[str])
    _ = sys.stdin.readline()
    for line in sys.stdin.readlines():
        name, dir = line.split(" ")
        nodes[name].append(dir.strip())
    pprint(nodes)
    keys = list(nodes.keys())
    keys.sort(key=lambda key: is_valid(nodes, key))
    print(keys[-1])


if __name__ == "__main__":
    main()
