from typing import List


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0

        for num in nums:
            max_or |= num

        def dfs(i: int, curr_or: int) -> int:
            if i == len(nums):
                return 1 if curr_or == max_or else 0

            # Include the current number
            include = dfs(i + 1, curr_or | nums[i])
            exclude = dfs(i + 1, curr_or)

            return include + exclude

        return dfs(0, 0)


if __name__ == "__main__":
    sol = Solution()
    print(sol.countMaxOrSubsets([3, 1]))  # Example test case
    print(sol.countMaxOrSubsets([3, 2, 1, 5]))  # Example test case
