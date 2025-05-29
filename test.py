from collections import deque
from typing import List


class Solution:
    def bfs(
        self, node: int, graph: List[List[int]], mark_even: List[bool] = None
    ) -> int:
        q = deque([(node, -1)])
        count = 0
        level = 0

        while q:
            if level % 2 == 0:
                count += len(q)
                if mark_even is not None:
                    for current, _ in q:
                        mark_even[current] = True
            for _ in range(len(q)):
                current, parent = q.popleft()
                for neighbor in graph[current]:
                    if neighbor != parent:
                        q.append((neighbor, current))
            level += 1
        return count

    def build_graph(self, edges: List[List[int]], n: int) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        return graph

    def maxTargetNodes(
        self, edges1: List[List[int]], edges2: List[List[int]]
    ) -> List[int]:
        m = len(edges1) + 1
        n = len(edges2) + 1

        graph1 = self.build_graph(edges1, m)
        graph2 = self.build_graph(edges2, n)

        # Calculate best1 in one pass
        even_count1 = self.bfs(0, graph2)
        best1 = max(even_count1, n - even_count1)

        included = [False] * m
        even_count2 = self.bfs(0, graph1, included)
        odd_count2 = m - even_count2

        # Use list comprehension for result
        return [
            even_count2 + best1 if included[i] else odd_count2 + best1 for i in range(m)
        ]


if __name__ == "__main__":
    edges1 = [[0, 1], [0, 2], [0, 3], [0, 4]]
    edges2 = [[0, 1], [1, 2], [2, 3]]
    solution = Solution()
    print(solution.maxTargetNodes(edges1, edges2))  # Example usage
