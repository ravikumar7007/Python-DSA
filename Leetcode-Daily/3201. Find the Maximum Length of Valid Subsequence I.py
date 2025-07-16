from typing import List


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        """
        Finds the maximum length of a valid subsequence where the parity (even/odd)
        of elements alternates according to one of four possible patterns.
        """
        max_length = 0
        # Patterns: [even, even], [even, odd], [odd, even], [odd, odd]
        patterns = [[0, 0], [0, 1], [1, 0], [1, 1]]

        for pattern in patterns:
            count = 0
            for num in nums:
                if num % 2 == pattern[count % 2]:
                    count += 1
            max_length = max(max_length, count)
        return max_length


if __name__ == "__main__":
    sol = Solution()
    print(sol.maximumLength([1, 2, 3, 4]))            # Example test case
    print(sol.maximumLength([1, 2, 1, 1, 2, 1, 2]))   # Example test case
    print(sol.maximumLength([1, 3]))                  # Example test case
