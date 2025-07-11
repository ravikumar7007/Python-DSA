from typing import List


class Solution:
    def get_free_time(
        self, i: int, top3: List[tuple], startTime: List[int], endTime: List[int]
    ) -> int:
        """
        Calculates the free time for the i-th meeting, considering the top 3 largest gaps.
        """
        last_end = 0 if i == 0 else endTime[i - 1]
        meeting_duration = endTime[i] - startTime[i]
        next_start = startTime[i + 1]
        original_gap = next_start - last_end

        # Check if any of the top 3 gaps can accommodate the current meeting duration
        for gap_length, gap_index in top3:
            if gap_length >= meeting_duration and gap_index != i and gap_index != i + 1:
                return original_gap

        # Otherwise, subtract the meeting duration from the original gap
        return original_gap - meeting_duration

    def maxFreeTime(
        self, eventTime: int, startTime: List[int], endTime: List[int]
    ) -> int:
        """
        Returns the maximum total free time available after rescheduling one meeting.
        """
        # Add a dummy meeting at eventTime if needed
        startTime.append(eventTime)
        endTime.append(eventTime)

        n = len(startTime)
        # Initialize top 3 largest gaps as (gap_length, gap_index)
        top3 = [(startTime[0], 0), (-1, -1), (-1, -1)]

        # Find the top 3 largest gaps between meetings
        for i in range(1, n):
            gap_length = startTime[i] - endTime[i - 1]
            gap_info = (gap_length, i)
            if gap_length > top3[2][0]:
                top3[2] = gap_info
                top3.sort(reverse=True, key=lambda x: x[0])

        max_free_time = 0
        # Calculate the maximum free time by possibly rescheduling each meeting
        for i in range(n - 1):
            free_time = self.get_free_time(i, top3, startTime, endTime)
            max_free_time = max(max_free_time, free_time)
        return max_free_time


if __name__ == "__main__":
    solution = Solution()
    print(
        solution.maxFreeTime(eventTime=41, startTime=[17, 24], endTime=[19, 25])
    )  # Expected output: 4
    print(
        solution.maxFreeTime(eventTime=10, startTime=[0, 7, 9], endTime=[1, 8, 10])
    )  # Expected output: 8
    print(
        solution.maxFreeTime(
            eventTime=10, startTime=[0, 3, 7, 9], endTime=[1, 4, 8, 10]
        )
    )  # Expected output: 9
    print(
        solution.maxFreeTime(
            eventTime=5, startTime=[0, 1, 2, 3, 4], endTime=[1, 2, 3, 4, 5]
        )
    )  # Expected output: 999999999
