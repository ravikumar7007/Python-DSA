from typing import List
import heapq


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        """
        Returns the index of the room that is booked the most number of times.
        """
        # Sort meetings by their start time
        meetings.sort()
        # Min-heap for free rooms: (available_time, room_index)
        free_rooms = []
        # Min-heap for occupied rooms: (end_time, room_index)
        occupied_rooms = []
        # Frequency of bookings for each room
        booking_count = [0] * n

        # Initially, all rooms are free at time 0
        for room_index in range(n):
            heapq.heappush(free_rooms, (0, room_index))

        for start, end in meetings:
            # Free up rooms that have become available by the meeting's start time
            while occupied_rooms and occupied_rooms[0][0] <= start:
                available_time, room_index = heapq.heappop(occupied_rooms)
                heapq.heappush(free_rooms, (0, room_index))

            if free_rooms:
                # Assign the meeting to the room with the smallest index
                _, room_index = heapq.heappop(free_rooms)
                booking_count[room_index] += 1
                heapq.heappush(occupied_rooms, (end, room_index))
            else:
                # All rooms are occupied, wait for the earliest one to become free
                available_time, room_index = heapq.heappop(occupied_rooms)
                booking_count[room_index] += 1
                new_end_time = available_time + (end - start)
                heapq.heappush(occupied_rooms, (new_end_time, room_index))

        # Return the room with the highest booking count (smallest index in case of tie)
        max_bookings = max(booking_count)
        return booking_count.index(max_bookings)


if __name__ == "__main__":
    solution = Solution()
    print(
        solution.mostBooked(n=2, meetings=[[0, 10], [1, 5], [2, 7], [3, 4]])
    )  # Expected output: 0
    print(
        solution.mostBooked(n=3, meetings=[[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]])
    )  # Expected output: 0
    print(solution.mostBooked(1, [[0, 10], [5, 15], [10, 20]]))  # Expected output: 0
    print(
        solution.mostBooked(2, [[0, 5], [1, 6], [2, 7], [3, 8]])
    )  # Expected output: 0
