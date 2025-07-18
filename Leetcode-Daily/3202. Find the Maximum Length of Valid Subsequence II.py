from typing import List


class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        """
        Finds the maximum length of a valid subsequence where each element's value modulo k
        matches a pattern. Uses dynamic programming to track the longest subsequence for each pattern.
        """
        # dp[i][j]: length of subsequence ending with modulo i, previous modulo j
        dp = [[0] * k for _ in range(k)]
        max_length = 0

        for num in nums:
            mod_val = num % k
            for prev_mod in range(k):
                dp[mod_val][prev_mod] = dp[prev_mod][mod_val] + 1
                max_length = max(max_length, dp[mod_val][prev_mod])

        return max_length


if __name__ == "__main__":
    sol = Solution()
    print(sol.maximumLength([1, 4, 2, 3, 1, 4], 3))  # Example test case
    print(sol.maximumLength([1, 2, 3, 4], 2))  # Example test case

    print(sol.maximumLength([5, 10, 15], 5))  # Example test case
