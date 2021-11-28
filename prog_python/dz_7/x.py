
from typing import Dict


def get_depth(elem: str, tree: Dict):
    depth = 0
    while elem in tree:
        depth += 1
        elem = tree[elem]
    return depth


def main():
    tree = {}
    all_elements = set()
    for _ in range(int(input()) - 1):
        child, parent = input().strip().split()
        tree[child] = parent
        all_elements.add(child)
        all_elements.add(parent)
    for elem in sorted(list(all_elements)):
        print(elem, get_depth(elem, tree))


if __name__ == "__main__":
    main()
