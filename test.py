from collections import deque
from typing import List


class Solution:
    def maxCandies(
        self,
        status: List[int],
        candies: List[int],
        keys: List[List[int]],
        containedBoxes: List[List[int]],
        initialBoxes: List[int],
    ) -> int:
        n = len(status)
        q = deque(initialBoxes)
        closed = set()
        total = 0

        while q:
            curr = q.popleft()

            if status[curr] == 0:
                closed.add(curr)
                continue

            for open in keys[curr]:
                status[open] = 1
                if open in closed:
                    q.append(open)
                    closed.remove(open)

            total += candies[curr]
            for box in containedBoxes[curr]:
                q.append(box)

        return total

if __name__ == "__main__":
    solution = Solution()
    status = [1, 0, 1]
    candies = [5, 2, 3]
    keys = [[], [0], []]
    containedBoxes = [[1], [], []]
    initialBoxes = [0]

    result = solution.maxCandies(status, candies, keys, containedBoxes, initialBoxes)
    print(result)  # Expected output: 5