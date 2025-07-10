from collections import deque
from typing import List


class Solution:
    def maxFreeTime(
        self, eventTime: int, k: int, startTime: List[int], endTime: List[int]
    ) -> int:
        """
        Returns the maximum total free time available after scheduling k meetings.
        Each meeting is represented by its start and end times.
        """
        # Add a dummy meeting at eventTime if needed
        if eventTime > endTime[-1]:
            startTime.append(eventTime)
            endTime.append(eventTime)

        n = len(startTime)
        last_end = 0
        max_free_time = 0
        current_window_sum = 0
        window = deque()

        for pos in range(n):
            free_time = startTime[pos] - last_end
            current_window_sum += free_time
            window.append(free_time)
            max_free_time = max(max_free_time, current_window_sum)

            if len(window) > k:
                current_window_sum -= window.popleft()

            last_end = endTime[pos]

        return max_free_time


if __name__ == "__main__":
    solution = Solution()
    print(
        solution.maxFreeTime(eventTime=5, k=1, startTime=[1, 3], endTime=[2, 5])
    )  # Expected output: 4
    print(
        solution.maxFreeTime(eventTime=10, k=1, startTime=[0, 2, 9], endTime=[1, 4, 10])
    )  # Expected output: 8
    print(
        solution.maxFreeTime(
            eventTime=5, k=2, startTime=[0, 1, 2, 3, 4], endTime=[1, 2, 3, 4, 5]
        )
    )  # Expected output: 9
    print(
        solution.maxFreeTime(10**9, k=1, startTime=[1], endTime=[10**9])
    )  # Expected output: 999999999
