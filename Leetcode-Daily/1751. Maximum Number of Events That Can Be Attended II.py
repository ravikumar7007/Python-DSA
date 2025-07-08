from typing import List
import bisect


class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        """
        Returns the maximum sum of values by attending at most k non-overlapping events.
        Each event is represented as [start, end, value].
        """
        n = len(events)
        # Sort events by start time
        events.sort()
        # Memoization table: mem[pos][k_rem] = max value from pos with k_rem events left
        mem = [[-1] * (k + 1) for _ in range(n)]

        # Precompute the next non-overlapping event for each event
        next_event = [0] * n
        for i in range(n):
            left, right = i + 1, n
            target = events[i][1] + 1
            while left < right:
                mid = (left + right) // 2
                if events[mid][0] >= target:
                    right = mid
                else:
                    left = mid + 1
            next_event[i] = left

        def attend_event(pos: int, k_rem: int) -> int:
            """
            Returns the maximum value by attending at most k_rem events starting from position pos.
            """
            if k_rem == 0 or pos >= n:
                return 0
            if mem[pos][k_rem] != -1:
                return mem[pos][k_rem]

            # Option 1: Skip current event
            skip = attend_event(pos + 1, k_rem)
            # Option 2: Attend current event and move to next non-overlapping event
            next_pos = next_event[pos]
            attend = events[pos][2] + attend_event(next_pos, k_rem - 1)

            mem[pos][k_rem] = max(skip, attend)
            return mem[pos][k_rem]

        return attend_event(0, k)


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxValue([[1, 2, 4], [3, 4, 3], [2, 3, 1]], 2))  # Expected output: 7
    print(solution.maxValue([[1, 2, 4], [3, 4, 3], [2, 3, 1]], 1))  # Expected output: 4
    print(solution.maxValue([[1, 2, 4], [3, 4, 3], [2, 3, 1]], 0))  # Expected output: 0
    print(
        solution.maxValue([[1, 10**9, 1000000000]], k=1)
    )  # Expected output: 1000000000
