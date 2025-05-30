from collections import deque
from typing import List


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def get_distances(start: int) -> List[int]:
            dist = [-1] * len(edges)
            curr, d = start, 0
            while curr != -1 and dist[curr] == -1:
                dist[curr] = d
                curr = edges[curr]
                d += 1
            return dist

        dist1 = get_distances(node1)
        dist2 = get_distances(node2)

        min_dist = float("inf")
        result = -1
        for i, (d1, d2) in enumerate(zip(dist1, dist2)):
            if d1 != -1 and d2 != -1:
                max_d = max(d1, d2)
                if max_d < min_dist:
                    min_dist = max_d
                    result = i
        return result


if __name__ == "__main__":
    edges = [2, 2, 3, -1]
    node1 = 0
    node2 = 1
    solution = Solution()
    print(solution.closestMeetingNode(edges, node1, node2))  # Output: 2
