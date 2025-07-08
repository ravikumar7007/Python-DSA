from typing import List
import heapq


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        """
        Returns the maximum number of events that can be attended.
        Each event is represented as [start_day, end_day].
        """
        # Sort events by their start day
        events.sort()
        n = len(events)
        event_index = 0
        current_day = 1
        attended_events = 0
        min_heap = []

        # Process days as long as there are events left or events in the heap
        while event_index < n or min_heap:
            # If no events are available to attend, jump to the next event's start day
            if not min_heap and event_index < n:
                current_day = max(current_day, events[event_index][0])

            # Add all events starting today or earlier to the heap (by end day)
            while event_index < n and events[event_index][0] <= current_day:
                heapq.heappush(min_heap, events[event_index][1])
                event_index += 1

            # Remove events that have already ended
            while min_heap and min_heap[0] < current_day:
                heapq.heappop(min_heap)

            # Attend the event that ends earliest (if any)
            if min_heap:
                heapq.heappop(min_heap)
                attended_events += 1

            # Move to the next day
            current_day += 1

        return attended_events


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxEvents([[1, 2], [2, 3], [3, 4]]))  # Expected output: 3
    print(solution.maxEvents([[1, 2], [2, 3], [3, 4], [1, 2]]))  # Expected output: 4
    print(
        solution.maxEvents([[1, 2], [2, 3], [3, 4], [1, 2], [4, 5]])
    )  # Expected output: 5
    print(solution.maxEvents([[1, 100000]]))  # Expected output: 1
