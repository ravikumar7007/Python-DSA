from typing import List


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # Pair each number with its index
        indexed = list(enumerate(nums))
        # Get k largest by value
        k_largest = sorted(indexed, key=lambda x: x[1], reverse=True)[:k]
        # Sort by original index to preserve order
        k_largest.sort(key=lambda x: x[0])
        return [nums[i] for i, _ in k_largest]


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSubsequence([3, 4, 3, 3], 2))  # Output: [4, 3]
    print(sol.maxSubsequence([2, 1, 3, 3], 2))  # Output: [2, 1, 3]
    print(sol.maxSubsequence([-1, -2, 3, 4], 3))  # Output: [3, 4, 5]
