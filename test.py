from typing import List


# Constraint
# 2 <= nums.length <= 100
# -100 <= nums[i] <= 100
class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        maxDist = float("-inf")

        for i in range(len(nums)):
            dist = abs(nums[i] - nums[i - 1])
            maxDist = max(maxDist, dist)

        return maxDist


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxAdjacentDistance([1, 3, 6, 10, 15]))  # Example test case
    print(sol.maxAdjacentDistance([1, 2, 3, 4, 5]))  # Another test case
    print(sol.maxAdjacentDistance([5, 10, 15, 20]))  # Circular distance check
