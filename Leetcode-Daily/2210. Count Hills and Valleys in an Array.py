from typing import List


class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        """
        Counts the number of hills and valleys in the given array.
        A hill is an element greater than its neighbors, a valley is less.
        """
        hills = 0
        valleys = 0
        i = 1
        prev = 0

        while i < len(nums) - 1:
            next_distinct = i + 1
            if nums[i] == nums[next_distinct]:
                i += 1
                continue

            # Check for hill or valley at position i
            if nums[i] > nums[prev] and nums[i] > nums[next_distinct]:
                hills += 1
            elif nums[i] < nums[prev] and nums[i] < nums[next_distinct]:
                valleys += 1

            prev = i
            i = next_distinct

        return hills + valleys


if __name__ == "__main__":
    nums = [6, 6, 5, 5, 4, 1]
    solution = Solution()
    print(solution.countHillValley(nums))  # Output: expected count of hills and valleys
