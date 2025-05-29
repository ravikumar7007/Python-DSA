from collections import deque
from threading import stack_size
from typing import List


class Solution:
    def bfs(self, node: int, graph: List[List[int]], k: int) -> int:
        q = deque()
        q.append((node, -1))
        count = 0

        while q and k >= 0:
            size = len(q)
            count += size
            for _ in range(size):
                current, parent = q.popleft()
                for neighbor in graph[current]:
                    if neighbor != parent:
                        q.append((neighbor, current))

            k -= 1
        return count

    def build_graph(self, edges: List[List[int]], n: int) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        return graph

    def maxTargetNodes(
        self, edges1: List[List[int]], edges2: List[List[int]], k: int
    ) -> List[int]:
        m = len(edges1) + 1
        n = len(edges2) + 1

        graph1 = self.build_graph(edges1, m)
        graph2 = self.build_graph(edges2, n)

        # Precompute all bfs results for graph2 to avoid repeated work
        bfs_graph2 = [self.bfs(i, graph2, k - 1) for i in range(n)]
        best = max(bfs_graph2)

        # Precompute all bfs results for graph1
        bfs_graph1 = [self.bfs(i, graph1, k) for i in range(m)]

        # Combine results
        return [x + best for x in bfs_graph1]


if __name__ == "__main__":
    edges1 = [[0, 1]]
    edges2 = [[0, 1]]
    k = 0
    solution = Solution()
    print(solution.maxTargetNodes(edges1, edges2, k))  # Example usage
