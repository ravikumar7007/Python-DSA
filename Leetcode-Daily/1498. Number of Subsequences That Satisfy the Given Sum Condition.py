from typing import List


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10**9 + 7
        nums.sort()
        n = len(nums)
        power = [1] * n
        for i in range(1, n):
            power[i] = (power[i - 1] * 2) % MOD

        res = 0
        left = 0
        right = n - 1

        while left <= right:
            if nums[left] + nums[right] <= target:
                count = power[right - left]
                res = (res + count) % MOD
                left += 1
            else:
                right -= 1
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.numSubseq([3, 5, 6, 7], 9))  # Output: 4
    print(sol.numSubseq([3, 3, 6, 8], 10))  # Output: 6
    print(sol.numSubseq([2, 3, 3, 4, 6, 7], 12))  # Output: 61
    print(sol.numSubseq([5, 2, 4, 1, 7], 8))  # Output: 16