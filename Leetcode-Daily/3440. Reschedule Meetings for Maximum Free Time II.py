from typing import List


class Solution:
    def maxFreeTime(
        self, eventTime: int, startTime: List[int], endTime: List[int]
    ) -> int:
        if eventTime > endTime[-1]:
            startTime.append(eventTime)
            endTime.append(eventTime)

        n = len(startTime)
        sum_free_time = 0
        last_end = 0

        for i in range(n):
            free_time = startTime[i] - last_end
            sum_free_time += free_time
            last_end = endTime[i]

        return sum_free_time
