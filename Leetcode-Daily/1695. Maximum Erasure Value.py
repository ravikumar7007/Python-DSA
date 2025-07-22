from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        """
        Finds the maximum sum of a subarray with all unique elements.
        """
        left = 0
        right = 0
        n = len(nums)
        unique_elements = set()
        max_sum = 0
        current_sum = 0

        while right < n:
            if nums[right] not in unique_elements:
                current_sum += nums[right]
                unique_elements.add(nums[right])
                max_sum = max(max_sum, current_sum)
                right += 1
            else:
                unique_elements.remove(nums[left])
                current_sum -= nums[left]
                left += 1

        return max_sum


if __name__ == "__main__":
    sol = Solution()
    print(sol.maximumUniqueSubarray([4, 2, 4, 5, 6]))  # Output: 17
    print(sol.maximumUniqueSubarray([5, 2, 1, 2, 3, 5]))  # Output: 8
    print(sol.maximumUniqueSubarray([1, 2, 3, 4, 5]))  # Output: 15
    print(sol.maximumUniqueSubarray([1, 1, 1, 1]))  # Output: 1
