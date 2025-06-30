from collections import deque


def height_of_tree(n: int, tree: list[int]) -> int:
    if n == 0:
        return 0

    # Build the adjacency list (children for each node)
    children = [[] for _ in range(n)]
    root = -1
    for child_index, parent_index in enumerate(tree):
        if parent_index == -1:
            root = child_index
        else:
            children[parent_index].append(child_index)

    # BFS to compute height
    max_height = 0
    queue = deque([(root, 1)])  # (node, current_height)
    while queue:
        node, height = queue.popleft()
        max_height = max(max_height, height)
        for child in children[node]:
            queue.append((child, height + 1))
    return max_height


if __name__ == "__main__":
    n = int(input())
    tree = list(map(int, input().split()))
    result = height_of_tree(n, tree)
    print(result)  # Expected output: 4
