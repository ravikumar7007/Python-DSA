from typing import List
import heapq


class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        """
        Finds the minimum difference between the sum of k smallest elements from the first 2k elements
        and the sum of k largest elements from the last 2k elements, after removing k elements.
        """
        n = len(nums)
        k = n // 3

        # Calculate right_max_sum: sum of k largest elements from the right
        max_heap = []
        right_max_sum = [0] * n
        right_sum = 0
        for i in range(n - 1, k - 1, -1):
            heapq.heappush(max_heap, nums[i])
            right_sum += nums[i]
            if len(max_heap) > k:
                right_sum -= heapq.heappop(max_heap)
            if len(max_heap) == k:
                right_max_sum[i] = right_sum

        # Calculate min_diff: minimum difference between left_sum and right_max_sum
        min_heap = []
        min_diff = float("inf")
        left_sum = 0
        for i in range(2 * k):
            heapq.heappush(min_heap, -nums[i])  # Use negative for max-heap
            left_sum += nums[i]
            if len(min_heap) > k:
                left_sum -= -heapq.heappop(min_heap)
            if len(min_heap) == k:
                min_diff = min(min_diff, left_sum - right_max_sum[i + 1])

        return min_diff


# Constraints:
# nums.length == 3 * n
# 1 <= n <= 105
# 1 <= nums[i] <= 105
if __name__ == "__main__":
    solution = Solution()
    print(solution.minimumDifference([3, 1, 2]))  # Example test case
    print(solution.minimumDifference([7, 9, 5, 8, 1, 3]))  # Example test case
    print(solution.minimumDifference([3, 1, 2, 4, 3, 5]))  # Example test case
    print(solution.minimumDifference([1, 2, 3, 4, 5, 6]))  # Example test case
