from typing import List


class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        """
        Calculates the maximum number of subarrays after removing one conflicting pair.
        """
        m = len(conflictingPairs)
        self._normalize_pairs(conflictingPairs)
        conflictingPairs.sort(key=lambda x: x[1])

        blocked = 0
        max_profit = 0
        profit = 0
        max_first = 0
        max_second = 0

        for i in range(m):
            start = conflictingPairs[i][0]
            bottom = conflictingPairs[i + 1][1] if i < m - 1 else n + 1
            gap = bottom - conflictingPairs[i][1]

            if start > max_first:
                max_second = max_first
                max_first = start
                profit = 0
            elif start > max_second:
                max_second = start

            profit += gap * (max_first - max_second)
            if profit > max_profit:
                max_profit = profit
            blocked += max_first * gap

        total_subarrays = n * (n + 1) // 2
        return total_subarrays - blocked + max_profit

    def _normalize_pairs(self, pairs: List[List[int]]) -> None:
        """
        Ensures each pair is in ascending order.
        """
        for pair in pairs:
            if pair[0] > pair[1]:
                pair[0], pair[1] = pair[1], pair[0]


if __name__ == "__main__":
    n = 5
    conflictingPairs = [[1, 2], [2, 5], [3, 5]]
    solution = Solution()
    print(
        solution.maxSubarrays(n, conflictingPairs)
    )  # Output: expected maximum subarrays count
